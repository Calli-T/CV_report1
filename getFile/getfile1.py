import os
from tkinter import filedialog
from tkinter import messagebox

list_file = []  # 파일 목록 담을 리스트 생성
files = filedialog.askopenfilenames(initialdir="/", \
                                    title="파일을 선택 해 주세요", \
                                    filetypes=(("*.png", "*png"), ("*.jpg", "*jpg"), ("*.jpeg", "*jpeg")))
# files 변수에 선택 파일 경로 넣기

if files == '':
    messagebox.showwarning("경고", "파일을 추가 하세요")  # 파일 선택 안했을 때 메세지 출력

print(files[0])  # files 리스트 값 출력