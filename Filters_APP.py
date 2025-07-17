import streamlit as st
import cv2
import numpy as np
from PIL import Image
st.title('Filters Application')
def black_white(img):
    gray_image = cv2.cvtcolor(img , cv2.COLOR_BGR2GRAY)
    return gray_image
def pencil_sketch(img , ksize = 5):
    blur = cv2.GaussianBlur(img , (ksize , ksize) , 0,0)
    sketch,_ = cv2.pencilSketch(blur)
    return sketch
def HDR(img , level = 50 , sigma_s = 10 , sigma_r = 0.1):
    bright = cv2.convertScaleAbs(img , beta = level)
    hd_image = cv2.detailEnhance(bright , sigma_s = sigma_s , sigma_r = sigma_r)
    return hd_image
def Brightness(img , level = 50):
    bright = cv2.convertScaleAbs(img , beta = level)
    return bright
    
def style_img(img , ksize = 5 , sigma_s = 10 , sigma_r = 0.1):
    blur = cv2.GaussianBlur(img , (ksize , ksize) , 0,0)
    style = cv2.stylization(blur , sigma_s = sigma_s , sigma_r = sigma_r)
    return style

upload = st.file_uploader('Choose an Image...', type = ['png' , 'jpg' , 'jpeg'])   
if upload is not None:
    img = Image.open(upload)
    img = np.array(img)
    original_image , output_image = st.columns(2)
    with original_image:
        st.header('Original Image:')
        st.image(img)
        st.header('Image Filters')
        options = st.selectbox('Select Filter' , ('None' , 'pencil_sketch' , 'HDR' , 'Brightness' , 'style_img'))
        if options == 'None':
            output = img
        elif options == 'black_white':
            outputI = black_white(img)
        elif options == 'pencil_sketch':
            ksize = st.slider('Kerbel Size' , 1 , 9 , 5 , step = 2)
            output = pencil_sketch(img , ksize)
        elif options == 'HDR':
            level = st.slider('level' , -100 , 100 , 0 , step = 5)
            sigma_s = st.slider('sigma_s' , 1 , 10 , 5 , step = 1)
            sigma_r = st.slider('sigma_r' , 0.0 , 1.0 , 0.1 , step = 0.1)
            output = HDR(img , level = level , sigma_s = sigma_s , sigma_r = sigma_r)
        elif options == 'Brighness':
            bright = st.slider('bright' , -100 , 100 , 0 , step = 5)
            output = bright(img , level = level)
        elif options == 'style_img':
            ksize = st.slider('ksize' , 1 , 9 , 5 , step = 2)
            sigma_s = st.slider('sigma_s' , -100 , 100  , 0 , step = 5)
            sigma_r = st.slider('sigma_r' , 0.0 , 1.0 , 0.1 , step = 0.1)
            output = style_img(img , ksize = ksize , sigma_s = sigma_s , sigma_r = sigma_r)
            with output_image:
                st.header('Output Image:')
                st.image(output)
            
       
