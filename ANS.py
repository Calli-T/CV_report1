import tkinter
import os
from tkinter import filedialog
from tkinter import messagebox
import cv2 as cv
import numpy as np
from PIL import Image, ImageTk

origin = cv.imread("Lenna.png", cv.IMREAD_COLOR)
gray = cv.imread("Lenna.png", cv.IMREAD_GRAYSCALE)
mask3 = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])

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


def mean33(before):
    after = np.copy(before)
    filter_1 = np.array([[1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9], [1 / 9, 1 / 9, 1 / 9]])

    x, y, channel = before.shape

    for i in range(1, x - 1):
        for j in range(1, y - 1):
            for c in range(3):
                after[i, j, c] = 0

                for k in [-1, 0, 1]:
                    for l in [-1, 0, 1]:
                        after[i, j, c] += filter_1[k + 1, l + 1] * before[i + k, j + l, c]

    return after


def mean55(before):
    after = np.copy(before)
    filter_2 = np.array([[0.04, 0.04, 0.04, 0.04, 0.04], [0.04, 0.04, 0.04, 0.04, 0.04], [0.04, 0.04, 0.04, 0.04, 0.04],
                         [0.04, 0.04, 0.04, 0.04, 0.04], [0.04, 0.04, 0.04, 0.04, 0.04]])

    x, y, channel = before.shape

    for i in range(2, x - 2):
        for j in range(2, y - 2):
            for c in range(3):
                after[i, j, c] = 0

                for k in [-2, -1, 0, 1, 2]:
                    for l in [-2, -1, 0, 1, 2]:
                        after[i, j, c] += filter_2[k + 2, l + 2] * before[i + k, j + l, c]

    return after


def median33(before):
    after = np.copy(before)

    x, y, channel = before.shape

    for i in range(1, x - 1):
        for j in range(1, y - 1):
            for c in range(3):
                slice = np.sort(np.array(before[i - 1:i + 2, j - 1:j + 2, c]).reshape(1, -1))
                after[i, j, c] = slice[0][4]

    return after


def median55(before):
    after = np.copy(before)

    x, y, channel = before.shape

    for i in range(2, x - 2):
        for j in range(2, y - 2):
            for c in range(3):
                slice = np.sort(np.array(before[i - 2:i + 3, j - 2:j + 3, c]).reshape(1, -1))
                after[i, j, c] = slice[0][12]

    return after


def change1():
    global next
    global origin
    filtered_mean33 = mean33(origin)
    filtered_mean33 = cv.cvtColor(filtered_mean33, cv.COLOR_RGB2BGR)
    next = ImageTk.PhotoImage(image=Image.fromarray(filtered_mean33))
    label2.config(image=next)


button1 = tkinter.Button(window, text="3*3 Mean Filter", command=change1)
button1.pack(side="top", pady=10)


def change2():
    global next
    global origin
    filtered_mean55 = mean55(origin)
    filtered_mean55 = cv.cvtColor(filtered_mean55, cv.COLOR_RGB2BGR)
    next = ImageTk.PhotoImage(image=Image.fromarray(filtered_mean55))
    label2.config(image=next)


button2 = tkinter.Button(window, text="5*5 Mean Filter", command=change2)
button2.pack(side="top", pady=10)


def change3():
    global next
    global origin
    filtered_median33 = median33(origin)
    filtered_median33 = cv.cvtColor(filtered_median33, cv.COLOR_RGB2BGR)
    next = ImageTk.PhotoImage(image=Image.fromarray(filtered_median33))
    label2.config(image=next)


button3 = tkinter.Button(window, text="3*3 Median Filter", command=change3)
button3.pack(side="top", pady=10)


def change4():
    global next
    global origin
    filtered_median55 = median55(origin)
    filtered_median55 = cv.cvtColor(filtered_median55, cv.COLOR_RGB2BGR)
    next = ImageTk.PhotoImage(image=Image.fromarray(filtered_median55))
    label2.config(image=next)


button4 = tkinter.Button(window, text="5*5 Median Filter", command=change4)
button4.pack(side="top", pady=10)


def change5():
    global next
    global gray
    laplacian_gray = cv.filter2D(gray, -1, mask3)
    next = ImageTk.PhotoImage(image=Image.fromarray(laplacian_gray))
    label2.config(image=next)


button5 = tkinter.Button(window, text="Laplacian GrayScale", command=change5)
button5.pack(side="top", pady=10)


def change6():
    global next
    global origin
    laplacian = cv.filter2D(origin, -1, mask3)
    laplacian = cv.cvtColor(laplacian, cv.COLOR_RGB2BGR)
    next = ImageTk.PhotoImage(image=Image.fromarray(laplacian))
    label2.config(image=next)


button6 = tkinter.Button(window, text="Laplacian Color", command=change6)
button6.pack(side="top", pady=10)


def change8():
    list_file = []  # 파일 목록 담을 리스트 생성
    files = filedialog.askopenfilenames(initialdir="/", \
                                        title="파일을 선택 해 주세요", \
                                        filetypes=(("*.png", "*png"), ("*.jpg", "*jpg"), ("*.jpeg", "*jpeg")))

    if files == '':
        messagebox.showwarning("경고", "파일을 추가 하세요")  # 파일 선택 안했을 때 메세지 출력

    filename = files[0]
    print(filename)

    global origin
    origin = cv.imread(filename, cv.IMREAD_COLOR)

    global gray
    gray = cv.imread(filename, cv.IMREAD_GRAYSCALE)

    global nextPhoto
    nextPhoto = tkinter.PhotoImage(file=filename)
    label1.config(image=nextPhoto)

    global nextPhoto2
    nextPhoto2 = tkinter.PhotoImage(file=filename)
    label2.config(image=nextPhoto2)


button8 = tkinter.Button(window, text="파일열기", command=change8)
button8.pack(side="bottom")

window.mainloop()

# def change_b():
# global photo2
# photo2 = tkinter.PhotoImage(file="suji.PNG")
# label2.config(image=photo2)
