import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'PassengerId':892, 'Pclass':3, 'Age':34.5,'SibSp':0,
                            'Fare':7.8292,'Sex_male':1,'Embarked_Q':1,'Embarked_S':0})

print(r.json())
    