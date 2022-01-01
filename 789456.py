__author__="teacher"
import random
import streamlit as st
confirm_input = st.button('確認產生答案')
if confirm_input:
  start = st.session_state.start = 1
  c = st.session_state.c = random.randint(2,99)
  end = st.session_state.end = 100
  st.session_state.start,st.session_state.end = 1,100
  st.write('c=', st.session_state.c)

x=st.number_input("請輸入%g到%g之間的整數:"%(1,100))
confirm_input2 = st.button('輸入確認')
if confirm_input2:
  if x==st.session_state.c:
    st.write("恭喜你中獎了")
elif x>st.session_state.c:
  if x>=100:
    st.write("輸入不合法,請重新輸入:")
  else:
    100=x
else:
  if x<=1:
    st.write("輸入不合法,請重新輸入:")
  else:
    1=x
