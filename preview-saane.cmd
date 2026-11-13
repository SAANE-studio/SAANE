@echo off
setlocal
cd /d "%~dp0"
if not exist "hugo.toml" if exist "saane-hugo\hugo.toml" cd /d "saane-hugo"
if not exist "scripts\preview_saane.py" (
  echo ERROR: Folder proyek saane-hugo tidak ditemukan di dekat launcher.
  pause
  exit /b 1
)
title SAANE - Obsidian Sync and Preview
where hugo >nul 2>nul
if errorlevel 1 (
  echo ERROR: Hugo tidak ditemukan.
  pause
  exit /b 1
)
where python >nul 2>nul
if errorlevel 1 (
  echo ERROR: Python 3.10 atau lebih baru diperlukan.
  pause
  exit /b 1
)
echo Edit catatan publish:true dan website_section:research di Obsidian lalu simpan.
echo Biarkan terminal ini terbuka. Ctrl+C untuk berhenti.
python -u "scripts\preview_saane.py"
if errorlevel 1 pause
endlocal


