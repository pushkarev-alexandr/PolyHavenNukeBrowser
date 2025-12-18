from PySide6.QtWidgets import QApplication
import sys

from ui.gui import AssetBrowserWindow


def main():
    app = QApplication(sys.argv)
    win = AssetBrowserWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
