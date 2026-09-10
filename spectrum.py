import http.server
import socketserver
import threading
import json
import os
import webbrowser
import time

import numpy as np
import sounddevice as sd


# ==============================
# 設定
# ==============================

PORT = 8765
SAMPLE_RATE = 44100
FFT_SIZE = 4096

HTML_FILE = "index.html"

# 現在の解析データ
audio_data = {
    "spectrum": [0] * 128,
    "level": -60,
    "frequency": 0,
    "sample_rate": SAMPLE_RATE,
    "status": "待機中"
}

data_lock = threading.Lock()
running = True


# ==============================
# 音声解析
# ==============================

def audio_callback(indata, frames, time_info, status):
    global audio_data

    if status:
        print("Audio:", status)

    # モノラル化
    samples = indata[:, 0].astype(np.float32)

    if len(samples) < FFT_SIZE:
        return

    # 最新部分だけ使用
    samples = samples[-FFT_SIZE:]

    # DC成分を除去
    samples = samples - np.mean(samples)

    # ハニング窓
    window = np.hanning(len(samples))
    samples_windowed = samples * window

    # FFT
    fft_result = np.fft.rfft(samples_windowed)

    # 振幅
    magnitude = np.abs(fft_result)

    # 正規化
    magnitude = magnitude / (len(samples) / 2)

    # dB変換
    db = 20 * np.log10(magnitude + 1e-10)

    # 30Hz～20kHz付近を使用
    frequencies = np.fft.rfftfreq(
        len(samples),
        1 / SAMPLE_RATE
    )

    # 周波数範囲
    min_freq = 30
    max_freq = 20000

    mask = (
        (frequencies >= min_freq) &
        (frequencies <= max_freq)
    )

    selected_freq = frequencies[mask]
    selected_db = db[mask]

    if len(selected_db) == 0:
        return

    # 128本のバーにまとめる
    bar_count = 128

    indexes = np.linspace(
        0,
        len(selected_db) - 1,
        bar_count
    ).astype(int)

    spectrum = selected_db[indexes]

    # 見やすい範囲に調整
    spectrum = np.clip(
        spectrum,
        -90,
        0
    )

    # 0～100に変換
    spectrum_normalized = (
        (spectrum + 90) / 90
    ) * 100

    # 全体の音量
    rms = np.sqrt(
        np.mean(samples ** 2)
    )

    level_db = 20 * np.log10(
        rms + 1e-10
    )

    level_db = float(
        np.clip(level_db, -60, 0)
    )

    # 一番強い周波数
    peak_index = np.argmax(selected_db)
    peak_frequency = float(
        selected_freq[peak_index]
    )

    # データ更新
    with data_lock:
        audio_data = {
            "spectrum": spectrum_normalized.tolist(),
            "level": level_db,
            "frequency": peak_frequency,
            "sample_rate": SAMPLE_RATE,
            "status": "解析中"
        }


# ==============================
# 音声入力開始
# ==============================

def start_audio():

    try:

        stream = sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="float32",
            blocksize=FFT_SIZE,
            callback=audio_callback
        )

        stream.start()

        print("🎙 マイク入力を開始しました")
        print(f"サンプルレート : {SAMPLE_RATE} Hz")
        print(f"FFTサイズ      : {FFT_SIZE}")

        return stream

    except Exception as e:

        print()
        print("❌ マイクを開始できませんでした")
        print(e)
        print()
        print("マイクが使用できるか確認してください。")

        return None


# ==============================
# HTTPサーバー
# ==============================

class Handler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/api/spectrum":

            with data_lock:
                response = json.dumps(
                    audio_data
                ).encode("utf-8")

            self.send_response(200)

            self.send_header(
                "Content-Type",
                "application/json; charset=utf-8"
            )

            self.send_header(
                "Cache-Control",
                "no-cache"
            )

            self.send_header(
                "Access-Control-Allow-Origin",
                "*"
            )

            self.end_headers()

            self.wfile.write(response)

            return

        return super().do_GET()

    def log_message(self, format, *args):
        # アクセスログを表示しない
        pass


# ==============================
# メイン
# ==============================

def main():

    global running

    folder = os.path.dirname(
        os.path.abspath(__file__)
    )

    os.chdir(folder)

    if not os.path.exists(HTML_FILE):

        print(
            "❌ index.html が見つかりません。"
        )

        input(
            "Enterキーで終了..."
        )

        return

    print("=" * 45)
    print("       🎧 Spectrum Analyzer")
    print("=" * 45)
    print()
    print("🐍 Python音声解析モード")
    print()
    print("音声解析 : Python")
    print("FFT      : NumPy")
    print("音声入力 : sounddevice")
    print("表示     : HTML / JavaScript")
    print()

    # 音声入力開始
    stream = start_audio()

    if stream is None:

        input(
            "Enterキーで終了..."
        )

        return

    # サーバー開始
    try:

        with socketserver.ThreadingTCPServer(
            ("127.0.0.1", PORT),
            Handler
        ) as server:

            server.allow_reuse_address = True

            url = (
                f"http://127.0.0.1:"
                f"{PORT}/index.html"
            )

            print()
            print("🌐 ブラウザ:")
            print(url)
            print()
            print("終了する場合:")
            print("Ctrl + C")
            print()

            # ブラウザを起動
            webbrowser.open(url)

            try:

                server.serve_forever()

            except KeyboardInterrupt:

                print()
                print("終了しています...")

    finally:

        running = False

        try:
            stream.stop()
            stream.close()
        except:
            pass

        print("🎧 音声入力を停止しました")
        print("終了しました。")


if __name__ == "__main__":
    main()
