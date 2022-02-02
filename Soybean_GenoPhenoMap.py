# ==============================
# Tanzila Islam
# PhD Student, Iwate University
# Email: tanzilamohita@gmail.com
# Created Date: 1/24/2022
# ===============================

import pandas as pd
import numpy as np

Y = pd.read_csv('Data_Prediction/Soybean_Y.csv', index_col=0)
missing_values_Y = Y.isnull().sum().sum()
print("Total Missing values in Y:", missing_values_Y)
Y = Y.dropna()
Y.columns = np.arange(0, len(Y.columns))
X = pd.read_csv('Data_Prediction/Compress_3_Chunk/Soybean_X_C3_0.csv',
                low_memory=False, index_col=0)
X = X.T
X.columns = np.arange(0, len(X.columns))
X = X.drop(X.index.difference(Y.index))
Y = Y.drop(Y.index.difference(X.index))
missing_values_X = X.isnull().sum().sum()
print("Total Missing values in X:", missing_values_X)
print("X: ", X.shape)
print("Y: ", Y.shape)

# X.to_csv("Data_Prediction/Compress_3_Chunk/Soybean_X_C3_0_Mapped.csv")
# Y.to_csv("Data_Prediction/Soybean_Y_Mapped.csv")
