from tkinter import *
from tkinter import messagebox, PhotoImage
import os
import subprocess

###-----[ INITIALIZING GLOBAL VARIABLES ]-----###
empty_entry = False
main_dir = os.path.dirname(os.path.abspath(__file__))
adb_path = os.path.join(main_dir, "adb")

def main():
    ###-----[ CREATING MAIN WINDOW WITH BASIC SETTINGS ]-----###
    root = Tk()
    root.title("Debloater")
    img = PhotoImage(file=os.path.join(main_dir, "icon.png"))
    root.iconphoto(True, img)
    root.geometry("500x750")
    root.minsize(500, 750)

    ###-----[ CREATING FUNCTION TO SHOW LIST OF APPS ]-----###
    def apps_list():
        def select_app():
            selection = listbox.selection_get()
            app_entry.delete(0, END)
            app_entry.insert(0, selection)
            child.destroy()
        
        ###-----[ GETTING LIST OF PACKAGES USING ADB ]-----###
        result = subprocess.run([adb_path, "shell", "pm", "list", "packages"], capture_output=True, text=True)
        packages = [line.split(":")[1] for line in result.stdout.splitlines()]
        packages.sort()

        ###-----[ CREATING CHILD WINDOW FOR PACKAGE LIST ]-----###
        child = Toplevel(root)
        child.title("Package Names")
        child.geometry("400x700")
        
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
    
    ###-----[ CREATING FUNCTION TO CLEAR LOGS ]-----###
    def clear_logs():
        logs_text.delete("1.0", END)
    
    ###-----[ CREATING FUNCTION TO CLEAR DEFAULT TEXT ]-----###
    def clear_text(event):
        global empty_entry
        if not empty_entry:
            app_entry.delete(0, "end")
        empty_entry = True

    ###-----[ CREATING FUNCTION TO REFRESH DEVICES ]-----###
    def refresh():
        result = subprocess.run([adb_path, "devices"], capture_output=True, text=True)
        output = result.stdout.strip()
        logs_text.insert(END, f"\n{output}")
        
    ###-----[ CREATING FUNCTION TO HANDLE PACKAGE OPERATIONS ]-----###
    def submit():
        global empty_entry
        package_name = app_entry.get()
        radio_value = radio_button.get()
        
        if package_name.strip() == "":
            logs_text.insert(END, f"\nError: No Package Or Component Specified")
            return
        
        app_entry.delete(0, END)
        empty_entry = True

        if radio_value == 1:
            result = subprocess.run([adb_path, "shell", "pm", "enable", package_name], capture_output=True, text=True)
        elif radio_value == 2:
            result = subprocess.run([adb_path, "shell", "pm", "disable-user", package_name], capture_output=True, text=True)
        elif radio_value == 3:
            confirm = messagebox.askyesno("Uninstall", f"Do you want to remove cache data?")
            if confirm == False:
                result = subprocess.run([adb_path, "shell", "su", "-c", f"pm uninstall --user 0 {package_name}"], capture_output=True, text=True)
            else:
                result = subprocess.run([adb_path, "shell", "su", "-c", f"pm uninstall -k --user 0 {package_name}"], capture_output=True, text=True)

        output = result.stdout.strip()
        errors = result.stderr.strip()
        
        if output != "":
            logs_text.insert(END, f"\n{output}")
        if "Unknown package:" in errors:
            logs_text.insert(END, f"\nError: No Such Package Was Found")
            return
        elif errors != "":
            logs_text.insert(END, f"\n{errors}")

    ###-----[ CREATING AND CONFIGURING FRAMES ]-----###
    frame_01 = Frame(root)
    frame_01.columnconfigure(0, weight=1)

    frame_02 = Frame(root)
    for i in range(3):
        frame_02.columnconfigure(i, weight=1)

    frame_03 = Frame(root)
    for i in range(3):
        frame_03.columnconfigure(i, weight=1)
    
    logs_frame = LabelFrame(root, text="Logs")
    logs_frame.columnconfigure(0, weight=1)
    logs_frame.rowconfigure(0, weight=1)
    
    scrollbar = Scrollbar(logs_frame)
    scrollbar.pack(side="right", fill="y")

    logs_text = Text(logs_frame, yscrollcommand=scrollbar.set)
    logs_text.pack(expand=True, fill="both")

    scrollbar.config(command=logs_text.yview)

    frame_01.pack(fill="x", padx=5, pady=5)
    frame_02.pack(fill="x", padx=5, pady=(0, 5))
    frame_03.pack(fill="x", padx=5, pady=(0, 5))
    logs_frame.pack(expand=True, fill="both", padx=5, pady=5)

    ###-----[ CREATING BUTTONS AND ENTRY WIDGETS ]-----###
    refresh_button = Button(frame_03, text="Refresh", command=refresh)
    submit_button = Button(frame_03, text="Submit", command=submit)
    clear_logs_button = Button(frame_03, text="Clear Logs", command=clear_logs)
    list_button = Button(frame_01, text="Select App", command=apps_list)

    default_package = "com.example.app"
    app_entry = Entry(frame_01)
    app_entry.grid(row=0, column=0, ipady=4, sticky="ew")
    list_button.grid(row=0, column=1, sticky="ew")
    app_entry.insert(0, default_package)
    app_entry.bind("<FocusIn>", clear_text)
    
    ###-----[ CREATING RADIO BUTTONS ]-----###
    radio_button = IntVar(value=1)
    radio_button_1 = Radiobutton(frame_02, text="Enable App", variable=radio_button, value=1)
    radio_button_2 = Radiobutton(frame_02, text="Disable App", variable=radio_button, value=2)
    radio_button_3 = Radiobutton(frame_02, text="Uninstall App", variable=radio_button, value=3)

    radio_button_1.grid(row=0, column=0)
    radio_button_2.grid(row=0, column=1)
    radio_button_3.grid(row=0, column=2)

    submit_button.grid(row=0, column=0, sticky="ew")
    refresh_button.grid(row=0, column=1, sticky="ew")
    clear_logs_button.grid(row=0, column=2, sticky="ew")

    ###-----[ STARTING MAIN APPLICATION LOOP ]-----###
    root.mainloop()

if __name__ == "__main__":
    main()
