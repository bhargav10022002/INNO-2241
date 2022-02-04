import numpy as np
import pickle
import pandas as pd
import lightgbm as lgb

dataset1 = pd.read_csv('OTT Final Cleaned data.csv')
del dataset1['Unnamed: 0']

X = dataset1.iloc[:,1:6].values
y = dataset1.iloc[:,6].values

clf = lgb.LGBMClassifier()
clf.fit(X, y)

pickle.dump(clf,open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))