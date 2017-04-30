import os
import sys
from justdb.server import create_server


def kill():
    justdb_cmd = "justdb serve"
    cmd = "kill $(ps aux | grep '" + justdb_cmd + "' | grep -v grep | awk '{print $2}')"
    os.system(cmd)


def main():
    command = sys.argv[1]
    if command == "kill":
        kill()
    elif command == "serve":
        create_server()
    else:
        print("Run 'justdb kill|serve'")
