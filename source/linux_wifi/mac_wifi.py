import subprocess
import re


class mac_WiFi_class:
    # Wi-Fi関連ユーティリティ

    @staticmethod
    def getUsingSSID():
        # 現在接続中のWi-FiのSSIDを取得する
        # returns:
        #   str -- SSID

        # wifiの状況を確認するコマンドを実行する
        cmd = [
            '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport',
            '-I']
        cmd_res = subprocess.run(cmd, stdout=subprocess.PIPE)

        # コマンドの実行結果をoutputに保存する
        output = cmd_res.stdout.decode('utf-8')

        # 文字列から、SSIDと書かれた部分を取得する
        matchs = re.findall(r' +SSID: .+', output)
        res = ""

        if len(matchs) > 0:
            res = matchs[0]
            res = re.sub(r'^ +SSID: ', '', res)
            res = res.rstrip()
        return res
