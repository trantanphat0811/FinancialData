import pandas as pd
from sklearn.utils import resample

# Ví dụ dữ liệu mẫu
X_train = pd.DataFrame({
    'feature1': [1, 2, 3, 4, 5, 6],
    'feature2': [10, 20, 30, 40, 50, 60]
})
y_train = pd.Series([0, 0, 0, 1, 1, 1])

# Áp dụng resample để cân bằng dữ liệu (up-sampling lớp thiểu số)
X = pd.concat([X_train, y_train], axis=1)
majority = X[X_train['feature1'] <= 3]
minority = X[X_train['feature1'] > 3]

minority_upsampled = resample(minority,
                              replace=True,
                              n_samples=len(majority),
                              random_state=42)

upsampled = pd.concat([majority, minority_upsampled])
X_train_resampled = upsampled[['feature1', 'feature2']]
y_train_resampled = upsampled[0]

# Kiểm tra phân bố nhãn sau resample
print("Phân bố nhãn sau resample:")
print(y_train_resampled.value_counts(normalize=True))