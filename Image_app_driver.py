from PyQt5 import QtWidgets
import sys 
from PyQt5.QtWidgets import  QMainWindow , QFileDialog ,QMessageBox
from mainwindow_new import Ui_MainWindow
from PyQt5.QtGui import QPixmap ,QImage
from ImageClass import ImageClass
import numpy as np
from PyQt5.QtCore import Qt
from skimage import  io 
import os
class mywindow(QMainWindow):

    def __init__(self):
 
        super(mywindow, self).__init__()
 
        self.ui = Ui_MainWindow()
        self.image = ImageClass()
        self.ui.setupUi(self)
        
        self.ui.file.clicked.connect(lambda :self.openfile())
        self.ui.clear_button.clicked.connect(lambda :self.clearOutput())
        self.ui.clear.clicked.connect(lambda :self.clearSource())
        self.ui.export_as.clicked.connect(lambda :self.exportAsSource())
        self.ui.rgb2gray_button.clicked.connect(lambda :self.RGB2GRAY())
        self.ui.rgb2hsv_button.clicked.connect(lambda :self.RGB2HSV())
        self.ui.mothres_button.clicked.connect(lambda :self.MOThresholding())
        self.ui.cvsegmen_button.clicked.connect(lambda :self.CVSegmentation())
        self.ui.morphosnake_button.clicked.connect(lambda :self.MorphoSnake())
        self.ui.roberts.clicked.connect(lambda :self.Roberts())
        self.ui.sobel.clicked.connect(lambda :self.Sobel())
        self.ui.scharr.clicked.connect(lambda :self.Scharr())
        self.ui.prewitt.clicked.connect(lambda :self.Prewitt())
        self.ui.save_button.clicked.connect(lambda :self.save())
        self.ui.save_as_button.clicked.connect(lambda :self.save_as())
        self.ui.export_as_button.clicked.connect(lambda :self.exportAsOutput())
        self.ui.undo_button.clicked.connect(lambda :self.undo())
        self.ui.redo_button.clicked.connect(lambda :self.redo())
        
        self.ui.actionOpen_Source.triggered.connect(lambda :self.openfile())
        self.ui.actionSave_Output.triggered.connect(lambda :self.save())
        self.ui.actionSave_As_Output.triggered.connect(lambda :self.save_as())
        self.ui.actionExit_2.triggered.connect(lambda :self.exit())

        self.ui.actionSource.triggered.connect(lambda :self.exportAsSource())
        self.ui.actionOutput.triggered.connect(lambda :self.exportAsOutput())

        self.ui.actionSource_2.triggered.connect(lambda :self.clearSource())
        self.ui.actionOutput_2.triggered.connect(lambda :self.clearOutput())

        self.ui.actionUndo_Output.triggered.connect(lambda :self.undo())
        self.ui.actionRdeo_Output.triggered.connect(lambda :self.redo())

        self.ui.actionRGB_to_Grayscale.triggered.connect(lambda :self.RGB2GRAY())
        self.ui.actionRGB_to_HSV.triggered.connect(lambda :self.RGB2HSV())

        self.ui.actionMulti_Otsu_Thresholding.triggered.connect(lambda :self.MOThresholding())
        self.ui.actionChan_Vese_Segmentation.triggered.connect(lambda :self.CVSegmentation())
        self.ui.actionMorphological_Snakes.triggered.connect(lambda :self.MorphoSnake())

        self.ui.actionRoberts.triggered.connect(lambda :self.Roberts())
        self.ui.actionSobel.triggered.connect(lambda :self.Sobel())
        self.ui.actionScharr.triggered.connect(lambda :self.Scharr())
        self.ui.actionPrewitt.triggered.connect(lambda :self.Prewitt())
        
        self.make_buttons_dis()

    def closeEvent(self, event):
    
        self.ui.statusbar.showMessage('Close Event')

        reply = QMessageBox.warning(self,'Message',
                "Are you sure to quit?",QMessageBox.Yes |
                QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            self.ui.statusbar.clearMessage()
            
    def make_buttons_dis(self):
        self.ui.clear_button.setDisabled(True)
        self.ui.clear.setDisabled(True)
        self.ui.export_as.setDisabled(True)
        self.ui.rgb2gray_button.setDisabled(True)
        self.ui.rgb2hsv_button.setDisabled(True)
        self.ui.mothres_button.setDisabled(True)
        self.ui.cvsegmen_button.setDisabled(True)
        self.ui.morphosnake_button.setDisabled(True)
        self.ui.roberts.setDisabled(True)
        self.ui.sobel.setDisabled(True)
        self.ui.scharr.setDisabled(True)
        self.ui.prewitt.setDisabled(True)
        self.ui.save_button.setDisabled(True)
        self.ui.save_as_button.setDisabled(True)
        self.ui.export_as_button.setDisabled(True)
        self.ui.undo_button.setDisabled(True)
        self.ui.redo_button.setDisabled(True)

        self.ui.actionSave_Output.setDisabled(True)
        self.ui.actionSave_As_Output.setDisabled(True)
        self.ui.actionExit_2.setDisabled(True)

        self.ui.actionSource.setDisabled(True)
        self.ui.actionOutput.setDisabled(True)

        self.ui.actionSource_2.setDisabled(True)
        self.ui.actionOutput_2.setDisabled(True)

        self.ui.actionUndo_Output.setDisabled(True)
        self.ui.actionRdeo_Output.setDisabled(True)

        self.ui.actionRGB_to_Grayscale.setDisabled(True)
        self.ui.actionRGB_to_HSV.setDisabled(True)

        self.ui.actionMulti_Otsu_Thresholding.setDisabled(True)
        self.ui.actionChan_Vese_Segmentation.setDisabled(True)
        self.ui.actionMorphological_Snakes.setDisabled(True)

        self.ui.actionRoberts.setDisabled(True)
        self.ui.actionSobel.setDisabled(True)
        self.ui.actionScharr.setDisabled(True)
        self.ui.actionPrewitt.setDisabled(True)

    def make_buttons_enb(self):
        self.ui.clear_button.setEnabled(True)
        self.ui.clear.setEnabled(True)
        self.ui.export_as.setEnabled(True)
        self.ui.rgb2gray_button.setEnabled(True)
        self.ui.rgb2hsv_button.setEnabled(True)
        self.ui.mothres_button.setEnabled(True)
        self.ui.cvsegmen_button.setEnabled(True)
        self.ui.morphosnake_button.setEnabled(True)
        self.ui.roberts.setEnabled(True)
        self.ui.sobel.setEnabled(True)
        self.ui.scharr.setEnabled(True)
        self.ui.prewitt.setEnabled(True)
        self.ui.save_button.setEnabled(True)
        self.ui.save_as_button.setEnabled(True)
        self.ui.export_as_button.setEnabled(True)
        self.ui.undo_button.setEnabled(True)
        self.ui.redo_button.setEnabled(True)
        self.ui.actionSave_Output.setEnabled(True)
        self.ui.actionSave_As_Output.setEnabled(True)
        self.ui.actionExit_2.setEnabled(True)

        self.ui.actionSource.setEnabled(True)
        self.ui.actionOutput.setEnabled(True)

        self.ui.actionSource_2.setEnabled(True)
        self.ui.actionOutput_2.setEnabled(True)

        self.ui.actionUndo_Output.setEnabled(True)
        self.ui.actionRdeo_Output.setEnabled(True)

        self.ui.actionRGB_to_Grayscale.setEnabled(True)
        self.ui.actionRGB_to_HSV.setEnabled(True)

        self.ui.actionMulti_Otsu_Thresholding.setEnabled(True)
        self.ui.actionChan_Vese_Segmentation.setEnabled(True)
        self.ui.actionMorphological_Snakes.setEnabled(True)

        self.ui.actionRoberts.setEnabled(True)
        self.ui.actionSobel.setEnabled(True)
        self.ui.actionScharr.setEnabled(True)
        self.ui.actionPrewitt.setEnabled(True)
    
        
    def clear(self):
        self.image.clear_input()
        self.image.clear_output()
        self.ui.label.clear()
        self.ui.label_2.clear()
        self.make_buttons_dis()
        
    def clearSource(self):
        self.image.clear_input()
        self.ui.label.clear()
        self.make_buttons_dis()
        self.image.clear_output()
        self.ui.label_2.clear()
        self.make_buttons_dis()

    def clearOutput(self):
        self.image.clear_output()
        self.ui.label_2.clear()
     

    def undo(self):
        if self.image.outputlist:
            temp=self.image.outputlist.pop()
            self.image.redolist.append(temp)
            
            if self.image.outputlist:
                output=self.image.outputlist[-1]
                print(output)
                self.ui.redo_button.setEnabled(True)
                self.ui.label_2.setPixmap(output)
            else:
                self.ui.label_2.clear()
            print("butona undo")
        else :
            self.ui.undo_button.setDisabled(True)
    def redo(self):
        if self.image.redolist:
            temp=self.image.redolist.pop()
            self.image.outputlist.append(temp)
            if self.image.redolist:
                output=self.image.redolist[-1]
                print(output)
                self.ui.undo_button.setEnabled(True)
                self.ui.label_2.setPixmap(output)
            else:
                 self.ui.redo_button.setDisabled(True)
        else:
             self.ui.redo_button.setDisabled(True)
       

    def RGB2GRAY(self):
        try:
            result = self.image.rgbtogray()
            if result is not None:
                image_array = (result * 255).astype(np.uint8)
                height, width = image_array.shape
                self.image.set_output(result)
                image = QImage(image_array.data, width, height, width, QImage.Format.Format_Grayscale8)
                pixmap = QPixmap.fromImage(image).scaled(self.ui.label_2.size(), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding)
                self.image.outputlist.append(pixmap)
                self.ui.label_2.setPixmap(pixmap)
        except Exception as e:
            print("Hata oluştu:", e)  # veya istediğiniz başka bir işlemi yapabilirsiniz
            
    def exportAsSource(self):
        if self.extensions == ".jpg":
            import_as_extension =".png"
        else:
            import_as_extension = ".jpg"

        save_path,_ = QFileDialog.getSaveFileName(self.ui.centralwidget,"Save Output","","Image Files (*{})".format(import_as_extension))
        if save_path:
            io.imsave(save_path, self.image.get_image())
        

        print("exportAsSource")

    def exportAsOutput(self):
        if self.extensions == ".jpg":
            import_as_extension =".png"
        else:
            import_as_extension = ".jpg"

        save_path,_ = QFileDialog.getSaveFileName(self.ui.centralwidget,"Save Output","","Image Files (*{})".format(import_as_extension))
        if save_path:
            io.imsave(save_path,  self.image.output)
        print("export_as")

        print("exportAsresult")

    def exit(self):
        self.close()
        print("exit")

    def RGB2HSV(self):
        try:
            result = self.image.rgbtohsv()
            if result is not None:
                image_array = (result * 255).astype(np.uint8)
                image = QImage(image_array, image_array.shape[1], image_array.shape[0], image_array.shape[1] * 3, QImage.Format.Format_RGB888)
                pixmap = QPixmap.fromImage(image).scaled(self.ui.label_2.size(), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding)
                self.image.outputlist.append(pixmap)
                self.ui.label_2.setPixmap(pixmap)
                print("butona RGB2HSV")
        except Exception as e:
            print("Hata oluştu:", e)  # veya istediğiniz başka bir işlemi yapabilirsiniz
            
    def MOThresholding(self):   
        otsu=self.image.MOThresholding()
        qimage = QImage(otsu.data, otsu.shape[1], otsu.shape[0], otsu.shape[1] , QImage.Format_Grayscale8)
        result = QPixmap.fromImage(qimage)
        self.image.outputlist.append(result)
        self.ui.label_2.setPixmap(result)

    def CVSegmentation(self):
        result=self.image.Chan_Vese_Seg()
        image_array = (result * 255).astype(np.uint8)
        height, width = image_array.shape
        image = QImage(image_array.data, width, height, width, QImage.Format.Format_Grayscale8)
        pixmap = QPixmap.fromImage(image).scaled(self.ui.label_2.size(), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.image.outputlist.append(pixmap)
        self.ui.label_2.setPixmap(pixmap)
        print("butona CVSegmentation")
    def MorphoSnake(self):
        result=self.image.Morphological()
        image_array = (result * 255).astype(np.uint8)
        height, width = image_array.shape
        image = QImage(image_array.data, width, height, width, QImage.Format.Format_Grayscale8)
        pixmap = QPixmap.fromImage(image).scaled(self.ui.label_2.size(), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.image.outputlist.append(pixmap)
        self.ui.label_2.setPixmap(pixmap)

        print("butona MorphoSnake")

    def Roberts(self):
        result =self.image.Roberts()
        print(type(result))
        image_array = (result * 255).astype(np.uint8)
        height, width = image_array.shape
        image = QImage(image_array.data, width, height, width, QImage.Format.Format_Grayscale8)
        pixmap = QPixmap.fromImage(image).scaled(self.ui.label_2.size(), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.image.outputlist.append(pixmap)
        self.ui.label_2.setPixmap(pixmap)
    def Sobel(self):
        result =self.image.Sobel()
        print(type(result))
        image_array = (result * 255).astype(np.uint8)
        height, width = image_array.shape
        image = QImage(image_array.data, width, height, width, QImage.Format.Format_Grayscale8)
        pixmap = QPixmap.fromImage(image).scaled(self.ui.label_2.size(), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.image.outputlist.append(pixmap)

        self.ui.label_2.setPixmap(pixmap)
    def Scharr(self):
        result =self.image.Scharr()
        print(type(result))
        image_array = (result * 255).astype(np.uint8)
        height, width = image_array.shape
        image = QImage(image_array.data, width, height, width, QImage.Format.Format_Grayscale8)
        pixmap = QPixmap.fromImage(image).scaled(self.ui.label_2.size(), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.image.outputlist.append(pixmap)

        self.ui.label_2.setPixmap(pixmap)
    def Prewitt(self):
        result =self.image.Prewitt()
        print(type(result))
        image_array = (result * 255).astype(np.uint8)
        height, width = image_array.shape
        image = QImage(image_array.data, width, height, width, QImage.Format.Format_Grayscale8)
        pixmap = QPixmap.fromImage(image).scaled(self.ui.label_2.size(), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.image.outputlist.append(pixmap)

        self.ui.label_2.setPixmap(pixmap)
        print("prewitt")
    def save_as(self):
        save_path, _= QFileDialog.getSaveFileName(self.ui.centralwidget,"Save Output","","Image Files (*{})".format(self.extensions))
        if save_path:
            io.imsave(save_path, self.image.output)
        print("save_as")
    def save(self):
        io.imsave(self.image.get_filename(), self.image.output)
        print("save")
 
    


        
    def openfile(self):
        try:
            filename = QFileDialog().getOpenFileName(self, "Open File", "C:/Users", "Image Files (*.png *.jpg)")
            split_tup = os.path.splitext(filename[0])
            self.extensions = split_tup[-1]
            #print("filename to qfile",filename[0])
            self.image.set_filename(filename[0])
            #print("image type :",type(self.image.get_filename()))
            pixmap = QPixmap(self.image.get_filename()).scaled(self.ui.label.size(), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding)
            print("pixmap type:",type(pixmap))
            self.make_buttons_enb()      
            self.ui.label.setPixmap(pixmap)
        except:
            filename =""
            self.ui.label.clear()
        #self.ui.label.resize(pixmap.width(), pixmap.height())



   


            
app = QtWidgets.QApplication([])

application = mywindow()
 
application.show()
 
sys.exit(app.exec())
