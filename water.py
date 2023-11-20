import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Tạo dữ liệu giả định
data = {
    'Temperature': [25, 28, 30, 32, 35, 30, 28, 26, 24, 22],
    'Humidity': [50, 55, 60, 65, 70, 65, 60, 55, 50, 45],
    'WaterConsumption': [10, 12, 14, 16, 18, 15, 13, 11, 10, 9],
}

df = pd.DataFrame(data)

# Chia dữ liệu thành dữ liệu đào tạo và dữ liệu kiểm tra
X = df[['Temperature', 'Humidity']]
y = df['WaterConsumption']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Xây dựng mô hình hồi quy tuyến tính
model = LinearRegression()
model.fit(X_train, y_train)

# Dự đoán lượng nước còn lại sau một số giá trị nhiệt độ và độ ẩm cho trước
new_data = np.array([[27, 58], [29, 62], [31, 68]])
predictions = model.predict(new_data)

for i in range(len(new_data)):
    print(f'Nhiệt độ: {new_data[i][0]}, Độ ẩm: {new_data[i][1]} => Lượng nước còn lại dự đoán: {predictions[i]:.2f}')

# Đánh giá mô hình
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')