import http.server
import socketserver
import webbrowser
import os

PORT = 8765
HTML_FILE = "index.html"


class Handler(http.server.SimpleHTTPRequestHandler):
    pass


def main():
    folder = os.path.dirname(
        os.path.abspath(__file__)
    )

    os.chdir(folder)

    if not os.path.exists(HTML_FILE):
        print("index.html が見つかりません。")
        input("Enterキーで終了...")
        return

    url = f"http://127.0.0.1:{PORT}/index.html"

    with socketserver.TCPServer(
        ("127.0.0.1", PORT),
        Handler
    ) as server:

        print("================================")
        print(" Spectrum Analyzer")
        print("================================")
        print()
        print(f"URL: {url}")
        print()
        print("ブラウザを起動しています...")
        print("終了する場合は Ctrl + C")
        print()

        webbrowser.open(url)

        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print()
            print("終了しました。")


if __name__ == "__main__":
    main()
