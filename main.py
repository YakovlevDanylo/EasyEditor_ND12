from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout

app = QApplication([])
win = QWidget()
win.setWindowTitle("Easy Editor")
win.resize(700, 500)

label_image = QLabel("Тут буде картинка")
btn_dir = QPushButton("Папка")
lw_files = QListWidget()

btn_left = QPushButton("Вліво")
btn_right = QPushButton("Вправо")
btn_flip = QPushButton("Дзеркало")
btn_bw = QPushButton("Ч/Б")

row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
row_tools = QHBoxLayout()

col1.addWidget(btn_dir)
col1.addWidget(lw_files)

row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_bw)
