import os

def ask_terminal():
    while True:
        terminal_input = input("Do you want to run the launcher in the terminal? (True/False): ").lower()
        if terminal_input in ['true', 'false']:
            return terminal_input == 'true'
        else:
            print("Invalid input. Please enter 'True' or 'False'.")

def ask_save_location():
    while True:
        save_location = input("Enter the path where you want to save the launcher: ")
        if os.path.isdir(save_location):
            return save_location
        else:
            print("Invalid path. Please enter a valid directory path.")

def create_launcher(name, command, icon_path, path="/usr/lib/qt6/bin/designer", terminal=False, save_location="."):
    """Creates a desktop launcher file with specified details."""
    
    terminal_str = 'true' if terminal else 'false'

    launcher_content = f"""[Desktop Entry]
Version=1.0
Type=Application
Name={name}
Comment={name}
Exec={command}
Icon={icon_path}
Path={path}
Terminal={terminal_str}
StartupNotify=false"""

    try:
        with open(os.path.join(save_location, f"{name}.desktop"), "w") as f:
            f.write(launcher_content)
            print(f"Launcher '{name}.desktop' created successfully!")
    except OSError as e:
        print(f"Error creating launcher: {e}")

# Get user input for launcher details
name = input("Enter the desired launcher name: ")
command = input("Enter the command to execute: ")
icon_path = input("Enter the path to the icon: ")

# Ask user for terminal and save location
terminal = ask_terminal()
save_location = ask_save_location()

# Create the launcher
create_launcher(name, command, icon_path, save_location=save_location, terminal=terminal)
