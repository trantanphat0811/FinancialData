import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Tải dữ liệu
df = pd.read_csv("financial_data.csv")

# Thiết lập phong cách cho seaborn
sns.set(style="whitegrid")

# Tạo biểu đồ phân bố số tiền
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Amount', hue='IsFraud', bins=50, kde=True, log_scale=True)
plt.title('Phân bố Số Tiền Giao Dịch (Log Scale)')
plt.xlabel('Số Tiền (USD)')
plt.ylabel('Số Lượng')
plt.legend(title='Gian Lận', labels=['Không', 'Có'])
plt.savefig('amount_distribution.png')
plt.close()