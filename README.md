# dzOpen

Uses OpenSeaDragon, Tkinter, Pywebview to render a dzi tiled image pyramid locally. 
- Currently there's an issue w/Pywebview and it's only accurately reading files from the directory it's invoked (where the dzi file is) and directories below it, and not parent directories. The workaround is to close and re-open the program, it resets the home directory for the pywebview localserver. I'm still working on it
- writes an html file to the same firectory as the dzi file.
- for compatibility, and to cut down on add'l path issues, loads OSD and OSD buttons from the source, not local

https://github.com/user-attachments/assets/8a03eb00-c10a-4b19-bdbc-18c2192b9019



