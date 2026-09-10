了解。**Python版のREADME.mdを1つにまとめた完全版**です。Pythonが音声解析を担当する構成です。

````markdown
# 🎧 Spectrum Analyzer

Pythonでマイクから音声を取得し、リアルタイムでFFT解析を行うスペクトラムアナライザーです。

Python側で音声の取得・解析・データ処理を行い、Webブラウザ側のHTMLで解析結果をリアルタイムに表示します。

---

## 🛠️ 使用技術

| 技術 | 用途 |
|---|---|
| 🐍 Python | 音声取得・音声解析・Webサーバー処理 |
| NumPy | FFT・数値計算・周波数解析 |
| SoundDevice | PCのマイクから音声を取得 |
| HTTP Server | PythonからWebページと解析データを提供 |
| JSON | PythonとWebブラウザ間のデータ通信 |
| HTML5 | Webページの構造 |
| CSS3 | デザイン・レイアウト |
| JavaScript | 解析データの取得・画面更新 |
| Canvas API | スペクトラムグラフの描画 |

---

## 🔧 技術構成

```text
🎙️ PCマイク
    │
    ▼
🐍 Python
    │
    ▼
🎤 SoundDevice
    │
    ▼
📊 NumPy
    │
    ▼
⚡ FFT解析
    │
    ├──────────────┐
    ▼              ▼
🔊 音量計算     📈 周波数解析
    │              │
    └──────┬───────┘
           ▼
        📦 JSON
           │
           ▼
🌐 Python HTTP Server
           │
           ▼
      📄 index.html
           │
           ▼
      JavaScript
           │
           ▼
      🖼️ Canvas API
           │
           ▼
    📊 Spectrum Graph
````

---

## 🐍 Python処理版について

このバージョンでは、**音声解析をPythonが担当します。**

ブラウザは解析そのものを行うのではなく、Pythonから送られてきた解析結果を受け取って表示します。

```text
Python
├── マイク入力
├── 音声データ取得
├── FFT
├── 周波数解析
├── 音量計算
├── ピーク周波数検出
└── JSONデータ生成

        ↓

HTML / JavaScript
├── JSON取得
├── 数値表示
└── グラフ描画
```

---

## 📊 スペクトラムとは？

スペクトラムは、音声に含まれている周波数成分を表示したものです。

音には低い音から高い音まで、さまざまな周波数が含まれています。

```text
低い音                                      高い音
 │                                             │
 ▼                                             ▼
30Hz ───── 100Hz ───── 1kHz ───── 10kHz ───── 20kHz
```

Spectrum Analyzerでは、これらの周波数ごとの強さをリアルタイムで表示します。

---

## ⚡ FFTとは？

FFT（Fast Fourier Transform）は、音声信号を周波数成分へ変換するための高速な計算方法です。

```text
時間領域
〰️〰️〰️〰️〰️〰️〰️
       │
       │ FFT
       ▼
周波数領域
█  ██  █████  ██  █
30Hz ─────────── 20kHz
```

PythonではNumPyのFFT機能を使用して音声データを解析します。

---

## 🎙️ 音声入力

`SoundDevice`を使用してPCのマイクから音声データを取得します。

```text
🎙️ マイク
   ↓
SoundDevice
   ↓
Python
   ↓
NumPy配列
   ↓
FFT解析
```

---

## 📈 主な機能

* 🎙️ PCマイクからリアルタイム音声入力
* ⚡ PythonによるリアルタイムFFT解析
* 📊 リアルタイムスペクトラム表示
* 🔊 AUDIO LEVEL表示
* 📌 PEAK FREQUENCY表示
* 📡 JSONによる解析データ通信
* 🌐 Python HTTP Server
* ⏸️ 一時停止
* ▶️ 解析再開
* ■ 解析停止
* 🧹 グラフクリア
* 🖥️ WebブラウザUI

---

## 📁 ファイル構成

```text
SpectrumAnalyzer/
│
├── spectrum.py
│   └── Python音声解析・Webサーバー
│
├── index.html
│   └── Web画面・グラフ表示
│
└── README.md
    └── プロジェクト説明
```

---

## 🐍 spectrum.py

`spectrum.py`はPython側のメインプログラムです。

主に以下の処理を行います。

```text
🎙️ マイク入力
      ↓
音声データ取得
      ↓
