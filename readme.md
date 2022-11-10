###### Setting up a Virtual Environment (Windows) ######

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv/Scripts/Activate.ps1

# If the Activate errors, try running this on PowerShell (Administrator mode)
Set-ExecutionPolicy RemoteSigned

# Upgrade pip
pip install --upgrade pip

# Install libraries
pip install -r requirements.txt
