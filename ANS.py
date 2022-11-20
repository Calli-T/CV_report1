import tkinter
import os
from tkinter import filedialog
from tkinter import messagebox

window = tkinter.Tk()
window.title("CV 공간 필터링")
# window.geometry("640x400+100+100")
window.geometry("860x460")
window.resizable(True, True)

image1 = tkinter.PhotoImage(file="lenna.png")
image2 = tkinter.PhotoImage(file="lenna.png")

label1 = tkinter.Label(window, image=image1)
label2 = tkinter.Label(window, image=image2)
label1.pack(side="left")
label2.pack(side="right")

def change1():
    print("muyaho")


button1 = tkinter.Button(window, text="무야호김상덕", command=change1)
button1.pack(side="top", pady=10)


def change2():
    print("muyaho")


button2 = tkinter.Button(window, text="무야호김상덕", command=change2)
button2.pack(side="top", pady=10)


def change3():
    print("muyaho")


button3 = tkinter.Button(window, text="무야호김상덕", command=change3)
button3.pack(side="top", pady=10)


def change4():
    print("muyaho")


button4 = tkinter.Button(window, text="무야호김상덕", command=change4)
button4.pack(side="top", pady=10)


def change5():
    print("muyaho")


button5 = tkinter.Button(window, text="무야호김상덕", command=change5)
button5.pack(side="top", pady=10)


def change6():
    print("muyaho")


button6 = tkinter.Button(window, text="무야호김상덕", command=change6)
button6.pack(side="top", pady=10)




def change8():
    list_file = []  # 파일 목록 담을 리스트 생성
    files = filedialog.askopenfilenames(initialdir="/", \
                                        title="파일을 선택 해 주세요", \
                                        filetypes=(("*.png", "*png"), ("*.jpg", "*jpg"), ("*.jpeg", "*jpeg")))

    if files == '':
        messagebox.showwarning("경고", "파일을 추가 하세요")  # 파일 선택 안했을 때 메세지 출력

    filename = files[0]

    global photo1
    photo1 = tkinter.PhotoImage(file=filename)
    label1.config(image=photo1)


button8 = tkinter.Button(window, text="파일열기", command=change8)
button8.pack(side="bottom")

window.mainloop()

# def change_b():
# global photo2
# photo2 = tkinter.PhotoImage(file="suji.PNG")
# label2.config(image=photo2)
