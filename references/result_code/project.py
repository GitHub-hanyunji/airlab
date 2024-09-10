import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QThread,pyqtSignal
from PIL import Image
import time
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

Test_form=uic.loadUiType("TestUI.ui")[0]

class Test(QWidget,Test_form):
    
    def __init__(self):
        super().__init__()
        self.model_directory.clicked.connect(lambda:self.test_openFolderDialog("model_path"))
        self.test_directory.clicked.connect(lambda:self.test_openFolderDialog("test_folder_path"))
        self.training.clicked.connect(self.test_show)

    def display_output(self,text):
        self.shell_2.append(text)  # 터미널 출력을 텍스트 위젯에 추가합니다.
    def test_openFolderDialog(self,path_type):
        # 파일 다이얼로그를 열어 사용자가 파일을 선택하도록 함
        # file_path = QFileDialog.getExistingDirectory(self, "폴더 선택", "")
        folder_path=QFileDialog.getExistingDirectory(self, "폴더 선택", "")
        if folder_path:
            if path_type == "test_folder_path":
                self.test_folder_path = folder_path
                self.file_dirShow2.setText(f"Select Test File path: {self.test_folder_path}")
            elif path_type == "model_path":
                self.model_path = folder_path
                self.file_dirShow2.setText(f"Select Model File path: {self.model_path}")
        else:
            self.file_dirShow2.setText("File not selected")
    def test_show(self):
        class_label = ['cat', 'dog']
        # load pth model
        model = train.torch.load(f"{self.model_path}\\model.pth", weights_only=False)
        # set model to inference mode
        model.eval()
        print(model)

        transform = train.torchvision.transforms.Compose([      
                train.torchvision.transforms.Resize(256),      # 이미지 크기 256x256으로 조정   
                train.torchvision.transforms.CenterCrop(224),  # 중앙을 기준으로 224x224로 자르기 
                train.torchvision.transforms.ToTensor(),       # 이미지를 텐서로 변환 
                train.torchvision.transforms.Normalize(        # 정규화 
                mean=[0.485, 0.456, 0.406],        # 이미지 정규화 평균
                std=[0.229, 0.224, 0.225])         # 이미지 정규화 표준편차
        ])
        # 테스트 이미지 디렉토리 설정
        test_dir = self.test_folder_path
        train.os.chdir(test_dir)   # 작업 디렉토리 변경
        list = train.os.listdir(test_dir)
        file_num = 20
        acc_num = 0
        self.test_figure = Figure()
        self.test_canvas = FigureCanvas(self.test_figure)
        test_widget = self.findChild(QWidget, 'train_image')
        layout = QVBoxLayout(test_widget)
        layout.addWidget(self.test_canvas)
        rows = 4
        cols = 5
        number = 0
        for file in list:
            start_time = time.time()
            print(file)
            test_image = Image.open(file)
            img = transform(test_image)
            print(img.shape)
            img = img.to('cpu')
            with train.torch.no_grad():
                pred = model(img.unsqueeze(0))
                print(pred)
                y_pred = train.torch.argmax(pred)

                print(y_pred)

                print(class_label[y_pred])

            using_time = time.time() - start_time
            print(f"using_time : {using_time}")

            if 'cat' in file and class_label[y_pred] == 'cat':
                acc_num = acc_num + 1
            elif 'dog' in file and class_label[y_pred] == 'dog':
                acc_num = acc_num + 1
            number += 1
            sub = self.test_figure.add_subplot(rows, cols, number)
            sub.set_title(file)
            sub.imshow(test_image)
            sub.set_xlabel('y_pred : ' + class_label[y_pred])
            sub.set_xticks([]), sub.set_yticks([])
            sub.text(0,100,class_label[y_pred]+':'+f'{pred[0][y_pred]:.3f}',size=15,color='red')

            self.test_canvas.draw()
            print(f"right_result : {acc_num}")
            print(f'acc : {acc_num / file_num}')