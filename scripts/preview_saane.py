"""SAANE local preview and one-way, allowlisted Obsidian synchronization."""
import argparse, hashlib, json, os, shutil, socket, subprocess, time, webbrowser
from pathlib import Path
from import_obsidian import Importer

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'scripts/obsidian-publication.json'
NOTE = 'BIM 6D/5_Natural Ventilation.md'

def fingerprint(manifest_path):
    raw = manifest_path.read_bytes()
    manifest = json.loads(raw.decode('utf-8-sig'))
    digest = hashlib.sha256(raw)
    vault = Path(manifest['vault'])
    for key in sorted(set(manifest['notes']) | set(manifest.get('assets', []))):
        path = (vault / key).resolve()
        if not path.is_relative_to(vault.resolve()):
            raise ValueError('Source escapes vault: ' + key)
        digest.update(key.encode())
        digest.update(path.read_bytes())
    return digest.hexdigest()

def sync(root=ROOT, manifest_path=MANIFEST, note=NOTE):
    before = fingerprint(manifest_path)
    manifest = json.loads(manifest_path.read_text(encoding='utf-8-sig'))
    importer = Importer(manifest, root)
    importer.run(note, write=False)
    if before != fingerprint(manifest_path):
        raise ValueError('Source is still being saved; retrying shortly.')
    changed = 0
    for rel, data in importer.pending.items():
        target = Path(root) / rel
        if target.exists() and target.read_bytes() == data:
            continue
        # Keep a first-sync backup of the previous article, outside Hugo content.
        if str(rel).replace('\\', '/').startswith('content/') and target.exists():
            backup = Path(root) / '.saane-preview/backups' / rel
            backup.parent.mkdir(parents=True, exist_ok=True)
            if not backup.exists():
                shutil.copy2(target, backup)
        target.parent.mkdir(parents=True, exist_ok=True)
        temporary = target.with_name(target.name + '.saane-tmp')
        temporary.write_bytes(data)
        os.replace(temporary, target)
        changed += 1
    return changed

from publish_sync import sync, fingerprint

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--once', action='store_true')
    parser.add_argument('--no-browser', action='store_true')
    args = parser.parse_args()
    if args.once:
        print('SYNC:', sync(), 'file(s) updated', flush=True)
        return
    # One watcher per project. The operating system releases this lock on exit.
    import msvcrt
    state = ROOT / '.saane-preview'
    state.mkdir(exist_ok=True)
    lock = (state / 'watcher.lock').open('a+b')
    lock.write(b'0'); lock.flush(); lock.seek(0)
    try:
        msvcrt.locking(lock.fileno(), msvcrt.LK_NBLCK, 1)
    except OSError:
        print('SAANE autosync is already running. Use its existing terminal.')
        return
    server = None
    try:
        print('Obsidian -> Hugo: publish:true + website_section:research. Ctrl+C to stop.', flush=True)
        print('Metadata comes from Obsidian. Only referenced attachments are copied. Local preview, no internet deployment.', flush=True)
        last = None
        try:
            print('SYNC:', sync(), 'file(s) updated', flush=True)
            last = fingerprint(MANIFEST)
        except Exception as error:
            print('SYNC ERROR (previous article retained):', error, flush=True)
        with socket.socket() as probe:
            occupied = probe.connect_ex(('127.0.0.1', 1313)) == 0
        if occupied:
            print('Port 1313 already active; reusing preview. Autosync remains active.', flush=True)
        else:
            server = subprocess.Popen(['hugo', 'server', '--bind', '127.0.0.1', '--port', '1313', '--renderToMemory', '--disableFastRender', '--noBuildLock'], cwd=ROOT)
        opened = args.no_browser
        observed = None
        stable_since = time.monotonic()
        last_error = None
        while True:
            if server and server.poll() is not None:
                raise RuntimeError('Hugo stopped; see build messages above.')
            if not opened:
                import urllib.request
                try:
                    with urllib.request.urlopen('http://127.0.0.1:1313/research/natural-ventilation/', timeout=1) as response:
                        if response.status == 200:
                            webbrowser.open('http://127.0.0.1:1313/research/natural-ventilation/')
                            opened = True
                except OSError:
                    pass
            try:
                current = fingerprint(MANIFEST)
                if current != observed:
                    observed = current
                    stable_since = time.monotonic()
                if current != last and time.monotonic() - stable_since >= 1.5:
                    changed = sync()
                    last = current
                    last_error = None
                    print(time.strftime('%H:%M:%S'), 'SYNC OK:', changed, 'file(s) updated', flush=True)
            except Exception as error:
                if str(error) != last_error:
                    print('SYNC ERROR (fix source/manifest to retry):', error, flush=True)
                    last_error = str(error)
            time.sleep(1)
    except KeyboardInterrupt:
        print('\nSAANE autosync stopped.', flush=True)
    finally:
        if server and server.poll() is None:
            server.terminate()
            try: server.wait(timeout=5)
            except subprocess.TimeoutExpired: server.kill()
        lock.close()

if __name__ == '__main__':
    main()

