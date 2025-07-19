import os

# Đường dẫn đến thư mục chứa các script và file dữ liệu
script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(os.path.dirname(script_dir), "data")
output_dir = os.path.join(os.path.dirname(script_dir), "output_images")

# Tạo thư mục output_images nếu chưa tồn tại
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Kiểm tra file financial_data.csv
data_file = os.path.join(data_dir, "financial_data.csv")
if not os.path.exists(data_file):
    print(f"Error: {data_file} not found!")
    exit(1)

# Danh sách các script cần chạy
scripts = [
    "amount_distribution.py",
    "box_amount_transaction_type.py",
    "correlation_heatmap.py",
    "scatter_amount_time.py",
    "transaction_type_distribution.py"
]

# Chạy từng script
for script in scripts:
    script_path = os.path.join(script_dir, script)
    if not os.path.exists(script_path):
        print(f"Error: {script_path} not found!")
        continue
    print(f"Running {script}...")
    result = os.system(f"python \"{script_path}\"")
    if result != 0:
        print(f"Error: Failed to run {script}")

print("All scripts executed!")