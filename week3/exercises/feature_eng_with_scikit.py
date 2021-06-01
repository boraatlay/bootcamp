"""
Example of engineering features with Scikit only
"""
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np

#
# 1. get data
#
df = pd.read_csv('example_project_solution/train.csv', index_col=0)
del df['Ticket']
del df['Cabin']

X = df.iloc[:, 1:]  # remove first column
y = df['Survived']

#
# 2. Define feature engineering steps
# 
def name_length(df):
    """function that gets a DataFrame and outputs a DataFrame"""
    # input: df
    # output: numpy matrix
    length = df[df.columns[0]].str.len()
    return length.values.reshape(-1, 1) # makes a matrix out of the result

# you could run this function like this:
#d = pd.DataFrame([['Mr. Bean'], ['Mrs. Dr. Bean']])
#print(name_length(d))

fill_embarked = make_pipeline(
             SimpleImputer(strategy='most_frequent'),
             OneHotEncoder(sparse=False, handle_unknown='ignore')
)

# alternative: make_column_transformer(...) without the strings
trans = ColumnTransformer([
       ('fill_embarked', fill_embarked, ['Embarked']),
       ('bins         ', KBinsDiscretizer(n_bins=3, encode='onehot-dense', strategy='quantile'), ['Fare']),
       ('name         ', FunctionTransformer(name_length), ['Name']),
       ('other cats   ', OneHotEncoder(sparse=False, handle_unknown='ignore'), ['Sex', 'Pclass']),
       ('do_nothing   ', 'passthrough', ['Parch', 'SibSp']),
])

#
# 3. fit and transform everything
#
model = make_pipeline(
       trans,
       MinMaxScaler(),
       LogisticRegression()
)
model.fit(X, y)
print('training acc:', round(model.score(X, y), 3))

"""
trans.fit(X)               # X is a DataFrame with titanic data
Xfe = trans.transform(X)  

print(Xfe.shape)
print(Xfe[0])

scaler.fit(Xfe)              # result of ColumnTransformer
Xsc = scaler.transform(Xfe)  # use this to train your model

#
# 5. train the model
#
model = LogisticRegression()
model.fit(Xsc, y)
print('training acc:', round(model.score(Xsc, y), 3))
"""