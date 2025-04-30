import platform
import subprocess

def trace(host):
    command = ['tracert' if platform.system().lower() == 'windows' else 'traceroute', host]
    subprocess.call(command)
