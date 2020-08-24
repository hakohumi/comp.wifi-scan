#! /usr/bin/env python

# OSに合わせて、実行するpythonファイルを選択する

import os
import sys

from win_wifi_pkg.win_wifi import win_WiFi_class as win
# from linux_wifi


class WiFiUtil:

    # Win用アプリ 起動用
    @staticmethod
    def win_main():
        win.main()
        return

    # Linux用アプリ 起動用
    @staticmethod
    def linux_main():
        return

    # 現在の仕様OSを確認する
    @staticmethod
    def view_os():

        print(
            "Python {0:s} {1:d}bit on {2:s}\n".format(
                " ".join(
                    item.strip() for item in sys.version.split("\n")),
                64 if sys.maxsize > 0x100000000 else 32,
                sys.platform))
        print("\nDone.")
        return


if __name__ == '__main__':
    path = os.getcwd()
print(path)

print("start main")
print("your os = ", os.name)
if os.name == "nt":
    WiFiUtil.view_os()

    WiFiUtil.win_main()

    # 現在のWiFiのSSIDを取得する
    res = win.getUsingSSID()
    print(res)

# else:
#     linux_main()
