import sys
import magic
import tkinter as tk
from tkinter import messagebox, scrolledtext
import os

def get_file_info(filename):
    try:
        # Create a magic object
        mime = magic.Magic(mime=True)
        
        # Get the MIME type of the file
        mime_type = mime.from_file(filename)
        
        # Create a magic object for detailed information
        magic_info = magic.Magic()
        file_info = magic_info.from_file(filename)
        
        return f"File: {filename}\nMIME Type: {mime_type}\nFile Info: {file_info}"
        
    except Exception as e:
        return f"Error: {e}"

def show_file_info(filename):
    result = get_file_info(filename)
    text_area.delete(1.0, tk.END)  # Clear previous text
    text_area.insert(tk.END, result)  # Insert new result

def copy_to_clipboard():
    result = text_area.get(1.0, tk.END)
    root.clipboard_clear()  # Clear the clipboard
    root.clipboard_append(result)  # Copy the result to the clipboard
    messagebox.showinfo("Copied", "Result copied to clipboard!")

# Create the main window
root = tk.Tk()
root.title("File Info")

# Set the window icon if file.ico exists
if os.path.exists("file.ico"):
    root.iconbitmap("file.ico")

# Create and place the text area to display results
text_area = scrolledtext.ScrolledText(root, width=60, height=20)
text_area.pack(pady=5)

# Create and place the button to copy to clipboard
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)

# Check for command-line arguments
if len(sys.argv) > 1:
    filename = sys.argv[1]
    show_file_info(filename)
else:
    text_area.insert(tk.END, "No file provided. Please provide a file path as an argument.")

# Start the GUI event loop
root.mainloop()
