from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox

from polyhaven.api import get_types


class AssetBrowserWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PolyHaven Asset Browser")

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("Asset type:"))

        self.type_combo = QComboBox()
        layout.addWidget(self.type_combo)

        self.populate_types()

    def populate_types(self):
        try:
            types = get_types()
        except Exception:
            types = []

        if types:
            # Ensure all items are strings
            self.type_combo.addItems([str(t) for t in types])
        else:
            self.type_combo.addItem("Unavailable")

