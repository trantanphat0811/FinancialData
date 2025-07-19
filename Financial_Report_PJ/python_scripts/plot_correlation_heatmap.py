import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Tải dữ liệu
df = pd.read_csv("financial_data.csv")

# Chọn các cột số
numeric_cols = ['Amount', 'TimeSinceLastTransaction', 'IsInternational', 'IsFraud']
df_numeric = df[numeric_cols]

# Thiết lập phong cách cho seaborn
sns.set(style="whitegrid")

# Tính ma trận tương quan
corr = df_numeric.corr()

# Tạo biểu đồ ma trận tương quan
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0)
plt.title('Ma Trận Tương Quan của Các Đặc Trưng')
plt.savefig('correlation_heatmap.png')
plt.close()