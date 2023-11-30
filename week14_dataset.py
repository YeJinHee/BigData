import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

titanic = sns.load_dataset('titanic')
#print(titanic.info())
titanic = titanic.drop(['who', 'deck', 'embark_town', 'alive', 'class', 'adult_male', 'alone'], axis=1)
titanic = titanic.dropna() #결축치가 있는 행 정리

titanic['sex'] = titanic['sex'].map({'male': 0, 'female': 1})
titanic['embarked'] = titanic['embarked'].map({'S': 0, 'C': 1, 'Q': 2})

X = titanic.drop('survived', axis=1)
y = titanic['survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=1)

#모델 생성
model = LogisticRegression(solver='liblinear')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f"정확도: {accuracy_score(y_test, y_pred)}")