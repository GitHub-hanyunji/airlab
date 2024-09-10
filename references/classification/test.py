from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

class Tab1Content(QWidget):
    def __init__(self):
        super().__init__()
        #self.setupUi(self)
        self.pushButton_2.clicked.connect(self.A)
    def A(self):
        self.label_2.setText(f"select folder path :")

class Tab2Content(QWidget):
    def __init__(self):
        super().__init__()
        #self.setupUi(self)
        self.pushButton.clicked.connect(self.A)
    def A(self):
        self.label.setText(f"select folder path :")

class MainWindow(QTabWidget,):
    def __init__(self):
        super().__init__()
        uic.loadUi("untitled03.ui", self)  # 전체 UI를 로드합니다.

        # 탭 위젯에서 각 탭에 대한 위젯 가져오기
        self.tab1 = self.findChild(QWidget, 'tab1')  # main_window.ui에서 설정한 Tab1의 위젯 이름
        self.tab2 = self.findChild(QWidget, 'tab2')  # main_window.ui에서 설정한 Tab2의 위젯 이름
        
        # 각 탭의 기능을 설정합니다.
        self.tab1_content = Tab1Content()
        self.tab2_content = Tab2Content()

        # 탭에 내용 추가
        self.tab1_layout = QVBoxLayout(self.tab1)
        self.tab1_layout.addWidget(self.tab1_content)

        self.tab2_layout = QVBoxLayout(self.tab2)
        self.tab2_layout.addWidget(self.tab2_content)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