NumPy配列へ変換
      ↓
平均値除去
      ↓
ハニング窓
      ↓
FFT
      ↓
振幅計算
      ↓
dB変換
      ↓
周波数計算
      ↓
ピーク周波数検出
      ↓
スペクトラムデータ生成
      ↓
JSON
      ↓
Webブラウザへ提供
```

---

## 🌐 index.html

`index.html`はブラウザ側の表示を担当します。

Pythonが解析したデータをHTTP経由で取得し、JavaScriptで画面を更新します。

```text
🐍 Python
   │
   │ JSON
   ▼
📄 index.html
   │
   ▼
JavaScript
   │
   ├── 音量表示
   ├── 周波数表示
   └── グラフ更新
           │
           ▼
       📊 Canvas
```

---

## 📦 必要な環境

Python 3.xが必要です。

必要なライブラリ：

```bash
pip install numpy sounddevice
```

### 使用ライブラリ

```text
NumPy
SoundDevice
```

---

## 🚀 起動方法

### 1. ファイルをダウンロード

以下のファイルを用意してください。

```text
spectrum.py
index.html
```

### 2. 同じフォルダに保存

```text
SpectrumAnalyzer/
├── spectrum.py
└── index.html
```

### 3. ライブラリをインストール

ターミナルで以下を実行します。

```bash
pip install numpy sounddevice
```

### 4. Spectrum Analyzerを起動

```bash
python spectrum.py
```

### 5. ブラウザで使用

Pythonサーバーが起動すると、Webブラウザが自動的に開きます。

通常は以下のアドレスでアクセスできます。

```text
http://127.0.0.1:8765/index.html
```

---

## 🌐 Python HTTP Server

Python側でローカルHTTPサーバーを起動します。

```text
┌─────────────────────────────┐
│       Python Server         │
│                             │
│  index.html                 │
│       +                     │
│  /api/spectrum              │
│       ↓                     │
│      JSON                   │
└─────────────┬───────────────┘
              │
              ▼
        🌐 Web Browser
```

解析データはJSONとしてブラウザへ送信されます。

---

## 📡 JSONデータ

Pythonからブラウザへ、例えば次のようなデータを送信します。

```json
{
  "spectrum": [12, 18, 25, 40, 65],
  "level": -20,
  "frequency": 440,
  "sample_rate": 44100,
  "status": "解析中"
}
```

### データの意味

| データ           | 内容        |
| ------------- | --------- |
| `spectrum`    | スペクトラムデータ |
| `level`       | 音声レベル     |
| `frequency`   | ピーク周波数    |
| `sample_rate` | サンプルレート   |
| `status`      | 現在の状態     |

---

## ⚙️ 解析設定

現在の主な解析設定です。

```text
サンプルレート
44100 Hz

FFTサイズ
4096

解析周波数
約30 Hz ～ 20 kHz

