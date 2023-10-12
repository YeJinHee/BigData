# import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
# from sklearn.neighbors import KNeighborsRegressor
import tglearn


def predict_life_satisfaction(*ev):
    x = int(en_GDP_per_capita.get())
    X_new = [[x]] #2차원 배열에 저장

    life_satisfaction = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")
    X = life_satisfaction[["GDP per capita (USD)"]].values  # return 2d array, GDP 값 추출 후 x에 저장
    y = life_satisfaction[["Life satisfaction"]].values  # return 2d array

    # print(X)
    # print(life_satisfaction)

    # life_satisfaction.plot(kind='scatter', grid=True, x="GDP per capita (USD)", y="Life satisfaction")
    # plt.axis([23500, 62500, 4, 9])
    # plt.show()

    model = tglearn.KNeighborsRegressor()  # default neighbor is 5, k-최근접 이웃 회귀 모델을 생성합니다.
    #model = KNeighborsRegressor(3)
    model.fit(X, y) #학습시킴

    # predict new GDP per capita (South Korea 2020)
    lbl_life_satisfaction.config(text=f"해당 국가의 삶의 만족도는 {model.predict(X_new)}로 예상합니다.")


if __name__ == "__main__":
    window = tk.Tk()
    window.title("삶의 만족도 예측 프로그램 v0.5")
    window.geometry("400x150")

    lbl_life_satisfaction = tk.Label(window, text="아래 입력상자에 삶의 만족도를 알고 싶은\n국가의 1인당 GDP값을 입력해주세요")
    en_GDP_per_capita = tk.Entry(window)
    btn_predict = tk.Button(window, text="예측", command=predict_life_satisfaction)

    lbl_life_satisfaction.pack()
    en_GDP_per_capita.pack(fill='x')
    btn_predict.pack(fill='x')

    #디자인 추가
    en_GDP_per_capita.bind("<Return>", predict_life_satisfaction)
    en_GDP_per_capita.focus()

    window.mainloop()