import sys
import subprocess

# Check for PyQt5 and PyQtWebEngine installation
try:
    from PyQt5.QtCore import Qt, QUrl
    from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QLineEdit, QPushButton, QVBoxLayout, QWidget
    from PyQt5.QtWebEngineWidgets import QWebEngineView
except ImportError:
    print("Some required packages are missing. Installing...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'PyQt5', 'PyQtWebEngine'])
    from PyQt5.QtCore import Qt, QUrl
    from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QLineEdit, QPushButton, QVBoxLayout, QWidget
    from PyQt5.QtWebEngineWidgets import QWebEngineView

class BantorConfigsBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.browser.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter URL and press Enter(Made By Benjamin Chan and BANTOR-Configs Team)")
        self.url_input.returnPressed.connect(self.navigate)

        self.go_button = QPushButton("Go")
        self.go_button.clicked.connect(self.navigate)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.browser.back)

        self.forward_button = QPushButton("Forward")
        self.forward_button.clicked.connect(self.browser.forward)

        layout = QVBoxLayout()
        layout.addWidget(self.url_input)
        layout.addWidget(self.go_button)
        layout.addWidget(self.back_button)
        layout.addWidget(self.forward_button)
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        self.browser.urlChanged.connect(self.updateUrlBar)

        self.setWindowTitle("BANTOR-Configs Browser")
        self.setGeometry(100, 100, 1024, 768)

    def navigate(self):
        url = self.url_input.text()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url

        self.browser.setUrl(QUrl(url))

    def updateUrlBar(self, q):
        self.url_input.setText(q.toString())
        self.url_input.setCursorPosition(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = BantorConfigsBrowser()
    browser.show()
    sys.exit(app.exec_())
