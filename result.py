from PyQt5 import QtWidgets, QtGui
from project1 import Ui_Form
from keras.models import load_model
import keras
import glob
import numpy as np
import tensorflow as tf
import sys
model = load_model('pict.h5')
folder = sorted(glob.glob("test/*.png"))
pictu = []
class_names = ["Black-grass","Charlock","Cleavers","Common Chickweed","Common wheat","Fat Hen","Loose Silky-bent","Maize","Scentless Mayweed","Shepherds Purse","Small-flowered Cranesbill","Sugar beet"]
for i in folder:
    pictu.append(i)

count = 0
class Image(QtWidgets.QMainWindow,Ui_Form):
    def __init__(self):
        super(Image,self).__init__()
        self.uif =Ui_Form()
        self.uif.setupUi(self)
        self.uif.frward.pressed.connect(self.show_pict)
        self.uif.back.pressed.connect(self.show_rpict)

    def show_pict(self):
        global count
        count = count +1

        if count ==len(pictu):
            count = 0

        tensor = tf.keras.preprocessing.image.load_img(
            pictu[count], grayscale=False, color_mode='rgb', target_size=(150, 150),
            interpolation='nearest'
        )
        input_arr = keras.preprocessing.image.img_to_array(tensor)
        tesnor_for_pred = tf.reshape(input_arr, [1, 150, 150, 3])
        res = model.predict(tesnor_for_pred)
        result = np.argmax(res)
        name = class_names[result]

        self.uif.result.setText("Model predicted: "+str(name))


        self.uif.display.setPixmap(QtGui.QPixmap(pictu[count]))


    def show_rpict(self):
        global count
        count = count - 1

        if count*(-1)==len(pictu):
            count =0

        tensor = tf.keras.preprocessing.image.load_img(
            pictu[count], grayscale=False, color_mode='rgb', target_size=(150, 150),
            interpolation='nearest'
        )
        input_arr = keras.preprocessing.image.img_to_array(tensor)
        tesnor_for_pred = tf.reshape(input_arr, [1, 150, 150, 3])
        res = model.predict(tesnor_for_pred)
        result = np.argmax(res)
        name = class_names[result]

        self.uif.result.setText("Model predicted: "+str(name))



        self.uif.display.setPixmap(QtGui.QPixmap(pictu[count]))





app = QtWidgets.QApplication(sys.argv)
img = Image()
img.show()
app.exec_()