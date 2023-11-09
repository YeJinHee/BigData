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
#df2_copy = df2.iloc[:, [0, 2]] #국어 수학만 출력
#df2_copy = df2.loc[:, ['KOR', 'MAT']] #얘도 똑같음
#df2_copy = df2.loc[:, 'KOR': 'MAT'] #영어 안 지워짐
df2_copy = df2.loc[:, 'KOR': 'MAT' :2] #지워짐
print(df2_copy)


df2 = (pd.melt(df2)
       .rename(columns={
        'variable': 'subject',
        'value': 'score'})
       .query('score >= 90')
       .sort_values('score', ascending=False) #내림차순
       )

print(df2)
print(df2.iloc[:, [1]]) #전체에서 1행만 출력
