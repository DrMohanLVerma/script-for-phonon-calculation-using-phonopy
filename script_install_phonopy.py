# Python script to install Phonopy on Ubuntu 20.04

import os
import subprocess

def run_command(command, description):
    """
    Runs a shell command and prints its status.
    """
    print(f"\n[INFO] {description}...")
    try:
        subprocess.run(command, check=True, shell=True)
        print(f"[SUCCESS] {description} completed.")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] {description} failed: {e}")
        exit(1)

# Step 1: Update the system
run_command("sudo apt update && sudo apt upgrade -y", "Updating and upgrading the system")

# Step 2: Install Python and dependencies
run_command(
    "sudo apt install -y python3 python3-pip python3-venv build-essential libopenblas-dev liblapack-dev gfortran", 
    "Installing Python and necessary dependencies"
)

# Step 3: Install Phonopy via pip
run_command("pip3 install --user phonopy", "Installing Phonopy using pip")

# Step 4: Verify installation
print("\n[INFO] Verifying Phonopy installation...")
try:
    phonopy_version = subprocess.check_output("phonopy --version", shell=True, text=True).strip()
    print(f"[SUCCESS] Phonopy installed successfully. Version: {phonopy_version}")
except subprocess.CalledProcessError:
    print("[ERROR] Phonopy installation verification failed. Make sure it is installed correctly.")
    exit(1)

# Step 5: Add Phonopy to PATH (optional)
print("\n[INFO] Adding Phonopy to PATH...")
user_bin_path = os.path.expanduser("~/.local/bin")
if user_bin_path not in os.environ["PATH"]:
    bashrc_path = os.path.expanduser("~/.bashrc")
    with open(bashrc_path, "a") as bashrc:
        bashrc.write(f"\n# Add Phonopy to PATH\nexport PATH=\"{user_bin_path}:$PATH\"\n")
    print("[INFO] PATH updated. Please run 'source ~/.bashrc' or restart your terminal.")
else:
    print("[INFO] Phonopy is already in PATH.")

print("\n[INFO] Phonopy installation script completed.")

