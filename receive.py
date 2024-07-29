from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

# 配置数据保存文件路径
DATA_FILE = 'data.json'

# 初始化data.json文件
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as json_file:
        json.dump([], json_file)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.is_json:
        data = request.get_json()
        
        # 读取现有数据
        with open(DATA_FILE, 'r') as json_file:
            existing_data = json.load(json_file)
        
        # 添加新数据
        existing_data.append(data)
        
        # 保存更新后的数据
        with open(DATA_FILE, 'w') as json_file:
            json.dump(existing_data, json_file)
        
        return jsonify({"message": "数据接收成功"}), 200
    else:
        return jsonify({"message": "请求数据格式错误，需为JSON格式"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # 在0.0.0.0地址上运行，监听5000端口
