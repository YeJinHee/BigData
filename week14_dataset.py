import seaborn as sns

titanic = sns.load_dataset('titanic')
# print(titanic.info())
# print(titanic.head())

#남성과 여성의 생존률
male_survived = titanic[(titanic['survived'] == 1) & (titanic['sex'] == 'male')]['survived'].count()
female_survived = titanic[(titanic['survived'] == 1) & (titanic['sex'] == 'female')]['survived'].count()
male_count = titanic[(titanic['sex'] == 'male')]['sex'].count()
female_count = titanic[(titanic['sex'] == 'female')]['sex'].count()
print(male_survived, male_count, female_survived, female_count)
print(male_survived/male_count, female_survived/female_count)

#생존자와 사망자의 수를 카운드
#판다스 사용?
# survived_human = titanic[titanic["survived"] == 1]["survived"].count() #살아있는 사람의 수 카운트
# dead_human = titanic[titanic["survived"] == 0]["survived"].count() #사망한 사람의 수 카운트
# print(f"생존자 수 : {survived_human}")
# print(f"사망자 수 : {dead_human}")
