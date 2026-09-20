import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="Image Processing App", page_icon=":camera:", layout="wide")
st.title("📸 Image Processing App")
st.write("Завантажте зображення та оберіть обробку, яку ви хочете застосувати!") 
st.sidebar.title("Налаштування обробки зображень")

uploaded_file = st.sidebar.file_uploader("Оберіть зображення", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    img_array = np.array(img)
    col1, col2 = st.columns(2)

    with  col1:
        st.header("Оригінальне зображення")
        st.image(img_array, use_container_width=True)
    filter_option = st.sidebar.selectbox("Оберіть обробку", ["Оригінал", "Чорно-білий", "Розмиття", "Ефект олівця", "Збільшити яскравість", "Контраст", "Інверсія кольорів"])

    processed_img = img_array.copy()
    if filter_option == "Чорно-білий":
            gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
            processed_img = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)  
    if filter_option == "Збільшити яскравість":
            processed_img = cv2.convertScaleAbs(img_array, alpha=1.0, beta=50)
    if filter_option == "Розмиття":
            processed_img = cv2.GaussianBlur(img_array, (15, 15), 0)
    if filter_option == "Ефект олівця":
            gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
            inverted_gray = 255 - gray
            blurred = cv2.GaussianBlur(inverted_gray, (21, 21), 0)
            inverted_blurred = 255 - blurred
            processed_img = cv2.divide(gray, inverted_blurred, scale=256.0)
            processed_img = cv2.cvtColor(processed_img, cv2.COLOR_GRAY2BGR)
    if filter_option == "Контраст":
            processed_img = cv2.convertScaleAbs(img_array, alpha=1.7, beta=0)
    if filter_option == "Інверсія кольорів":
            processed_img = cv2.bitwise_not(img_array)

    with col2:
        st.subheader("Оброблене зображення")
        st.image(processed_img, use_container_width=True)
