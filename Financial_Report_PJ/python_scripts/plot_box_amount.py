import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Tải dữ liệu
df = pd.read_csv("financial_data.csv")

# Thiết lập phong cách cho seaborn
sns.set(style="whitegrid")

# Tạo biểu đồ hộp
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='TransactionType', y='Amount', hue='IsFraud')
plt.title('Phân bố Số Tiền theo Loại Giao Dịch')
plt.xlabel('Loại Giao Dịch')
plt.ylabel('Số Tiền (USD)')
plt.yscale('log')  # Sử dụng thang log cho Amount
plt.legend(title='Gian Lận', labels=['Không', 'Có'])
plt.savefig('box_amount_transaction_type.png')
plt.close()