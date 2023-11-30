import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
# print(titanic.info())
# print(titanic.head())

#생존자와 사망자의 나이 분표를 시각화하기
#판다스의 dropna 사용
survived_ages = titanic[titanic['survived']==1]['age'].dropna()
dead_ages = titanic[titanic['survived']==0]['age'].dropna()

plt.hist(survived_ages, bins=20, label='Survived', alpha=0.5) #투명도 추가해서 겹치는 부분도 보이게 함
plt.hist(dead_ages, bins=20, label='Dead', alpha=0.5)
plt.xlabel('Age')
plt.ylabel('Count')
plt.legend()
plt.show()

# 나이대별 생존자 수
# 데이터를 나이대로 잘라서 사용할 것이기 떄문에 판다스의 qcut 사용
# [0, 10, 20, 30, 40, 50, 60 , 70, 80]
# age_survived = titanic.groupby(pd.cut(titanic['age'], bins=range(0, 81, 10)))['survived'].sum()
# print(age_survived)

# 객실 등급별 생존자 수
# 여기서도 판다스 예제 사용 그룹바이?

#아래는 교수님 코드
#pclass_survived = titanic.groupby('pclass')['survived'].sum()

#다른 학생 코드
# pclass_survived = titanic[titanic['survived']==1].groupby(['pclass']).size()
# print(pclass_survived)


#남성과 여성의 생존률
# male_survived = titanic[(titanic['survived'] == 1) & (titanic['sex'] == 'male')]['survived'].count()
# female_survived = titanic[(titanic['survived'] == 1) & (titanic['sex'] == 'female')]['survived'].count()
# male_count = titanic[(titanic['sex'] == 'male')]['sex'].count()
# female_count = titanic[(titanic['sex'] == 'female')]['sex'].count()
# print(male_survived, male_count, female_survived, female_count)
# print(male_survived/male_count, female_survived/female_count)

# 생존자와 사망자의 수를 카운드
# 판다스 예제 사용?
# survived_human = titanic[titanic["survived"] == 1]["survived"].count() #살아있는 사람의 수 카운트
# dead_human = titanic[titanic["survived"] == 0]["survived"].count() #사망한 사람의 수 카운트
# print(f"생존자 수 : {survived_human}")
# print(f"사망자 수 : {dead_human}")
