import mermaid from "./vendor/mermaid/mermaid.esm.min.mjs";
mermaid.initialize({startOnLoad:false,securityLevel:"strict",theme:"base",themeVariables:{fontFamily:"Jost, sans-serif",primaryColor:"#eeede7",primaryTextColor:"#202020",primaryBorderColor:"#62625E",lineColor:"#62625E",secondaryColor:"#F7F6F2",tertiaryColor:"#F7F6F2"}});
try { await mermaid.run({querySelector:".sr-page .mermaid"}); }
catch (error) { console.error("Mermaid could not render; diagram source remains available.", error); }
