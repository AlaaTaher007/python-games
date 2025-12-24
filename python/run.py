import subprocess

app_name = "ping_pong"

command = f"python -m apps.{app_name}.main"

# Run the command using Popen
process = subprocess.Popen(command, shell=True)

# (optional) Wait for it to  finish
process.wait() 
