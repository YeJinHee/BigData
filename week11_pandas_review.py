import pandas as pd

df = pd.DataFrame(
    [[99, 89, 100],
        [91, 98, 90],
        [95, 97, 85],
        [83, 100, 94]],
    index=[1, 2, 3, 4],
    columns=['KOR', 'ENG', 'MAT']
)
print(df)

df = df.apply(lambda n: n+1) #얘도 1점 추가함
print(df)

# def scale_score(n): #점수 조정 1점씩 추가
#     return n + 1
#
# df = df.apply(scale_score)
# print(df)