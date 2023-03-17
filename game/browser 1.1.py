import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView


class WebView(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My Web View')
        self.load(QUrl('https://www.silvergames.com/en/mega-brick-breaker'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    web_view = WebView()
    web_view.show()
    sys.exit(app.exec_())

