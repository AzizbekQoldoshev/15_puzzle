from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import random


app = QApplication(sys.argv)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.lst = []
        for i in range(200):
            if len(self.lst) == 15:
                break
            a = random.randint(1, 15)
            if a in self.lst:
                continue
            else:
                self.lst.append(a)

        print(self.lst)
        self.data = {
            "button_1": {"cor_x": 50, "cor_y": 50},
            "button_2": {"cor_x": 105, "cor_y": 50},
            "button_3": {"cor_x": 160, "cor_y": 50},
            "button_4": {"cor_x": 215, "cor_y": 50},
            "button_5": {"cor_x": 50, "cor_y": 105},
            "button_6": {"cor_x": 105, "cor_y": 105},
            "button_7": {"cor_x": 160, "cor_y": 105},
            "button_8": {"cor_x": 215, "cor_y": 105},
            "button_9": {"cor_x": 50, "cor_y": 160},
            "button_10": {"cor_x": 105, "cor_y": 160},
            "button_11": {"cor_x": 160, "cor_y": 160},
            "button_12": {"cor_x": 215, "cor_y": 160},
            "button_13": {"cor_x": 50, "cor_y": 215},
            "button_14": {"cor_x": 105, "cor_y": 215},
            "button_15": {"cor_x": 160, "cor_y": 215},
            "null_button": {"cor_x": 215, "cor_y": 215},
        }

        self.start()

    def font(self, obj, x, y):
        obj.setGeometry(x, y, 50, 50)

    def start(self):
        

        self.one = QPushButton(f"{self.lst[0]}", self)
        self.font(
            self.one, self.data["button_1"]["cor_x"], self.data["button_1"]["cor_y"]
        )

        self.two = QPushButton(f"{self.lst[1]}", self)
        self.font(
            self.two, self.data["button_2"]["cor_x"], self.data["button_2"]["cor_y"]
        )

        self.three = QPushButton(f"{self.lst[2]}", self)
        self.font(
            self.three, self.data["button_3"]["cor_x"], self.data["button_3"]["cor_y"]
        )

        self.four = QPushButton(f"{self.lst[3]}", self)
        self.font(
            self.four, self.data["button_4"]["cor_x"], self.data["button_4"]["cor_y"]
        )

        self.five = QPushButton(f"{self.lst[4]}", self)
        self.font(
            self.five, self.data["button_5"]["cor_x"], self.data["button_5"]["cor_y"]
        )

        self.six = QPushButton(f"{self.lst[5]}", self)
        self.font(
            self.six, self.data["button_6"]["cor_x"], self.data["button_6"]["cor_y"]
        )

        self.seven = QPushButton(f"{self.lst[6]}", self)
        self.font(
            self.seven, self.data["button_7"]["cor_x"], self.data["button_7"]["cor_y"]
        )

        self.eight = QPushButton(f"{self.lst[7]}", self)
        self.font(
            self.eight, self.data["button_8"]["cor_x"], self.data["button_8"]["cor_y"]
        )

        self.nine = QPushButton(f"{self.lst[8]}", self)
        self.font(
            self.nine, self.data["button_9"]["cor_x"], self.data["button_9"]["cor_y"]
        )

        self.ten = QPushButton(f"{self.lst[9]}", self)
        self.font(
            self.ten, self.data["button_10"]["cor_x"], self.data["button_10"]["cor_y"]
        )

        self.eleven = QPushButton(f"{self.lst[10]}", self)
        self.font(
            self.eleven,
            self.data["button_11"]["cor_x"],
            self.data["button_11"]["cor_y"],
        )

        self.twelwe = QPushButton(f"{self.lst[11]}", self)
        self.font(
            self.twelwe,
            self.data["button_12"]["cor_x"],
            self.data["button_12"]["cor_y"],
        )

        self.threeteen = QPushButton(f"{self.lst[12]}", self)
        self.font(
            self.threeteen,
            self.data["button_13"]["cor_x"],
            self.data["button_13"]["cor_y"],
        )

        self.fourteen = QPushButton(f"{self.lst[13]}", self)
        self.font(
            self.fourteen,
            self.data["button_14"]["cor_x"],
            self.data["button_14"]["cor_y"],
        )

        self.fifteen = QPushButton(f"{self.lst[14]}", self)
        self.font(
            self.fifteen,
            self.data["button_15"]["cor_x"],
            self.data["button_15"]["cor_y"],
        )

        self.one.clicked.connect(
            lambda: self.changeButton(data=self.data["button_1"], button=1)
        )

        self.two.clicked.connect(
            lambda: self.changeButton(data=self.data["button_2"], button=2)
        )

        self.three.clicked.connect(
            lambda: self.changeButton(data=self.data["button_3"], button=3)
        )

        self.four.clicked.connect(
            lambda: self.changeButton(data=self.data["button_4"], button=4)
        )

        self.five.clicked.connect(
            lambda: self.changeButton(data=self.data["button_5"], button=5)
        )

        self.six.clicked.connect(
            lambda: self.changeButton(data=self.data["button_6"], button=6)
        )

        self.seven.clicked.connect(
            lambda: self.changeButton(data=self.data["button_7"], button=7)
        )

        self.eight.clicked.connect(
            lambda: self.changeButton(data=self.data["button_8"], button=8)
        )

        self.nine.clicked.connect(
            lambda: self.changeButton(data=self.data["button_9"], button=9)
        )

        self.ten.clicked.connect(
            lambda: self.changeButton(data=self.data["button_10"], button=10)
        )

        self.eleven.clicked.connect(
            lambda: self.changeButton(data=self.data["button_11"], button=11)
        )

        self.twelwe.clicked.connect(
            lambda: self.changeButton(data=self.data["button_12"], button=12)
        )

        self.threeteen.clicked.connect(
            lambda: self.changeButton(data=self.data["button_13"], button=13)
        )

        self.fourteen.clicked.connect(
            lambda: self.changeButton(data=self.data["button_14"], button=14)
        )

        self.fifteen.clicked.connect(
            lambda: self.changeButton(data=self.data["button_15"], button=15)
        )

    def changeButton(self, data, button):
        if (
            (data["cor_x"] != self.data["null_button"]["cor_x"] and data["cor_x"] - self.data["null_button"]["cor_x"]<=70)
            or (data["cor_y"] != self.data["null_button"]["cor_y"] and data["cor_y"] - self.data["null_button"]["cor_y"]<=70)
        ) :
            nullx = self.data["null_button"]["cor_x"]
            nully = self.data["null_button"]["cor_y"]
            x = self.data[f"button_{button}"]["cor_x"]
            y = self.data[f"button_{button}"]["cor_y"]
            self.data.update(
                {
                    "button_{}".format(button): {"cor_x": nullx, "cor_y": nully},
                    "null_button": {"cor_x": x, "cor_y": y},
                }
            )
            self.font(
                    self.aniqlash(button=button), self.data["button_{}".format(button)]["cor_x"], self.data["button_{}".format(button)]["cor_y"]
                    )
        functions=[self.one,self.two,self.three,self.four,self.five,self.six,self.seven,self.eight,self.nine,self.ten,self.eleven,self.twelwe,self.threeteen,self.fourteen,self.fifteen]
        yutuq=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        sonlar=[]
        for i in functions:
            sonlar.append(int(i.text()))
        if sonlar==yutuq:
            a=QMessageBox(self)
            a.setText("You Win!")
            a.show()
        else:
            sonlar.clear()

    def aniqlash(self,button):
        functions=[self.one,self.two,self.three,self.four,self.five,self.six,self.seven,self.eight,self.nine,self.ten,self.eleven,self.twelwe,self.threeteen,self.fourteen,self.fifteen]
        return functions[button-1]
window = Window()
window.show()
app.exec_()
