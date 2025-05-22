import tkinter as tk
from tkinter import filedialog
import webview
import os

def open_dzi_file():
    file_path = filedialog.askopenfilename(filetypes=[("DZI files", "*.dzi")])
    
    if file_path:
        # Get the directory of the DZI file
        dzi_dir = os.path.dirname(file_path)
        dzi_filename = os.path.basename(file_path)
        
        # Create an HTML content string to load the DZI file using OpenSeadragon
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
                    tileSources: "{dzi_filename}"
                }});
            </script>
            <script src="https://code.jquery.com/jquery-3.7.1.min.js" integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo=" crossorigin="anonymous"></script>
        </body>
        </html>
        """
        
        # Save the HTML file in the DZI file's directory
        html_file_path = os.path.join(dzi_dir, "dzi_viewer.html")
        print(f"Saving HTML to: {html_file_path}")
        with open(html_file_path, "w") as html_file:
            html_file.write(html_content)
        
        # Print the DZI file path and directory for debugging
        print(f"Selected DZI file path: {file_path} | DZI directory: {dzi_dir}")
        
        # Launch WebView, loading the HTML file and setting the base URL to the DZI's directory
        webview.create_window(
            'DZI Viewer',
            url=f"file://{html_file_path.replace('\\', '/')}", # Load the HTML file
            width=1000,
            height=800,
            easy_drag=True,
            resizable=True
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
