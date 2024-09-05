import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QThread,pyqtSignal
from PIL import Image
import cv2
import train
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure



# UI 파일 연결
# 단, UI 파일은 Python 코드 파일과 같은 디렉토리에 위치해야 한다.
form_class = uic.loadUiType("untitled.ui")[0]


# Thread 클래스
class TrainThread(QThread):
    progress = pyqtSignal(str)  # Progress signal to update the GUI
    
    def __init__(self, args,window):
        super().__init__()
        self.args = args
        self.window=window
        self._running=True

    def run(self):
        original_stdout = sys.stdout  # 원래의 표준 출력(터미널)을 저장
        # 표준 출력을 OutputCapture로 리다이렉트하여 터미널 출력을 캡처
        sys.stdout = OutputCapture(self.progress) 
        # 학습 작업 시작
        train.main(self.window, self.args)
        # 학습 작업이 끝나면 표준 출력을 원래대로 복구
        sys.stdout = original_stdout
        
    
# 터미널 출력을 캡처하고 pyqt 시그널로 전송하는 클래스
class OutputCapture:
    def __init__(self, signal):
        self.signal = signal

    def write(self, text):
        # 공백이 아닌 경우에만 시그널로 전송
        if text.strip():  
            self.signal.emit(text)

    def flush(self):
        pass
    
# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QTabWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # QLabel에서 텍스트가 길어지면 자동으로 줄바꿈
        self.file_dirShow.setWordWrap(True)
    
        # dataset directory 버튼 클릭시 openFileDialog 메서드를 호출
        self.data_directory.clicked.connect(self.openFolderDialog)
        # output directory 버튼 클릭시 openFileDialog 메서드를 호출
        self.out_directory.clicked.connect(self.openFolderDialog_result)
        # 모델학습 버튼 클릭시 run_command 메서드 호출
        self.model_teach.clicked.connect(self.run_command)
        self.model_teach_exit.clicked.connect(self.for_key)
        
        self.key=False
        
        # 그래프
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        acc_widget = self.findChild(QWidget, 'accuarcy')
        layout = QVBoxLayout(acc_widget)
        layout.addWidget(self.canvas)
        
        self.ax1 = self.figure.add_subplot(2, 1, 1)
        self.ax2 = self.figure.add_subplot(2, 1, 2)
        
        self.ax1.set_title('Loss')
        self.ax1.set_xlim(0, 50)  # x축 범위 설정
        self.ax1.set_ylim(0, 1)   # y축 범위 설정

        self.ax2.set_title('Accuracy')
        self.ax2.set_xlim(0, 50)  # x축 범위 설정
        self.ax2.set_ylim(0, 1)   # y축 범위 설정
    


    def run_shell_command(self):
        self.shell.clear()  # 텍스트 위젯을 비웁니다.
        self.worker.start()    # 스레드를 시작하여 명령어를 실행합니다.

    def display_output(self,text):
        self.shell.append(text)  # 터미널 출력을 텍스트 위젯에 추가합니다.
        
    # 그래프 그리기
    def plot(self,x_arr,to_numpy_valid,to_numpy_train):
        self.figure.clear()
        
        # Create subplots
        self.ax1 = self.figure.add_subplot(2, 1, 1)
        self.ax1.plot(x_arr, to_numpy_train[0], '-', label='Train loss',marker='o')
        self.ax1.plot(x_arr, to_numpy_valid[0], '--', label='Valid loss',marker='o')
        handles, labels = self.ax1.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        self.ax1.legend(by_label.values(), by_label.keys())
        
        self.ax2 = self.figure.add_subplot(2, 1, 2)
        self.ax2.plot(x_arr, to_numpy_train[1], '-', label='Train acc',marker='o')
        self.ax2.plot(x_arr, to_numpy_valid[1], '--', label='Valid acc',marker='o')
        handles, labels = self.ax2.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        self.ax2.legend(by_label.values(), by_label.keys())
        
        self.ax1.set_title('Loss')
        self.ax2.set_title('Accuracy')
        # canvas 그리기
        self.canvas.draw()
    
    def for_key(self):
        self.key=True
    
    def stop_training(self):
        if hasattr(self, 'thread') and self.thread.isRunning() and self.key:
            return False
        return True
        
    def openFolderDialog(self):
        # 파일 다이얼로그를 열어 사용자가 파일을 선택하도록 함
        self.folder_path = QFileDialog.getExistingDirectory(self, "폴더 선택", "")
        # 선택된 파일 처리 if문
        if self.folder_path:
            # 선택된 파일 경로를 QLabel에 표시
            self.file_dirShow.setText(f"select folder path : {self.folder_path}")
        else:
            self.file_dirShow.setText("select folder path : not select")
            
    def openFolderDialog_result(self):
        # 파일 다이얼로그를 열어 사용자가 파일을 선택하도록 함
        self.resultfolder_path = QFileDialog.getExistingDirectory(self, "choice folder", "")
        self.file_dirShow.setText(f"input: {self.folder_path}\noutput: {self.resultfolder_path}")
    def run_command(self):
        
        # 실행할 명령어 정의
        self.key=False
        # 에포크
        self.epochs_spinBox = self.findChild(QSpinBox, 'epochs_spinBox') 
        epoch=self.epochs_spinBox.value()
        # -j
        self.worker_spinBox = self.findChild(QSpinBox, 'worker_spinBox') 
        worker=self.worker_spinBox.value()
        # learning rate
        self.lr_spinBox = self.findChild(QDoubleSpinBox, 'lr_spinBox') 
        lr=self.lr_spinBox.value()
        # model
        self.model_comboBox = self.findChild(QComboBox, 'model_comboBox') 
        model=self.model_comboBox.currentText()
        # weight
        self.weight_comboBox = self.findChild(QComboBox, 'weight_comboBox') 
        weight=self.weight_comboBox.currentText()
        # device
        self.device_comboBox = self.findChild(QComboBox, 'device_comboBox') 
        device=self.device_comboBox.currentText()
        
        if(self.resultfolder_path!="" and self.folder_path!=""):
            args = train.get_args_parser(self.folder_path,epoch,worker,lr,model,weight,device,self.resultfolder_path)
            self.thread = TrainThread(args, self)
            self.thread.progress.connect(self.display_output)  # TrainThread의 출력을 GUI에 연결
            self.thread.start() 
            # self.thread.start()
        

