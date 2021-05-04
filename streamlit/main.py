import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title('Streamlit 入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteraction{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!'

left_column,right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ内容1の回答')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ内容2の回答')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('問い合わせ内容3の回答')

# text = st.text_input('あなたの趣味を教えて下さい。')
# 'あなたの趣味は', text,'です。'
#
# condition = st.slider('あなたの今の調子は？',0,100,50)
# 'コンディション',condition


# option = st.selectbox(
#     'あなたが好きな数字を教えて下さい',
#     list(range(1,11))
# )
#
# 'あなたの好きな数字は',option,'です'
# if st.checkbox('Show Image'):
#     img = Image.open('bruce-mars-AndE50aaHn4-unsplash.jpg')
#     st.image(img, caption='test', use_column_width=True)
