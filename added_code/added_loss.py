import subprocess
import os
import yaml

# Đọc kết quả từ pip show
result = subprocess.run(['pip', 'show', 'paddlepaddle'], capture_output=True, text=True)
location = ''
for line in result.stdout.split("\n"):
    if line.startswith("Location:"):
        location = line.split(":", 1)[1].strip()
if location == '':
    result = subprocess.run(['pip', 'show', 'paddlepaddle-gpu'], capture_output=True, text=True)
    for line in result.stdout.split("\n"):
        if line.startswith("Location:"):
            location = line.split(":", 1)[1].strip()

# Ghép đường dẫn với thư mục cần thay đổi
location = os.path.join(location, "paddle", "nn")

# Đọc file YAML để lấy danh sách thay đổi
current_dir = os.path.dirname(os.path.realpath(__file__))
loss_file = os.path.join(current_dir, 'added_loss.yaml')
with open(loss_file, 'r') as file:
    changes = yaml.safe_load(file)
    
# Thực hiện thay đổi trên các file được chỉ định
for file_path, modifications in changes['files'].items():
    full_path = os.path.join(location, file_path)
    with open(full_path, 'r') as f:
        lines = f.readlines()

    # Áp dụng các thay đổi trong file
    for change in modifications['changes']:
        line_index = change['line']
        content = change['content']
        lines.insert(line_index, content + "\n")

    # Ghi lại file sau khi thay đổi
    with open(full_path, 'w') as f:
        f.writelines(lines)
