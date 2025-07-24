cd "$(dirname "$0")" || exit 1
script_path="$(pwd)"

if [ ! -d "${script_path}/venv" ]; then
    echo -e "Virtual environment not found. \
    \nCreate a new one by running the following command: \
    \npython3 -m venv \"${script_path}/venv\" \
    \nThen run the script again."
    exit 1
else
    source "${script_path}/venv/bin/activate"
    
    if ! command -v pyinstaller &> /dev/null;
    then
        echo -e "pyinstaller not found in virtual environment\nInstall it by running the following commands: \
        \nsource \"${script_path}/venv/bin/activate\" \
        \npip3 install pyinstaller\nThen run the script again."
        exit 1
    fi

    pyinstaller --clean --onefile --windowed \
    --add-data="${script_path}/icon.png:." \
    --add-data="${script_path}/adb:." \
    --name "AndroidDebloater" \
    "${script_path}/main.py"
fi