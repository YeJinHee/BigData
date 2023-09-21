# import matplotlib.pyplot as plt
import pandas as pd #pandas는 데이터 처리를 위한 모듈
import tkinter as tk #tkinter를 이용하여 GUI를 생성
from sklearn.linear_model import LinearRegression #선형 회귀 모델을 사용하기 위한 모듈.


def predict_life_satisfaction():
#함수를 정의
#사용자가 입력한 1인당 GDP 값을 받아옴
#데이터를 불러와서 삶의 만족도와 1인당 GDP 값을 추출
#선형 회귀 모델을 생성하고 데이터를 학습
#사용자가 입력한 GDP 값을 사용하여 삶의 만족도를 예측하고 예측 결과를 화면에 출력
    x = int(en_GDP_per_capita.get())
    X_new = [[x]]

    life_satisfaction = pd.read_csv("https://github.com/ageron/data/raw/main/lifesat/lifesat.csv")
    X = life_satisfaction[["GDP per capita (USD)"]].values  # return 2d array
    y = life_satisfaction[["Life satisfaction"]].values  # return 2d array

    # life_satisfaction.plot(kind='scatter', grid=True, x="GDP per capita (USD)", y="Life satisfaction")
    # plt.axis([23500, 62500, 4, 9])
    # plt.show()

    model = LinearRegression()
    model.fit(X, y)

    # predict new GDP per capita (South Korea 2020)
    lbl_life_satisfaction.config(text=f"해당 국가의 삶의 만족도는 {model.predict(X_new)}로 예상합니다.")


if __name__ == "__main__":
#블록에서 프로그램을 실행함
#Tkinter를 사용하여 GUI 창을 생성함
#레이블, 입력 상자, 예측 버튼을 생성하고 창에 배치함
#사용자가 입력 상자에 1인당 GDP 값을 입력하고 예측 버튼을 누를 때 predict_life_satisfaction 함수가 호출

    window = tk.Tk()
    window.title("삶의 만족도 예측 프로그램 v0.1")
    window.geometry("400x150")

    lbl_life_satisfaction = tk.Label(window, text="아래 입력상자에 삶의 만족도를 알고 싶은\n국가의 1인당 GDP값을 입력해주세요")
    en_GDP_per_capita = tk.Entry(window)
    btn_predict = tk.Button(window, text="예측", command=predict_life_satisfaction)

    lbl_life_satisfaction.pack()
    en_GDP_per_capita.pack(fill='x')
    btn_predict.pack(fill='x')

    window.mainloop() #Tkinter 창을 실행하고 이벤트 루프를 시작. 이 루프는 사용자 입력 및 버튼 클릭과 같은 이벤트를 처리