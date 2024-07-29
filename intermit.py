from flask import Flask, request, jsonify
import os
import json
import requests

app = Flask(__name__)

# 配置数据保存文件路径
DATA_FILE = 'data.json'
WEBHOOK_URL = 'http://your-webhook-server-url/webhook'  # 替换为你的Webhook服务器URL

# 初始化data.json文件
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as json_file:
        json.dump([], json_file)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.is_json:
        data = request.get_json()

        # 根据Type字段执行不同的操作
        if data.get('Type') == 'server':
            # 读取现有数据
            if os.path.getsize(DATA_FILE) == 0:
                existing_data = []
            else:
                with open(DATA_FILE, 'r') as json_file:
                    try:
                        existing_data = json.load(json_file)
                        if isinstance(existing_data, dict):
                            existing_data = [existing_data]
                    except json.JSONDecodeError:
                        existing_data = []
            
            # 添加新数据
            existing_data.append(data)
            
            # 保存更新后的数据
            with open(DATA_FILE, 'w') as json_file:
                json.dump(existing_data, json_file)
            
            return jsonify({"message": "数据接收成功并保存到data.json"}), 200
        elif data.get('Type') == 'windows' and 'cmd' in data:
            # 将cmd内容发送到Webhook服务器
            cmd_data = {"cmd": data['cmd']}
            response = requests.post(WEBHOOK_URL, json=cmd_data)
            if response.status_code == 200:
                return jsonify({"message": "cmd已成功发送到Webhook服务器"}), 200
            else:
                return jsonify({"message": "cmd发送到Webhook服务器失败"}), 500
        else:
            return jsonify({"message": "无效的Type或缺少cmd字段"}), 400
    else:
        return jsonify({"message": "请求数据格式错误，需为JSON格式"}), 400

@app.route('/download', methods=['GET'])
def get_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as json_file:
            data = json.load(json_file)
        return jsonify(data), 200
    else:
        return jsonify({"message": "数据文件未找到"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # 在0.0.0.0地址上运行，监听5000端口
