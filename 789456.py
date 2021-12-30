__author__="teacher"
import random
import streamlit as st
confirm_input = st.button('確認產生答案')
if confirm_input:
  c=random.randint(2,99)
  st.session_state.c = c
  st.session_state.start = 1
  st.session_state.end = 100
  
#start,end=1,100
b=st.number_input("請輸入1到100之間的整數:")
confirm_input2 = st.button('輸入確認')
if confirm_input2:
  if x==st.session_state.c:
    st.write("恭喜你中獎了")
  elif x>st.session_state.c:
    if x>=st.session_state.end:
      st.write("輸入不合法,請重新輸入:")
    else:
      st.session_state.end=x
  else:
    if x<=st.session_state.start:
      st.write("輸入不合法,請重新輸入:")
    else:
      st.session_state.start=x
