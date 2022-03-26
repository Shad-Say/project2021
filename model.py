# Importing the libraries

import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
#from sklearn.preprocessing import StandardScaler
#from sklearn.linear_model import LinearRegression
from sklearn.ensemble import BaggingRegressor
from sklearn.tree import DecisionTreeRegressor

#EDA
data = pd.read_csv('concrete_data.csv')
#df.columns=["Cement","Blast Furnace Slag","Fly Ash","Water","Superplasticizer","Coarse Aggregate","Fine Aggregate","Age","CC Strength"]

#Data Preprocessing
X = data.iloc[:,:-1]
Y = data.iloc[:,-1]
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

#Scaling
#sc = StandardScaler()
#x_train = sc.fit_transform(x_train)
#x_test = sc.transform(x_test)

#Linear Regression
#lr = LinearRegression()
dt=DecisionTreeRegressor()
br=BaggingRegressor(base_estimator=dt,n_estimators=400)
br.fit(X,Y)

#Pickle
pickle.dump(br,open ('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
#print(model.predict([[540,0,0,162,2.5,1040,676,28]]))




