import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Đường dẫn đến file dữ liệu
script_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(os.path.dirname(script_dir), "data", "financial_data.csv")
output_dir = os.path.join(os.path.dirname(script_dir), "output_images")

# Kiểm tra file tồn tại
if not os.path.exists(data_file):
    print(f"Error: {data_file} not found!")
    exit(1)

# Tạo thư mục output_images nếu chưa tồn tại
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Tải dữ liệu
df = pd.read_csv(data_file)

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
plt.savefig(os.path.join(output_dir, "correlation_heatmap.png"))
plt.close()