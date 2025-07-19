from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd

# Đọc dữ liệu từ file CSV (thay 'du_lieu.csv' bằng tên file thực tế của bạn)
df = pd.read_csv('du_lieu.csv')

# Mã hóa cột phân loại (Loại Giao Dịch)
le = LabelEncoder()
df['Loại Giao Dịch'] = le.fit_transform(df['Loại Giao Dịch'])

# Loại bỏ cột không cần thiết (Mã Giao Dịch, Mã Nhà Cung Cấp, Mã Khách Hàng không mang thông tin dự đoán)
df = df.drop(['Mã Giao Dịch', 'Mã Nhà Cung Cấp', 'Mã Khách Hàng'], axis=1)

# Chia dữ liệu thành tập huấn luyện và kiểm tra
X = df.drop('Gian Lận', axis=1)
y = df['Gian Lận']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Kiểm tra phân bố nhãn trong tập huấn luyện
print("Phân bố nhãn trong tập huấn luyện:")
print(y_train.value_counts(normalize=True))