import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
#read data
dataframe = pd.read_fwf('brain_body.txt')
x_values = dataframe[['Brain']]
y_values = dataframe[['Body']]
s = 0
