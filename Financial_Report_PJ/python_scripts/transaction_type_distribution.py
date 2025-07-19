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

# Tạo biểu đồ thanh
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='TransactionType', hue='IsFraud')
plt.title('Phân bố Loại Giao Dịch theo Gian Lận')
plt.xlabel('Loại Giao Dịch')
plt.ylabel('Số Lượng')
plt.legend(title='Gian Lận', labels=['Không', 'Có'])
plt.savefig(os.path.join(output_dir, "transaction_type_distribution.png"))
plt.close()