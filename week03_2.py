import numpy as np
import tkinter as tk  # Built in GUI
from tkinter import messagebox  # pop-up window


def create_2d_array(row, col):
    return np.random.randint(1, 101, size=(row, col))


def click_button(event): #event라고 추가적으로 해 줘야 엔터 먹음
    try:
        r, c = map(int, en_row_column.get().split())  # spacebar
        matrix = create_2d_array(r, c)
        lbl_result.config(text=matrix)
    except ValueError as err:
        #lbl_result.config(text=f"입력 값이 없습니다.\n{err}")
        messagebox.showerror('Error!', f"입력 값이 없습니다.\n{err}")


window = tk.Tk()
window.title('numpy gui version v1.5')
window.geometry('300x150')

# create widget
lbl_result = tk.Label(text="random numpy 2d array")
en_row_column = tk.Entry()
#en_column = tk.Entry()
btn_click = tk.Button(text="click me!", command=click_button)

#엔터 키 바인딩
en_row_column.bind("<Return>", click_button)
#btn_click.bind가 안 되는 이유 : 버튼 클릭 쪽이어서?

# widget layout
# lbl_result.grid(row=0, column=0, columnspan=2)
# en_row.grid(row=1, column=0)
# en_column.grid(row=1, column=1)
# btn_click.grid(row=2, column=0, columnspan=2, sticky=tk.EW)
lbl_result.pack()
en_row_column.pack(fill='x')
btn_click.pack(fill='x')

window.mainloop()