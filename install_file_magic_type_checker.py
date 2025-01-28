import os
import shutil
import sys
import tkinter as tk
from tkinter import messagebox
import ctypes
import winreg
import subprocess

# Constants
INSTALLATION_FOLDER_NAME = "file magic type checker"
DEFAULT_INSTALL_PATH = os.path.join(os.getenv("APPDATA"), INSTALLATION_FOLDER_NAME)
DATA_FOLDER = "data"  # Folder where file.exe and file.ico are located
ICON_PATH = os.path.join(DATA_FOLDER, "file.ico")  # Path to the installer icon
EXE_PATH = os.path.join(DATA_FOLDER, "file.exe")    # Path to the executable to install

# Check if the program is running as administrator
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Check if required files exist
def check_required_files_exist():
    return os.path.exists(EXE_PATH) and os.path.exists(ICON_PATH)

# Create the context menu
def create_context_menu(install_path):
    try:
        # Create the registry key for the context menu
        key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, r"*\\shell\\Check file magic type")
        winreg.SetValue(key, "", winreg.REG_SZ, "Check file magic type")

        # Add the icon value, referencing the copied icon in the installation folder
        icon_path = os.path.join(install_path, "file.ico")
        winreg.SetValueEx(key, "Icon", 0, winreg.REG_SZ, icon_path)

        # Create the command key for executing the program
        command_key = winreg.CreateKey(key, "command")
        command_path = f'"{os.path.join(install_path, "file.exe")}" "%1"'
        winreg.SetValue(command_key, "", winreg.REG_SZ, command_path)

        # Close the registry keys
        winreg.CloseKey(command_key)
        winreg.CloseKey(key)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create context menu: {e}")

# Remove the context menu
def remove_context_menu():
    try:
        # Use the reg.exe command to delete the entire 'Check file magic type' subkey
        command = r'reg delete "HKCR\*\shell\Check file magic type" /f'
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode == 0:
            return True  # Successfully removed
        else:
            # Show an error message if the command fails
            messagebox.showerror("Error", f"Failed to remove context menu: {result.stderr.strip()}")
            return False
    except Exception as e:
        # Handle unexpected errors
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
        return False


# Install files
def install_files(install_path):
    try:
        # Create the installation directory if it doesn't exist
        if not os.path.exists(install_path):
            os.makedirs(install_path)

        # Copy the executable and icon to the installation directory
        shutil.copy(EXE_PATH, install_path)
        shutil.copy(ICON_PATH, install_path)

        # Create the context menu
        create_context_menu(install_path)
    except Exception as e:
        messagebox.showerror("Error", f"Installation failed: {e}")

# Uninstall files
def uninstall_files(install_path):
    try:
        # Remove the installation directory and its contents
        if os.path.exists(install_path):
            shutil.rmtree(install_path)

        # Remove the context menu
        if not remove_context_menu():
            messagebox.showwarning("Uninstall Incomplete", "Failed to remove context menu. Some changes may persist.")
            return False  # Uninstallation incomplete

        return True  # Successfully uninstalled
    except Exception as e:
        messagebox.showerror("Error", f"Uninstallation failed: {e}")
        return False

# Install button handler
def on_install():
    install_path = entry.get().strip()
    if not install_path:
        install_path = DEFAULT_INSTALL_PATH

    if not check_required_files_exist():
        messagebox.showerror("Error", "Required files (file.exe and file.ico) not found in the data folder.")
        return

    install_files(install_path)
    messagebox.showinfo("Success", f"Installed to {install_path}")

# Uninstall button handler
def on_uninstall():
    if not os.path.exists(DEFAULT_INSTALL_PATH):
        messagebox.showinfo("Info", "The program is not installed.")
        return

    if uninstall_files(DEFAULT_INSTALL_PATH):
        messagebox.showinfo("Success", "Uninstalled successfully.")

if __name__ == "__main__":
    # Check for administrator privileges
    if not is_admin():
        # Show an error message using a Tkinter popup window
        tk.Tk().withdraw()  # Hide the root window
        messagebox.showerror("Administrator Privileges Required", "This program must be run as an administrator.")
        sys.exit(1)

    # Create the main window
    root = tk.Tk()
    root.title("Install File Magic Type Checker")

    # Set the window icon if file.ico exists
    if os.path.exists(ICON_PATH):
        root.iconbitmap(ICON_PATH)

    # Create and place the installation path input
    label = tk.Label(root, text="Installation Path:")
    label.pack(pady=5)

    entry = tk.Entry(root, width=50)
    entry.pack(pady=5)
    entry.insert(0, DEFAULT_INSTALL_PATH)  # Set default path

    # Create and place the install button
    install_button = tk.Button(root, text="Install", command=on_install)
    install_button.pack(pady=5)

    # Create and place the uninstall button
    uninstall_button = tk.Button(root, text="Uninstall", command=on_uninstall)
    uninstall_button.pack(pady=5)

    # Start the GUI event loop
    root.mainloop()

