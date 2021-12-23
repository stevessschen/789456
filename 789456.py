__author__="teacher"
import random
def paly():
  a=random.randint(2,99)
  start,end=1,100
  while 1:
    b=int(input("請輸入%d到%d之間的整數:"%(start,end)))
    if b==a:
      st.write("恭喜你中獎了")
      break
    elif b>a:
      if b>=end:
        st.write("輸入不合法,請重新輸入:")
      else:
        end=b
    else:
      if b<=start:
        st.write("輸入不合法,請重新輸入:")
      else:
          start=b
if __name__=='__main__':
  paly()
