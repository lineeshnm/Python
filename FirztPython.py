#! python3

import subprocess


def ExecCommand(cmd):
    subprocess.call(cmd, shell=True)


def PrintHello():
    print("Hello Function")

if __name__ == '__main__':
    for i in range(5):
        PrintHello()
        ExecCommand("dir")
