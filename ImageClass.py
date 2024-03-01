# -*- coding: utf-8 -*-
"""
Created on Mon May 29 18:43:00 2023

@author: sinan

"""

from skimage import filters

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget , QFileDialog ,QVBoxLayout

from skimage.segmentation import (morphological_chan_vese,                                 
                                  checkerboard_level_set)
from skimage.filters import threshold_multiotsu ,roberts ,scharr ,sobel,prewitt
from skimage.color import rgb2gray ,rgb2hsv
import matplotlib.pyplot as plt
from skimage import  io 
from skimage.segmentation import chan_vese
from skimage.segmentation import checkerboard_level_set
from skimage.util import img_as_float
import numpy as np

class ImageClass():
    def __init__(self):
        self.__imagename=None
        self.__output=None
        self.output=None
        self.extentions=None
        self.outputlist=[]
        self.redolist=[]        
    def set_filename(self,image):
        self.__imagename = image
        self.__image =io.imread(self.__imagename)
    
    def set_output(self,image):
        self.__output = image

    def get_output(self):
        return self.__output

    def get_filename(self):
        return self.__imagename

    def get_image(self):
        return self.__image

    def clear_input(self):
        self.__image=""
    
    def clear_output(self):
        self.__output=""

    def clear(self):
        self.__imagename=""
    


    def rgbtogray(self):
        grayscale = rgb2gray(self.get_image())
        self.output=grayscale
        return grayscale
    
    
    def rgbtohsv(self):
        print(type(self.__image))
        hsv_img = rgb2hsv(self.__image)
        image_array = (hsv_img * 255).astype(np.uint8)
        self.output=image_array
        return hsv_img
    
    def MOThresholding(self):

        self.__image=self.__image[:,:,:3]

        grayscale = rgb2gray(self.get_image())

        thresholds = threshold_multiotsu(grayscale)

        regions = np.digitize(grayscale, bins=thresholds)

        otsu = (regions * 255).astype(np.uint8)
        self.output=otsu


        return otsu
    
    def Chan_Vese_Seg(self):
        self.__image=self.__image[:,:,:3]

        original_image=rgb2gray(self.__image)
        cv = chan_vese(original_image, mu=0.25, lambda1=1, lambda2=1, tol=1e-3,
                               max_num_iter=200, dt=0.5, init_level_set="checkerboard",
                               extended_output=True)
        self.output=cv[0]

        return cv[0]

    def Morphological(self):

        image = img_as_float(rgb2gray(self.__image))
        init_ls = checkerboard_level_set(image.shape, 6)
        rs =  morphological_chan_vese(image, num_iter=35, init_level_set=init_ls,
                             smoothing=3, lambda1=0.5, lambda2=0.5)

        self.output=rs
        return rs

    
    def Roberts(self):

        image = rgb2gray(self.__image)
        edge_roberts = roberts(image)
        self.output=edge_roberts
        return edge_roberts

    def Sobel(self):
        image = rgb2gray(self.__image)

        edge_sobel = filters.sobel(image)
        self.output=edge_sobel

        return edge_sobel

    def Scharr(self):
        image = rgb2gray(self.__image)

        edge_scharr = filters.scharr(image)
        self.output=edge_scharr

        return edge_scharr
    def Prewitt(self):
        image = rgb2gray(self.__image)
        edge_prewitt = filters.prewitt(image)
        self.output=edge_prewitt
        return edge_prewitt
def store_evolution_in(lst):


    def _store(x):
        lst.append(np.copy(x))
    
    return _store
        