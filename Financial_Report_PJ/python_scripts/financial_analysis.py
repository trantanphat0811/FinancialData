import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Tải file CSV
df = pd.read_csv("financial_data.csv")

# Xem thông tin cơ bản
print("Thông tin dữ liệu:")
print(df.info())
print("\nMô tả dữ liệu:")
print(df.describe())

# Kiểm tra giá trị thiếu
print("\nGiá trị thiếu:")
print(df.isnull().sum())

# Phân tích nhãn Gian Lận
print("\nPhân bố nhãn Gian Lận:")
print(df['IsFraud'].value_counts(normalize=True))

# Trực quan hóa phân bố Số Tiền
plt.figure(figsize=(10, 6))
sns.histplot(df['Amount'], bins=50, kde=True)
plt.title('Phân bố Số Tiền Giao Dịch')
plt.xlabel('Số Tiền (USD)')
plt.ylabel('Số lượng')
plt.show()

# Trực quan hóa phân bố Loại Giao Dịch
plt.figure(figsize=(10, 6))
sns.countplot(x='TransactionType', hue='IsFraud', data=df)
plt.title('Phân bố Loại Giao Dịch theo Gian Lận')
plt.xlabel('Loại Giao Dịch')
plt.ylabel('Số lượng')
plt.show()