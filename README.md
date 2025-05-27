# dzOpen

*Windows Binary (.exe) release is [here](https://github.com/cioran0/dzOpen/releases/download/v1.0.0-windows/dzOpen1.0.exe) and Linux is forthcoming if you just want to download/install the app.* 

Uses [OpenSeaDragon](https://openseadragon.github.io/), [Tkinter](https://wiki.python.org/moin/TkInter), [Pywebview](https://pywebview.flowrl.com/) to render a [dzi](https://learn.microsoft.com/en-us/previous-versions/windows/silverlight/dotnet-windows-silverlight/cc645050(v=vs.95)?redirectedfrom=MSDN) locally. .dzi/tiled image pyramid are used in biomedical imaging, microscopy, professional photography, aerospace/telescopy imaging, art preservation etc. This app is useful if you want to check a dzi quickly but not enough to spin up a server. 

https://github.com/user-attachments/assets/8a03eb00-c10a-4b19-bdbc-18c2192b9019

Only requirement is python webview, which can be installed ```pip install pywebview``` on windows. On Linux you have to pick gtk or qt so it's either ```pip install pywebview[qt]``` or ```pip install pywebview[gtk]```. Mentioned in requirements.txt

If you want to create dzi's OTOH check [libvips](https://www.libvips.org/) and my gui for that [dzSaver](https://github.com/cioran0/dzSaver).

- Fixed parent directory issue. As far as I know. Will open parent directory of current directory of first dzi now The `webview` is now launched with the `url` pointing directly to this `dzi_viewer.html` file
- Confirmed working on windows. I don't own a mac. I'm remedying the linux version. 
- writes an html file to the same directory as the dzi file.
- for compatibility, and to cut down on add'l path issues, loads OSD and OSD buttons from the source, not local
- Added (windows) executable in releases. Unsigned, because a certificate in windows costs $ and this is FOSS built in my kitchen, click "More info" -> "Run anyway". Need to build for linux.
- Linux executable problematic. Changes to fix pathing may have had unintended consequences on Linux version breaking pathing.
- If you are experiencing a problem running the file with McAfee Antivirus, uninstalling McAfee Antivirus should fix the problem
- If you are running Windows 7, newer versions of Python such as used in this may not function properly. Upgrading is recommended
- The Linux problems may have something to do with pyWebview OS differences or caching
- [Sample Dzi files](https://github.com/cioran0/sampleDzi)  for user testing. Endusers please ignore
