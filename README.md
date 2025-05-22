# dzOpen

Uses [OpenSeaDragon](https://openseadragon.github.io/), [Tkinter](https://wiki.python.org/moin/TkInter), [Pywebview](https://pywebview.flowrl.com/) to render a dzi tiled image pyramid locally. This is useful if you want to check a dzi but not enough to spin up a server. Only requirement is python webview, which can be installed ```pip install pywebview``` on windows. On Linux you have to pick gtk or qt so it's either ```pip install pywebview[qt]``` or ```pip install pywebview[gtk]```. Mentioned in requirements.txt

- Fixed parent directory issue. As far as I know. Will open parent directory of current directory of first dzi now The `webview` is now launched with the `url` pointing directly to this `dzi_viewer.html` file
- Confirmed working on windows and linux. I don't own a mac.
- writes an html file to the same directory as the dzi file.
- for compatibility, and to cut down on add'l path issues, loads OSD and OSD buttons from the source, not local

https://github.com/user-attachments/assets/8a03eb00-c10a-4b19-bdbc-18c2192b9019



