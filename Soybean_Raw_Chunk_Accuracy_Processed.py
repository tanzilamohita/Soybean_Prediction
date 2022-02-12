# ==============================
# Tanzila Islam
# PhD Student, Iwate University
# Email: tanzilamohita@gmail.com
# Created Date: 11/2/2022
# ===============================

import pandas as pd
import numpy as np

soy_Raw_Chunk0 = pd.read_csv('ModelMetaData_Prediction/'
                'Raw_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_Raw_Chunk_0.csv',
                    low_memory=False)
soy_Raw_Chunk1 = pd.read_csv('ModelMetaData_Prediction/'
                'Raw_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_Raw_Chunk_1.csv',
                            low_memory=False)
soy_Raw_Chunk2 = pd.read_csv('ModelMetaData_Prediction/'
                'Raw_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_Raw_Chunk_2.csv',
                    low_memory=False)
soy_Raw_Chunk3 = pd.read_csv('ModelMetaData_Prediction/'
                'Raw_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_Raw_Chunk_3.csv',
                            low_memory=False)
soy_Raw_Chunk4 = pd.read_csv('ModelMetaData_Prediction/'
                'Raw_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_Raw_Chunk_4.csv',
                    low_memory=False)
soy_Raw_Chunk5 = pd.read_csv('ModelMetaData_Prediction/'
                'Raw_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_Raw_Chunk_5.csv',
                            low_memory=False)
soy_Raw_Chunk6 = pd.read_csv('ModelMetaData_Prediction/'
                'Raw_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_Raw_Chunk_6.csv',
                    low_memory=False)
soy_Raw_Chunk7 = pd.read_csv('ModelMetaData_Prediction/'
                'Raw_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_Raw_Chunk_7.csv',
                            low_memory=False)
soy_Raw_Chunk8 = pd.read_csv('ModelMetaData_Prediction/'
                'Raw_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_Raw_Chunk_8.csv',
                            low_memory=False)
soy_Raw_Chunk9 = pd.read_csv('ModelMetaData_Prediction/'
                'Raw_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_Raw_Chunk_9.csv',
                    low_memory=False)
soy_Raw_Chunk10 = pd.read_csv('ModelMetaData_Prediction/'
                'Raw_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_Raw_Chunk_10.csv',
                            low_memory=False)
soy_Raw_Chunk11 = pd.read_csv('ModelMetaData_Prediction/'
                'Raw_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_Raw_Chunk_11.csv',
                    low_memory=False)
soy_Raw_Chunk12 = pd.read_csv('ModelMetaData_Prediction/'
                'Raw_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_Raw_Chunk_12.csv',
                            low_memory=False)
soy_Raw_Chunk13 = pd.read_csv('ModelMetaData_Prediction/'
                'Raw_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_Raw_Chunk_13.csv',
                    low_memory=False)
soy_Raw_Chunk14 = pd.read_csv('ModelMetaData_Prediction/'
                'Raw_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_Raw_Chunk_14.csv',
                            low_memory=False)
soy_Raw_Chunk15 = pd.read_csv('ModelMetaData_Prediction/'
                'Raw_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_Raw_Chunk_15.csv',
                    low_memory=False)
soy_Raw_Chunk16 = pd.read_csv('ModelMetaData_Prediction/'
                'Raw_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_Raw_Chunk_16.csv',
                            low_memory=False)

soy_Raw_Chunk0_mean = soy_Raw_Chunk0.mean(axis=0)
soy_Raw_Chunk1_mean = soy_Raw_Chunk1.mean(axis=0)
soy_Raw_Chunk2_mean = soy_Raw_Chunk2.mean(axis=0)
soy_Raw_Chunk3_mean = soy_Raw_Chunk3.mean(axis=0)
soy_Raw_Chunk4_mean = soy_Raw_Chunk4.mean(axis=0)
soy_Raw_Chunk5_mean = soy_Raw_Chunk5.mean(axis=0)
soy_Raw_Chunk6_mean = soy_Raw_Chunk6.mean(axis=0)
soy_Raw_Chunk7_mean = soy_Raw_Chunk7.mean(axis=0)
soy_Raw_Chunk8_mean = soy_Raw_Chunk8.mean(axis=0)
soy_Raw_Chunk9_mean = soy_Raw_Chunk9.mean(axis=0)
soy_Raw_Chunk10_mean = soy_Raw_Chunk10.mean(axis=0)
soy_Raw_Chunk11_mean = soy_Raw_Chunk11.mean(axis=0)
soy_Raw_Chunk12_mean = soy_Raw_Chunk12.mean(axis=0)
soy_Raw_Chunk13_mean = soy_Raw_Chunk13.mean(axis=0)
soy_Raw_Chunk14_mean = soy_Raw_Chunk14.mean(axis=0)
soy_Raw_Chunk15_mean = soy_Raw_Chunk15.mean(axis=0)
soy_Raw_Chunk16_mean = soy_Raw_Chunk16.mean(axis=0)

chunk_list = ['Chunk_0', 'Chunk_1', 'Chunk_2', 'Chunk_3',
            'Chunk_4', 'Chunk_5', 'Chunk_6', 'Chunk_7', 'Chunk_8',
            'Chunk_9', 'Chunk_10', 'Chunk_11',
            'Chunk_12', 'Chunk_13', 'Chunk_14', 'Chunk_15',
             'Chunk_16']

# print(soy_Raw_Chunk0_mean)
soy_Raw_Chunk_df = [soy_Raw_Chunk0_mean, soy_Raw_Chunk1_mean,
                   soy_Raw_Chunk2_mean, soy_Raw_Chunk3_mean,
                   soy_Raw_Chunk4_mean, soy_Raw_Chunk5_mean,
                   soy_Raw_Chunk6_mean, soy_Raw_Chunk7_mean,
                   soy_Raw_Chunk8_mean, soy_Raw_Chunk9_mean,
                    soy_Raw_Chunk10_mean, soy_Raw_Chunk11_mean,
                    soy_Raw_Chunk12_mean, soy_Raw_Chunk13_mean,
                    soy_Raw_Chunk14_mean, soy_Raw_Chunk15_mean,
                    soy_Raw_Chunk16_mean]
soy_Raw_Chunk_df = pd.DataFrame(np.column_stack(soy_Raw_Chunk_df))

soy_Raw_Chunk_df.columns = list(chunk_list)
soy_Raw_Chunk_df["Average"] = soy_Raw_Chunk_df.mean(axis=1)
print(soy_Raw_Chunk_df)

soy_Raw_Chunk_df.to_csv('ModelMetaData_Prediction/'
                'Raw_RF_Chunk/'
                'Soybean_PredictionAccuracy_RF_Raw_Chunk_All.csv')


