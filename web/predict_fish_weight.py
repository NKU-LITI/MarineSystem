import joblib
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import os
import warnings



def make_data():
    feature_names = ['Length1(cm)', 'Length2(cm)', 'Length3(cm)', 'Height(cm)', 'Width(cm)']
    mean_values = [25.655769, 27.786538, 30.571154, 8.951128, 4.375719]
    min_values = [7.5, 8.4, 8.8, 1.7284, 1.0476]
    max_values = [52, 56, 59.7, 18.957, 8.142]
    # 生成一个随机的新鱼的数据，在平均值周围波动
    new_values = np.random.normal(mean_values, (np.array(mean_values)-np.array(min_values))/3)
    new_values_df = pd.DataFrame([new_values], columns=feature_names)
    return new_values_df


def use_model(new_values, model_path=None, scaler_path=None):
    # 加载模型
    model = joblib.load(model_path)
    # 加载标准化模型
    scaler = joblib.load(scaler_path)
    # 标准化数据
    new_values_scaled = scaler.transform(new_values)
    new_values_scaled_df = pd.DataFrame(new_values_scaled, columns=new_values.columns)
    # 预测
    weight = model.predict(new_values_scaled_df)
    return weight[0]


def predict_weight():
    model_path = 'web/save_weights/fish_weight_predictor.pkl'
    scaler_path = 'web/save_weights/fish_weight_scaler.pkl'
    weight = -1
    # warnings.filterwarnings("ignore")
    while weight <0 or weight > 1100:
        new_values = make_data()
        weight = use_model(new_values, model_path, scaler_path)
    return new_values, weight

    

