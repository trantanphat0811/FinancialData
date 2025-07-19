import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Tải dữ liệu
df = pd.read_csv("financial_data.csv")

# Thiết lập phong cách cho seaborn
sns.set(style="whitegrid")

# Tạo biểu đồ thanh
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='TransactionType', hue='IsFraud')
plt.title('Phân bố Loại Giao Dịch theo Gian Lận')
plt.xlabel('Loại Giao Dịch')
plt.ylabel('Số Lượng')
plt.legend(title='Gian Lận', labels=['Không', 'Có'])
plt.savefig('transaction_type_distribution.png')
plt.close()