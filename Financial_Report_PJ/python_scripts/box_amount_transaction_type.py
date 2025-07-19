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

# Tạo biểu đồ hộp
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='TransactionType', y='Amount', hue='IsFraud')
plt.title('Phân bố Số Tiền theo Loại Giao Dịch')
plt.xlabel('Loại Giao Dịch')
plt.ylabel('Số Tiền (USD)')
plt.yscale('log')
plt.legend(title='Gian Lận', labels=['Không', 'Có'])
plt.savefig(os.path.join(output_dir, "box_amount_transaction_type.png"))
plt.close()