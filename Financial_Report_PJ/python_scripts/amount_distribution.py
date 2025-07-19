
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Đường dẫn đến file dữ liệu
script_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(os.path.dirname(script_dir), "data", "financial_data.csv")

# Kiểm tra file tồn tại
if not os.path.exists(data_file):
    print(f"Error: {data_file} not found!")
    exit(1)

# Tải dữ liệu
df = pd.read_csv(data_file)

# Thiết lập phong cách cho seaborn
sns.set(style="whitegrid")

# Tạo biểu đồ phân bố số tiền
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Amount', hue='IsFraud', bins=50, kde=True, log_scale=True)
plt.title('Phân bố Số Tiền Giao Dịch (Log Scale)')
plt.xlabel('Số Tiền (USD)')
plt.ylabel('Số Lượng')
plt.legend(title='Gian Lận', labels=['Không', 'Có'])
plt.savefig(os.path.join(os.path.dirname(script_dir), "output_images", "amount_distribution.png"))
plt.close()
