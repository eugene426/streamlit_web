import streamlit as st
import numpy as np
import pandas as np
from PIL import Image

# from time import sleep

st.set_page_config(
    page_icon='🍑',
    page_title = '김유진 페이지 테스트',
    layout='wide'
)

st.header('말랑콩떡 강아지 성현이 사랑해 ❤️❤️')
st.subheader('키키키')

if st.button('여기 눌러봐 성현이'):
    image = Image.open('./IMG_6299.jpg')
    st.image(image)