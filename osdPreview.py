import tkinter as tk
from tkinter import filedialog
import webview
import os

def open_dzi_file():
    file_path = filedialog.askopenfilename(filetypes=[("DZI files", "*.dzi")])
    print("filepath ", file_path)
    if file_path:
        # Create a file URL for the DZI file with forward slashes
        file_url = f"file://{os.path.abspath(file_path).replace('\\', '/')}"
        # Print the file path and URL for debugging
        print(f"Selected file path: {file_path} | File URL: {file_url}")
        base = os.path.dirname(file_path)
        relative_path = os.path.basename(file_path)
        print("Relative PATH ", relative_path)
        # Create an HTML file to load the DZI file using OpenSeadragon
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>DZI Viewer</title>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/openseadragon/3.0.0/openseadragon.min.js"></script>
            <style>
                #openseadragon1 {{
                    width: 100%;
                    height: 100vh;
                }}
            </style>
        </head>
        <body>
            <div id="openseadragon1"></div>
            <script>
                var viewer = OpenSeadragon({{
                    id: "openseadragon1",
                    prefixUrl: "https://cdnjs.cloudflare.com/ajax/libs/openseadragon/3.0.0/images/",
                    showRotationControl: true,
                    tileSources: "{relative_path}"
                }});
            </script>
            <script src="https://code.jquery.com/jquery-3.7.1.min.js" integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo=" crossorigin="anonymous"></script>
        </body>
        </html>
        """
        
        base_path = os.path.join(base, "dzi_viewer.html")
        print("ospath...", os.path.dirname(base), "BASE ", base, "os path base and dzi", os.path.join(base, "dzi_viewer.html") )
        with open(base_path, "w") as html_file:
            html_file.write(html_content)
        
        # Print the HTML file path for debugging
        print("Attempting to launch WebView...")
        webview.create_window(
            'DZI Viewer',
            base_path,
            width=1000,
            height=800,
            easy_drag=True,
            resizable=True,
            # fullscreen=False     # Optional: start in fullscreen
            )
        webview.start()

# Create the main window
root = tk.Tk()
root.title("DZI Viewer")
root.configure(background='blue')

frame = tk.Frame(
    root, 
    bg="blue", 
    padx=2, 
    pady=2
    )
frame.pack(pady=20)

# Create a button to open DZI files
open_button = tk.Button(
    frame,
    text="Open DZI File",
    command=open_dzi_file,
    font = ('Courier', 16),
    width=20,
    heigh=2,
    borderwidth=5,
    relief="raised"
    )
open_button.pack(pady=20)

# Run the application
root.mainloop()
