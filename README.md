# Android Debloater

Debloater is a Python-based desktop application that allows users to remove or disable unwanted system or third-party applications (also known as "bloatware") on their Android devices using ADB (Android Debug Bridge).

## Getting Started

### Prerequisites

- <a href="https://www.python.org/downloads/">Python</a>
- Tkinter - ```sudo apt-get install python3-tk```
- <a href="https://developer.android.com/tools/releases/platform-tools">ADB (Android Debug Bridge)</a>

### Installing

1. Clone the repository.
```bash
git clone https://github.com/Musaddiq-Sultan/Android-Debloater
```

2. Open a terminal or command prompt and navigate to the Debloater directory.
```bash
cd Android-Debloater/
```

3. Connect your Android device to your computer using a USB cable and make sure that USB debugging is enabled on your device.
4. Launch the Debloater app by running the `main.py` file.
```
python3 debloat.py
```

## Usage

1. Enter the package name of the application you want to remove or disable.
2. Select the desired action (enable app, disable app, or uninstall app) using the radio buttons.
3. Click the "Submit" button to execute the selected action.
4. View the logs in the "Logs" section to see the output of the ADB commands.
5. (Optional) Use the "Select App" button to view a list of installed packages and select a package from the list to automatically.
