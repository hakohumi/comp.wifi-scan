# comp.wifi-scan

wifiをスキャンする

## フローチャート

![flow chart](フローチャート/wifi-scan.png)

## 現在の状況

+ ファイルの分割
  + windows用とlinu用で分けたい

+ Windows に対応中
  + ssidのリスト取得
    + "netsh wlan show networks mode=Bssid"コマンドでリストを取得しようと思ったが、WlanScanをしないと、キャッシュからのリードとなり、最新のAPが取得できない
      + win32wifiのライブラリでいけそう
        + ssidは取得しようとすることはできた
        + プログラムを実行したあとに、コマンドを実行すると、最新のリストが取得できる。

## 今後の展望


+ 他のOSにも対応
  + Linux
  + macOS
+ WiFiの電波の強度を確認する
  