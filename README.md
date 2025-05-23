# File Magic Number Checker for Microsoft Windows


## Overview
This application consists of two components:

1. **File Magic Number Checker** (`file.exe`): A tool for checking the MIME type and detailed magic information of a file.
2. **Installer** (`install_file_magic_number_checker.exe`): A utility to install or uninstall the File Magic number Checker and its context menu.

---

## 1. **File Magic Type Checker**

### Purpose:
The File Magic number Checker allows users to get the MIME type and detailed magic information of a file.

## 2. **Installer**

### Purpose:
The installer allows you to install or uninstall the File Magic number Checker and its context menu integration.

### Features:
- **Install the File Magic number Checker**: This option installs `file.exe` and the associated icon (`file.ico`) to a specified directory.
- **Add Context Menu**: The installer also adds an entry to your Windows context menu that allows you to check the magic number of files directly from the right-click menu.
- **Uninstall**: Remove the application and its context menu entry.

### Steps to Use the Installer:

1. **Run the Installer**:
   - Right click on `install_file_magic_number_checker` and select "Run as administrator" to open the installation window.
   
2. **Installation Process:**
   - In the installation window, you'll see an input field for the installation path.
     - By default, it will suggest the path `C:\Users\<YourUsername>\AppData\Roaming\file magic number checker`.
     - You can change this path by typing a different directory or leave it as default.
   - Click on **Install** to begin the installation process.
     - If required files (`file.exe` and `file.ico`) are not found, an error message will appear.
   - Upon successful installation, you will see a message confirming the installation path.

3. **Context Menu Integration:**
   - The installer will add a **"Check file magic number"** option to the right-click context menu for all files.
   - Right-click on any file and select **"Check file magic number"** to launch the File Magic number Checker for that file.

4. **Uninstallation:**
   - To uninstall, open the installer again as administrator and click on **Uninstall**.
   - If the application is installed, it will be removed along with the context menu integration.
   - If the program isn't installed, a message will notify you that it was not found.

---

## Important Notes:
- **Administrator Privileges**: 
   - The installer requires administrator privileges to modify the context menu and install the application properly. If you run the installer without administrator rights, it will notify you and exit.
  
- **File Paths**: 
   - Ensure that the file paths you provide to the application are correct. The tool works best when given the absolute path to the file.

