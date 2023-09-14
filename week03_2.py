import numpy as np
import tkinter as tk  # Built in GUI
from tkinter import messagebox  # pop-up window


# def press_enter_key(ev):
#     click_button()
#     messagebox.showinfo('x, y', f"({ev.x}, {ev.y})")


def click_button(*args): #가변매개변수 사용한 것
    try:
        r, c = map(int, en_row_column.get().split())
        matrix = np.random.randint(1, 101, size=(r, c))
        lbl_result.config(text=matrix)
    except ValueError as err:
        messagebox.showerror('Error!', f"입력 값이 없습니다.\n{err}")


window = tk.Tk()
window.title('numpy gui version v2.0')
window.geometry('300x150')

# create widget
lbl_result = tk.Label(text="random numpy 2d array")
en_row_column = tk.Entry()
#en_column = tk.Entry()
btn_click = tk.Button(text="click me!", command=click_button)

#엔터 키 바인딩
en_row_column.bind("<Return>", press_enter_key)
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