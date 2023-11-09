import pandas as pd

df1 = pd.DataFrame(
    {
        "KOR": [99, 91, 100],
        "ENG": [89, 98, 97],
        "MAT": [100, 90, 85],
    }, index=[1, 2, 3]
)
print(df1)
print(df1.sort_values('MAT')) #수학을 오름차순
df1 = df1.drop(columns=['ENG'])
print(df1)

df2 = pd.DataFrame(
    [[99, 89, 100],
        [91, 98, 90],
        [100, 97, 85],
        [83, 100, 85]],
    index=[1, 2, 3, 4],
    columns=['KOR', 'ENG', 'MAT']
)
print(df2)
#국어 수학 칼럼을 추출
#조건은 국어가 95 이상이어야 함
df2_copy = df2.loc[df2['KOR']>=95, ['KOR', 'MAT']]
print(df2_copy)
