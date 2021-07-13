# Configuring custom shortcuts for JupyterLab

### Problem
I often do things like restart the kernel and clear variables. I'd like to do this without the GUI.

### Steps
* Go to Settings > Keyboard Shortcuts
* Edit right-hand window "User Preferences" with a dict in the format below
* Hit Save/disc icon in upper-right for the shortcut to take effect

### Example custom shortcut format

```
{"shortcuts": [{
              "command": "kernelmenu:restart-and-clear",
              "keys": ["Ctrl Alt Shift R"],
              "selector": "[data-jp-kernel-user]:focus"
               }
]
}
```
