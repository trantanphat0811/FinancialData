import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Tải dữ liệu
df = pd.read_csv("financial_data.csv")

# Thiết lập phong cách cho seaborn
sns.set(style="whitegrid")

# Tạo biểu đồ phân tán
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='TimeSinceLastTransaction', y='Amount', hue='IsFraud', style='IsFraud', size='IsFraud', sizes={0: 50, 1: 100})
plt.title('Mối Quan Hệ giữa Số Tiền và Thời Gian Kể Từ Giao Dịch Trước')
plt.xlabel('Thời Gian Kể Từ Giao Dịch Trước (phút)')
plt.ylabel('Số Tiền (USD)')
plt.yscale('log')  # Sử dụng thang log cho Amount
plt.legend(title='Gian Lận', labels=['Không', 'Có'])
plt.savefig('scatter_amount_time.png')
plt.close()