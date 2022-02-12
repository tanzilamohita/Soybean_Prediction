# ==============================
# Tanzila Islam
# PhD Student, Iwate University
# Email: tanzilamohita@gmail.com
# Created Date: 11/2/2022
# ===============================

import pandas as pd
import numpy as np

soy_c1_Chunk0 = pd.read_csv('ModelMetaData_Prediction/'
                'Net_1_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_c1_Chunk_0.csv',
                    low_memory=False)
soy_c1_Chunk1 = pd.read_csv('ModelMetaData_Prediction/'
                'Net_1_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_c1_Chunk_1.csv',
                            low_memory=False)
soy_c1_Chunk2 = pd.read_csv('ModelMetaData_Prediction/'
                'Net_1_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_c1_Chunk_2.csv',
                    low_memory=False)
soy_c1_Chunk3 = pd.read_csv('ModelMetaData_Prediction/'
                'Net_1_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_c1_Chunk_3.csv',
                            low_memory=False)
soy_c1_Chunk4 = pd.read_csv('ModelMetaData_Prediction/'
                'Net_1_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_c1_Chunk_4.csv',
                    low_memory=False)
soy_c1_Chunk5 = pd.read_csv('ModelMetaData_Prediction/'
                'Net_1_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_c1_Chunk_5.csv',
                            low_memory=False)
soy_c1_Chunk6 = pd.read_csv('ModelMetaData_Prediction/'
                'Net_1_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_c1_Chunk_6.csv',
                    low_memory=False)
soy_c1_Chunk7 = pd.read_csv('ModelMetaData_Prediction/'
                'Net_1_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_c1_Chunk_7.csv',
                            low_memory=False)
soy_c1_Chunk8 = pd.read_csv('ModelMetaData_Prediction/'
                'Net_1_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_c1_Chunk_8.csv',
                            low_memory=False)

soy_c1_Chunk0_mean = soy_c1_Chunk0.mean(axis=0)
soy_c1_Chunk1_mean = soy_c1_Chunk1.mean(axis=0)
soy_c1_Chunk2_mean = soy_c1_Chunk2.mean(axis=0)
soy_c1_Chunk3_mean = soy_c1_Chunk3.mean(axis=0)
soy_c1_Chunk4_mean = soy_c1_Chunk4.mean(axis=0)
soy_c1_Chunk5_mean = soy_c1_Chunk5.mean(axis=0)
soy_c1_Chunk6_mean = soy_c1_Chunk6.mean(axis=0)
soy_c1_Chunk7_mean = soy_c1_Chunk7.mean(axis=0)
soy_c1_Chunk8_mean = soy_c1_Chunk8.mean(axis=0)

chunk_list = ['Chunk_0', 'Chunk_1', 'Chunk_2', 'Chunk_3',
            'Chunk_4', 'Chunk_5', 'Chunk_6', 'Chunk_7', 'Chunk_8']
# print(soy_c1_Chunk0_mean)
soy_c1_Chunk_df = [soy_c1_Chunk0_mean, soy_c1_Chunk1_mean,
                   soy_c1_Chunk2_mean, soy_c1_Chunk3_mean,
                   soy_c1_Chunk4_mean, soy_c1_Chunk5_mean,
                   soy_c1_Chunk6_mean, soy_c1_Chunk7_mean,
                   soy_c1_Chunk8_mean]
soy_c1_Chunk_df = pd.DataFrame(np.column_stack(soy_c1_Chunk_df))

soy_c1_Chunk_df.columns = list(chunk_list)
soy_c1_Chunk_df["Average"] = soy_c1_Chunk_df.mean(axis=1)
print(soy_c1_Chunk_df)

soy_c1_Chunk_df.to_csv('ModelMetaData_Prediction/'
                'Net_1_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_c1_Chunk_All.csv')


