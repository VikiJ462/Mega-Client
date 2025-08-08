import tkinter as tk
import subprocess
import os

def install():
    bat_file = "install-mega-client.bat"
    if os.path.exists(bat_file):
        subprocess.run([bat_file], shell=True)
    else:
        output_label.config(text="❌ File 'install-mega-client.bat' not found!")

app = tk.Tk()
app.title("Mega Client Installer")
app.geometry("500x400")
app.resizable(False, False)

# Install button
install_button = tk.Button(app, text="Install", font=("Arial", 16, "bold"), command=install, bg="lightgreen", fg="black", padx=10, pady=5)
install_button.pack(pady=20)

# How to install
instructions = """
How to install:
1. Install Fabric from https://fabricmc.net and choose Minecraft version 1.21
2. Go to %APPDATA%\\.minecraft and delete the folder "mods"
3. Click "Install"

How to launch:
1. Open your Minecraft launcher
2. Launch installation named "fabric-loader-1.21"
"""

instructions_label = tk.Label(app, text=instructions, justify="left", font=("Arial", 12), wraplength=480)
instructions_label.pack(pady=10)

# Output/Error label
output_label = tk.Label(app, text="", fg="red", font=("Arial", 10))
output_label.pack(pady=5)

app.mainloop()
