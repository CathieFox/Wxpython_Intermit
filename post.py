import json
import requests
from random import uniform


server_url = 'http://207.148.93.106:5000/webhook'


# 生成随机数据
def generate_data():
    data = {
        "Type":'server',
        "Temperature":round(uniform(20.0, 30.0), 2),  # 生成20到30之间的随机温度
        "Pressure":round(uniform(20.0, 30.0), 2),  # 生成20到30之间的随机温度
        "Angle_X":round(uniform(-90.0, 90.0), 2),  # 生成-90到90之间的随机角度
        "Angle_Y":round(uniform(20.0, 30.0), 2),  # 生成20到30之间的随机温度
        "Angle_Z":round(uniform(20.0, 30.0), 2), # 生成20到30之间的随机温度
    }
    return data


# 上传数据至Webhook
def upload_data(url, data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print("数据上传成功！")
    else:
        print(f"数据上传失败，状态码：{response.status_code}")


if __name__ == "__main__":
    data = generate_data()
    print(f"生成的数据：{data}")
    upload_data(server_url, data)