class Test_Thread(QThread):
    test_progress = pyqtSignal(str)
    finished = pyqtSignal(Figure)
    def __init__(self,model_path,test_folder_path):
        super().__init__()
        self.model_path = model_path
        self.test_folder_path = test_folder_path
    def run(self):
        class_label = ['cat', 'dog']
        # load pth model
        model = train.torch.load(self.model_path)
        # set model to inference mode
        model.eval()
        #print(model)
        test_image_name = self.test_folder_path
        #test_image_name = 'dog.jpg'
        # check test image
        test_image = Image.open(test_image_name)
        # apply transform to test image
        transform = train.torchvision.transforms.Compose([      
                train.torchvision.transforms.Resize(256),     
                train.torchvision.transforms.CenterCrop(224), 
                train.torchvision.transforms.ToTensor(),        
                train.torchvision.transforms.Normalize(        
                mean=[0.485, 0.456, 0.406], 
                std=[0.229, 0.224, 0.225])
        ])
        img = transform(test_image)
        #print(img.shape)
        #plt.figure(figsize=(5,5))  
        #plt.imshow(img.permute(1, 2, 0))
        #plt.show()
        with train.torch.no_grad():
        
                pred = model(img.unsqueeze(0))
                print(pred)
                y_pred = train.torch.argmax(pred)
                print(y_pred)
                #print(class_label[y_pred])
        output_text = f"Prediction: {class_label[y_pred]} with probability {pred[0][y_pred]:.4f}\n"
        self.test_progress.emit(output_text)
        
        # Create and prepare the figure for plotting
        figure = Figure()
        ax = figure.add_subplot(111)
        ax.imshow(test_image)
        ax.set_title(f'Prediction: {class_label[y_pred]}')
        ax.set_xticks([])
        ax.set_yticks([])
        self.finished.emit(figure)
        

class Test_OutputCapture:

    def __init__(self, signal):
        super().__init__()
        self.output_signal = signal

    def write(self, text):
        if text.strip():  # 빈 줄을 무시할 수 있습니다.
            self.output_signal.emit(text)

    def flush(self):
        # flush 메서드는 스트림 인터페이스에서 필요하지만, 이 구현에서는 아무 동작도 하지 않습니다.
        pass
            
class Test(WindowClass):
    
    def __init__(self):
        super().__init__()
        self.model_directory.clicked.connect(lambda:self.test_openFolderDialog("model_path"))
        self.test_directory.clicked.connect(lambda:self.test_openFolderDialog("test_folder_path"))
        self.training.clicked.connect(self.start_training)

    def display_output(self,text):
        self.shell_2.append(text)  # 터미널 출력을 텍스트 위젯에 추가합니다.
    def test_openFolderDialog(self,path_type):
        # 파일 다이얼로그를 열어 사용자가 파일을 선택하도록 함
        # file_path = QFileDialog.getExistingDirectory(self, "폴더 선택", "")
        file_path, _ = QFileDialog.getOpenFileName(self, "파일 선택", "", "All Files (*);;Image Files (*.png *.jpg *.bmp)")
        if file_path:
            if path_type == "test_folder_path":
                self.test_folder_path = file_path
                self.file_dirShow2.setText(f"Select Test File path: {self.test_folder_path}")
            elif path_type == "model_path":
                self.model_path = file_path
                self.file_dirShow2.setText(f"Select Model File path: {self.model_path}")
        else:
            self.file_dirShow2.setText("File not selected")
    def start_training(self):
        if hasattr(self, 'model_path') and hasattr(self, 'test_folder_path'):
            self.thread = Test_Thread(self.model_path, self.test_folder_path)
            self.thread.test_progress.connect(self.display_output)
            self.thread.finished.connect(self.update_graph)
            self.thread.start()

    def update_graph(self, figure):
        self.test_figure = figure
        self.test_canvas = FigureCanvas(self.test_figure)
        test_widget = self.findChild(QWidget, 'train_image')
        layout = QVBoxLayout(test_widget)
        layout.addWidget(self.test_canvas)
        self.test_canvas.draw()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow2=Test()
    # 프로그램 화면을 보여주는 코드
    myWindow2.show()
    # 프로그램을 이벤트 루프로 진입시키는(프로그램을 작동시키는) 코드
    sys.exit(app.exec_())