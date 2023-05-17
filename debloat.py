from tkinter import *
from tkinter import messagebox
import subprocess

counter = 0

def main():
    root = Tk()
    root.title("Debloater")
    root.geometry("380x700")
    root.resizable(0, 0)
    
    def apps_list():
        def select_app():
            # Get the selected text from the listbox
            selection = listbox.selection_get()
            app_entry.delete(0, END)
            app_entry.insert(0, selection)
            
            child.destroy()
        
        # Get the list of installed packages
        result = subprocess.run(["adb", "shell", "pm", "list", "packages"], capture_output=True, text=True)
        packages = [line.split(":")[1] for line in result.stdout.splitlines()]
        packages.sort()

        child = Toplevel(root)
        child.title("Package Names")
        child.geometry("400x700")
        
        # Create a frames
        list_frame = Frame(child)
        button_frame = Frame(child)
        
        list_frame.pack(expand=True, fill="both", padx=5, pady=(5, 0))
        button_frame.pack(fill="x", padx=5)
        
        scrollbar = Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")
        listbox = Listbox(list_frame, yscrollcommand=scrollbar.set)
        for package in packages:
            listbox.insert(END, package)
        listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=listbox.yview)
        Button(button_frame, text="Select", command=select_app).pack(side="right", padx=5, pady=5)
    
    def clear_logs():
        logs_text.delete("1.0", END)
    
    # Creating Functions
    def clear_text(event):
        global counter
        if counter == 0:
            app_entry.delete(0, "end")
        counter = 1

    def refresh():
        result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
        output = result.stdout.strip()
        logs_text.insert(END, f"\n{output}")
        
    def submit():
        global counter
        package_name = app_entry.get()
        radio_value = radio_button.get()
        
        app_entry.delete(0, END)
        counter = 1

        if radio_value == 1:
            result = subprocess.run(["adb", "shell", "pm", "enable", package_name], capture_output=True, text=True)
        elif radio_value == 2:
            result = subprocess.run(["adb", "shell", "pm", "disable-user", "--user", "0", package_name], capture_output=True, text=True)
        elif radio_value == 3:
            confirm = messagebox.askyesno("Uninstall", f"Do you want to remove cache data?")
            if confirm == False:
                result = subprocess.run(["adb", "shell", "su", "-c", f"pm uninstall --user 0 {package_name}"], capture_output=True, text=True)
            else:
                result = subprocess.run(["adb", "shell", "su", "-c", f"pm uninstall -k --user 0 {package_name}"], capture_output=True, text=True)

        # Get the output and error messages from the result object
        output = result.stdout.strip()
        errors = result.stderr.strip()
        
        if output != "":
            logs_text.insert(END, f"\n{output}")
        if "Unknown package:" in errors:
            logs_text.insert(END, f"\nError: No Such Package Was Found")
        elif package_name.strip() == "":
            logs_text.insert(END, f"\nError: No Package Or Component Specified")
        elif errors != "":
            logs_text.insert(END, f"\n{errors}")

    # Creating Frames
    frame_01 = Frame(root)
    frame_02 = Frame(root)
    frame_03 = Frame(root)
    logs_frame = LabelFrame(root, text="Logs")
    
    # Create a scrollbar for the logs_frame widget
    scrollbar = Scrollbar(logs_frame)
    scrollbar.pack(side="right", fill="y")

    # Creating the Text widget for logs
    logs_text = Text(logs_frame, yscrollcommand=scrollbar.set)
    logs_text.pack(expand=True, fill="both")

    # Configure the scrollbar to scroll the logs_text widget
    scrollbar.config(command=logs_text.yview)

    frame_01.pack(fill="x", padx=5, pady=5)
    frame_02.pack(fill="x", padx=(0, 5), pady=5)
    frame_03.pack(fill="x", padx=(0, 5), pady=5)
    logs_frame.pack(expand=True, fill="both", padx=5, pady=5)

    # Creating entries
    default_package = "com.example.app"
    app_entry = Entry(frame_01)
    app_entry.pack(expand=True, fill="x", padx=(0, 5), ipady="5")
    app_entry.insert(0, default_package)
    app_entry.bind("<FocusIn>", clear_text)
    
    # Creating radio buttons
    radio_button = IntVar(value=1)
    radio_button_1 = Radiobutton(frame_02, text="Enable App", variable=radio_button, value=1)
    radio_button_2 = Radiobutton(frame_02, text="Disable App", variable=radio_button, value=2)
    radio_button_3 = Radiobutton(frame_02, text="Uninstall App", variable=radio_button, value=3)

    radio_button_1.grid(row=0, column=0)
    radio_button_2.grid(row=0, column=1)
    radio_button_3.grid(row=0, column=2)

    # Creating buttons
    refresh_button = Button(frame_03, text="Refresh", command=refresh)
    submit_button = Button(frame_03, text="Submit", command=submit)
    list_button = Button(frame_03, text="Select App", command=apps_list)
    clear_logs_button = Button(frame_03, text="Clear Logs", command=clear_logs)
    frame_03.columnconfigure(0, weight=4)

    submit_button.grid(row=0, column=0, sticky="ew")
    refresh_button.grid(row=0, column=1, sticky="ew")
    clear_logs_button.grid(row=0, column=2, sticky="ew")
    list_button.grid(row=0, column=3, sticky="ew")

    # Starting the mainloop
    root.mainloop()
main()