import tkinter

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


def change7():
    print("muyaho")


button7 = tkinter.Button(window, text="무야호김상덕", command=change7)
button7.pack(side="bottom")


def change8():
    print("muyaho")


button8 = tkinter.Button(window, text="파일열기", command=change8)
button8.pack(side="bottom")

window.mainloop()

# def change_b():
# global photo2
# photo2 = tkinter.PhotoImage(file="suji.PNG")
# label2.config(image=photo2)
