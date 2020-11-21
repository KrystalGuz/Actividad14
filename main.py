from PySide2.QtWidgets import QPushButton, QApplication
import sys
from mainwindow import MainWindow

# Aplicación de Qt
app = QApplication()
window = MainWindow()
# Se hace visible el botón
window.show()
# Qt loop
sys.exit(app.exec_())