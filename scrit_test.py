import tkinter as tk #라이브러리
 
window = tk.Tk() # Tk 객체생성
window.title('myGUI') #창 타이틀
window.geometry('300x300')#가로x세로
 
fontSize = 10 #글자 크기 변수
 
def up():    #글자 크기가 커지는 함수
  global fontSize
  fontSize += 1
  label1.config(font=('',fontSize))
 
def down():  #글자 크기가 작아지는 함수
  global fontSize
  fontSize -= 1
  label1.config(font=('',fontSize))
 
# fg=글자색, bg=배경색
btn1 = tk.Button(text='Up', font=('',10), fg='red',bg='white', command=up)
btn1.place(x=0,y=0,width=100,height=50)
 
btn2 = tk.Button(text='Down', font=('',10), fg='blue',bg='white', command=down)
btn2.place(x=0,y=50,width=100,height=50)
 
label1 = tk.Label(text='This is text.')
label1.place(x=150,y=50)
 
tk.mainloop()
#화면 X버튼 누르기전까지 종료안되게c