スペクトラムバー
128本
```

### FFTサイズについて

FFTサイズを大きくすると、より細かく周波数を分析できます。

一方で、処理するデータ量が増えるため、PCの性能によっては負荷が高くなる場合があります。

---

## 🖥️ 画面構成

```text
┌────────────────────────────────────────────────────┐
│ 〽 SPECTRUM ANALYZER                       ● ONLINE │
├───────────────────────────────────────┬────────────┤
│                                       │ AUDIO LEVEL│
│                                       │   -20 dB   │
│          REALTIME SPECTRUM            ├────────────┤
│                                       │ PEAK FREQ  │
│       █                               │   440 Hz   │
│       █       ██                      ├────────────┤
│   █   █   █   ██                      │ AUDIO INFO │
│ █ █ █ █ █████████                     │ FFT 4096   │
│███████████████████                    │ 44100 Hz   │
│                                       ├────────────┤
│───────────────────────────────────────│ ▶ START    │
│ 30Hz  100Hz  1kHz  10kHz  20kHz      │ ⏸ PAUSE    │
│                                       │ ■ STOP     │
└───────────────────────────────────────┴────────────┘
```

---

## 🆚 Web処理版との違い

| 項目           | Python版            | Web処理版        |
| ------------ | ------------------ | ------------- |
| 音声処理         | 🐍 Python          | 🌐 ブラウザ       |
| FFT          | NumPy              | Web Audio API |
| マイク          | SoundDevice        | Web Audio API |
| サーバー         | Python HTTP Server | 不要            |
| JavaScript   | 表示処理               | 音声解析・表示       |
| Python       | ✅ 使用               | ❌ 不要          |
| GitHub Pages | ソース公開のみ            | ✅ そのまま動作      |
| インストール       | Python + ライブラリ     | 基本不要          |

---

## 💡 Python版の特徴

```text
✅ Pythonで音声解析
✅ NumPyでFFT
✅ SoundDeviceでマイク入力
✅ JSONでデータ通信
✅ HTMLでグラフ表示
✅ ローカルHTTPサーバー
✅ 音声解析処理をPython側に集約
```

---

## 🔒 プライバシー

このプロジェクトでは、基本的に音声解析を実行しているPC上で処理します。

マイクから取得した音声を外部サービスへ送信することを目的としたプログラムではありません。

使用する環境や追加した機能によって通信内容が変わる場合があるため、実際のコードを確認して利用してください。

---

## 🔐 マイクについて

マイクが正常に認識されない場合は、以下を確認してください。

```text
・マイクが接続されているか
・OSでマイクが有効になっているか
・Pythonにマイクへのアクセス権限があるか
・別のアプリがマイクを使用していないか
・SoundDeviceが正常にインストールされているか
```

---

## 🛠️ トラブルシューティング

### `ModuleNotFoundError` が表示される

以下を実行してください。

```bash
pip install numpy sounddevice
```

---

### `index.html` が見つからない

`spectrum.py`と`index.html`を同じフォルダに保存してください。

```text
SpectrumAnalyzer/
├── spectrum.py
└── index.html
```

---

### マイクを開始できない

OSのマイク設定と、Pythonから利用できる入力デバイスを確認してください。

---

### ブラウザが開かない

以下のアドレスをブラウザで開いてください。

```text
http://127.0.0.1:8765/index.html
```

---

## 🌐 GitHubで公開する場合

GitHubにはPython版のソースコードを公開できます。

```text
GitHub
   │
   ▼
SpectrumAnalyzer
   ├── spectrum.py
   ├── index.html
   └── README.md
```

ただし、**GitHub PagesではPythonプログラムを実行できません。**

GitHub PagesでWebページとして動作させたい場合は、Python版ではなくWeb処理版を使用してください。

Python版は、GitHubをソースコードの公開場所として利用し、実際の音声解析はPythonを実行できるPCやサーバーで行います。

---

## 📥 ダウンロードして使用

以下のファイルをダウンロードして、同じフォルダに保存してください。

```text
spectrum.py
index.html
```

保存後、必要なライブラリをインストールします。

```bash
pip install numpy sounddevice
```

その後、以下を実行してください。

```bash
python spectrum.py
```

Pythonサーバーが起動し、WebブラウザからSpectrum Analyzerを使用できます。

---

## ⚠️ 注意事項

* Python 3.xが必要です。
* NumPyとSoundDeviceが必要です。
* PCのマイクが必要です。
* マイクへのアクセスが許可されている必要があります。
* `spectrum.py`と`index.html`は同じフォルダに保存してください。
* Pythonプログラムを終了すると解析も終了します。
* GitHub PagesではPythonを実行できません。
* 使用するマイクやPC環境によって解析結果が変化する場合があります。

---

## 📜 License

Copyright © Spectrum Analyzer Project

このプロジェクトのソースコードを利用・改変・再配布する場合は、設定されているライセンスの条件に従ってください。

---

## 🎧 Spectrum Analyzer

Pythonで音を取得し、FFTで解析。

解析したデータをJSONとしてWebブラウザへ送り、リアルタイムで音を「見る」ことができます。

```text
🎙️ PCマイク
     │
     ▼
🐍 Python
     │
     ▼
🎤 SoundDevice
     │
     ▼
📊 NumPy
     │
     ▼
⚡ FFT
     │
     ▼
📦 JSON
     │
     ▼
🌐 HTTP Server
     │
     ▼
📄 HTML / JavaScript
     │
     ▼
📈 Canvas
     │
     ▼
🎧 Spectrum Analyzer
```

**Python × NumPy × SoundDevice × HTML × JavaScript × Canvas**

Pythonで音声解析を行い、Webブラウザでリアルタイムに可視化するスペクトラムアナライザーです。

```
```
