# ==============================
# Tanzila Islam
# PhD Student, Iwate University
# Email: tanzilamohita@gmail.com
# Created Date: 11/2/2022
# ===============================

import pandas as pd
import numpy as np

soy_c3_Chunk0 = pd.read_csv('ModelMetaData_Prediction/'
                'Net_3_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_C3_Chunk_0.csv',
                    low_memory=False)
soy_c3_Chunk1 = pd.read_csv('ModelMetaData_Prediction/'
                'Net_3_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_C3_Chunk_1.csv',
                            low_memory=False)
soy_c3_Chunk2 = pd.read_csv('ModelMetaData_Prediction/'
                'Net_3_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_C3_Chunk_2.csv',
                            low_memory=False)

soy_c3_Chunk0_mean = soy_c3_Chunk0.mean(axis=0)
soy_c3_Chunk1_mean = soy_c3_Chunk1.mean(axis=0)
soy_c3_Chunk2_mean = soy_c3_Chunk2.mean(axis=0)
chunk_list = ['Chunk_0', 'Chunk_1', 'Chunk_2']
# print(soy_c3_Chunk0_mean)
soy_c3_Chunk_df = [soy_c3_Chunk0_mean, soy_c3_Chunk1_mean, soy_c3_Chunk2_mean]
soy_c3_Chunk_df = pd.DataFrame(np.column_stack(soy_c3_Chunk_df))

soy_c3_Chunk_df.columns = list(chunk_list)
soy_c3_Chunk_df["Average"] = soy_c3_Chunk_df.mean(axis=1)
print(soy_c3_Chunk_df)

soy_c3_Chunk_df.to_csv('ModelMetaData_Prediction/'
                'Net_3_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_C3_Chunk_All.csv')


