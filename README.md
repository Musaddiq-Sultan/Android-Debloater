# Android Debloater

**Android Debloater** is a lightweight Python-based desktop application that allows you to remove, disable, or enable pre-installed system and third-party apps ("bloatware") from your Android device using **ADB (Android Debug Bridge)**, all through a simple graphical interface built with Tkinter.

<p align="center">
  <img src="icon.png" alt="Android Debloater Logo" width="512" height="512">
</p>

---

## Features

- View installed packages
- Disable any system or third-party app
- Enable previously disabled apps
- Uninstall system/third-party apps (root only)
- GUI-based (no terminal knowledge required)
- Built-in ADB binary

---

## 1. Running the App (Prebuilt Executable)

If you're not a developer and just want to use the tool:

### Prerequisites

- USB Debugging must be enabled on your Android phone
- A USB cable to connect your phone

### Steps

1. Download the precompiled Linux binary from the [Releases](https://github.com/Musaddiq-Sultan/Android-Debloater/releases).
2. (Linux only) Make it executable:
   ```bash
   chmod +x AndroidDebloater
    ```

4. Run it directly:
   ```bash
   ./AndroidDebloater
   ```

   or double-click the executable.

---

## 2. Build It Yourself (Linux)

If you'd like to build the executable yourself:

### Prerequisites

* Python 3
* `python3-tk` installed:

  ```bash
  sudo apt install python3-tk
  ```

### Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/Musaddiq-Sultan/Android-Debloater
   ```
   ```bash
   cd Android-Debloater
   ```

2. Install tkinter:
   ```bash
   sudo apt install python3-tk
   ```

3. Run the builder script:

   ```bash
   bash builder.sh
   ```

This will generate a single standalone file (`dist/AndroidDebloater`) which includes your GUI app, embedded `adb`, and icon.

---

## Manual Python Usage (For Developers)

If you prefer to run the app without building an executable:

1. Connect your Android phone with USB debugging enabled
2. Run:

   ```bash
   python3 main.py
   ```

---

## Usage

* Select an app or enter the package name manually
* Click Refresh
* Choose an action:
  * Enable App
  * Disable App
  * Uninstall App (Root only)
* Click Submit
* Check the Logs for results

---

## Author

[Musaddiq Sultan](https://github.com/Musaddiq-Sultan)
