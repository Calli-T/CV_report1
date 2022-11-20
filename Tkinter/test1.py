import tkinter

window = tkinter.Tk()
window.title("CV 공간 필터링")
#window.geometry("640x400+100+100")
window.geometry("860x460")
window.resizable(True, True)

image1 = tkinter.PhotoImage(file="lenna.png")
image2 = tkinter.PhotoImage(file="lenna.png")

label1 = tkinter.Label(window, image=image1)
label2 = tkinter.Label(window, image=image2)
label1.pack(side="left", padx=50)
label2.pack(side="right", padx=50)

window.mainloop()
