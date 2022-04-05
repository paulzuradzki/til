```
# settings.json
  # this config allows use of Anaconda prompt (and thus environments) in VS Code
  # the settings are quite esoteric. Note the following parameters:
    # "terminal.integrated.shell.windows"
    # "terminal.integrated.shellArgs.windows"
  # references: http://mscodingblog.blogspot.com/2017/08/setup-integrated-terminal-in-vs-code-to.html 
  
# TODO: set up Java
    # "java.home": "C:\\Users\\pzuradzki\\Downloads\\java-1.8.0-openjdk-1.8.0.262-3.b10.redhat.windows.x86_64\\java-1.8.0-openjdk-1.8.0.262-3.b10.redhat.windows.x86_64\\bin\\javac.exe",
    # "java.home": "C:\\Program Files\\AdoptOpenJDK\\jdk-8.0.232.09-hotspot"

{

    // prevent folders from expanding when opening new file
    "explorer.autoReveal": false,

    "editor.suggestSelection": "first",
    "vsintellicode.modify.editor.suggestSelection": "automaticallyOverrodeDefaultValue",
    "java.home": "C:\\Users\\pzuradzki\\Downloads\\amazon-corretto-11.0.8.10.1-windows-x64-jdk\\jdk11.0.8_10",
    "java.semanticHighlighting.enabled": true,
    "editor.minimap.enabled": false,
    "breadcrumbs.enabled": false,
    "editor.renderWhitespace": "none",
    "window.zoomLevel": 1,
    "editor.mouseWheelZoom": true,
    "python.languageServer": "Microsoft",
    "python.defaultInterpreterPath": "C:\\Users\\pzuradzki\\AppData\\Local\\Continuum\\miniconda3\\envs\\dev\\python.exe",
    "python.dataScience.sendSelectionToInteractiveWindow": true,
    "terminal.integrated.shell.windows": "C:\\Windows\\System32\\cmd.exe", 
    "terminal.integrated.shellArgs.windows": ["/K", "C:\\Users\\pzuradzki\\AppData\\Local\\Continuum\\miniconda3\\Scripts\\activate.bat C:\\Users\\pzuradzki\\AppData\\Local\\Continuum\\miniconda3 & conda activate dev"],
    "python.pythonPath": "C:\\Users\\pzuradzki\\AppData\\Local\\Continuum\\miniconda3\\envs\\dev\\python.exe",
    "python.autoComplete.extraPaths": []
}
```
