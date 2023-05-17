# Android Debloater

Debloater is a Python-based desktop application that allows users to remove or disable unwanted system or third-party applications (also known as "bloatware") on their Android devices using ADB (Android Debug Bridge).

## Getting Started

### Prerequisites

- Python 3.x
- ADB (Android Debug Bridge)

### Installing

1. Clone the repository.
```bash
git clone 
2. Open a terminal or command prompt and navigate to the Debloater directory.
3. Install the required Python packages using pip.

```bash
pip install -r requirements.txt
```
4. Connect your Android device to your computer using a USB cable and make sure that USB debugging is enabled on your device.
5. Launch the Debloater app by running the `main.py` file.
sh python main.py

📋 Copy code
## Usage

1. Enter the package name of the application you want to remove or disable in the "Package Name" field.
2. Select the desired action (enable app, disable app, or uninstall app) using the radio buttons.
3. Click the "Submit" button to execute the selected action.
4. View the logs in the "Logs" section to see the output of the ADB commands.
5. (Optional) Use the "Select App" button to view a list of installed packages and select a package from the list to automatically populate the "Package Name" field.

## Contributing

Contributions are welcome! If you find a bug, have a feature request, or want to contribute code, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
