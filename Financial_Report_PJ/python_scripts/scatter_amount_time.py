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

# Thiết lập phong cách cho seaborn
sns.set(style="whitegrid")

# Tạo biểu đồ phân tán
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='TimeSinceLastTransaction', y='Amount', hue='IsFraud', style='IsFraud', size='IsFraud', sizes={0: 50, 1: 100})
plt.title('Mối Quan Hệ giữa Số Tiền và Thời Gian Kể Từ Giao Dịch Trước')
plt.xlabel('Thời Gian Kể Từ Giao Dịch Trước (phút)')
plt.ylabel('Số Tiền (USD)')
plt.yscale('log')
plt.legend(title='Gian Lận', labels=['Không', 'Có'])
plt.savefig(os.path.join(output_dir, "scatter_amount_time.png"))
plt.close()