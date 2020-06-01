#! /usr/bin/env python

import subprocess
import os
import sys


def win_main():
    print("win_main() start")

    cmd = 'dir'

    # os.system("dir")
    try:
        res = subprocess.run(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    except:
        print("subprocess.check_output() failed")

    print(res.stdout.decode('shift-jis'))

    return


def linux_main():
    return


if __name__ == '__main__':
    print("start main")
    print("your os = ", os.name)
    if os.name == "nt":
        win_main()
    else:
        linux_main()
