import requests
import pandas as pan
import numpy as np
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
from  sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import BayesianRidge

from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

from functools import reduce  # Required in Python 3
import operator

def prod(iterable):
    return reduce(operator.mul, iterable, 1)
def test():
    # req = requests
    # get = req.get(url="https://public-api.cian.ru/v1/get-my-offers?source=manual&statuses=inactive&statuses=published",
    #               headers={'Authorization':'Bearer <ACCESS TOKEN>'})
    # print(get)
    df = pan.read_excel("train.xlsx",index_col=False)
    df = df.fillna('0')
    # print(df.values)
    y, x = data_processing(df)
    x.to_csv('output',index=False)
    # print(y)
    X_train, X_validation, y_train, y_validation = train_test_split(x, y, test_size=0.1, random_state=21)
    ln = LinearRegression()
    ln.fit(X_train, y_train)
    pred = ln.predict(X_validation)
    pred = pred * 1000000
    y_validation = y_validation * 1000000
    pan.DataFrame(data={'Цена': pred}).to_csv('pred',index=False)
    pan.DataFrame(data={'Цена':y_validation}).to_csv('val',index=False)

    print(mean_absolute_error(y_validation,pred))
    print(mean_squared_error(y_validation,pred))

def data_processing(data):

    sale = data['Цена']
    sale = sale.map(lambda x: int(x.lstrip('').rstrip(' руб., Свободная продажа, Возможна ипотека руб., 214-ФЗ, Договор уступки права требования,Альтернатива')))
    sale = sale * 0.000001

    le = LabelEncoder()
    data = data.drop('Цена', axis=1)
    data['Площадь, м2'] = data['Площадь, м2'].map(lambda x: prod(float (f)for f in x.split('/')))
    square = data['Площадь, м2'] * 0.001
    data = data.drop('Площадь, м2',axis=1)
    floors = data['Дом'].map(lambda x: str(x.lstrip('').rstrip(' ,,Кирпичный,Панельный,Блочный')).split('/'))
    data = data.drop('Дом',axis=1)
    ceiling = data['Высота потолков, м']
    # ceiling = ceiling.map(lambda x: 0 if (x == np.NaN) else x)

    rooms = data['Количество комнат'].map(lambda x: x.lstrip('').rstrip(' , ,Изолированная,Смежная,Оба вариант') )
    data = data.drop('Высота потолков, м',axis=1)
    data = data.drop('Количество комнат',axis=1)

    # print(data['Дом'])
    encoded_series = data[data.columns[:]].apply(le.fit_transform)
    encoded_series['Этаж'] = floors.map(lambda x: x[0])
    encoded_series['Этажи'] = floors.map(lambda x:x[1])
    encoded_series['Высота потолков'] = ceiling
    encoded_series['Площадь'] = square
    encoded_series['Колличество комнат'] = rooms

    return sale, encoded_series







