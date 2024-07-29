import requests

server_url = 'http://207.148.93.106:5000/download'  # 使用服务器IP地址

# 声明全局变量
data = None

def download_data(url):
    global data
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("数据下载成功！")
        print("下载的数据：", data)
    else:
        print(f"数据下载失败，状态码：{response.status_code}")
        data = None

def get_temperature():
    if data and 'Temperature' in data:
        return data['Temperature']
    else:
        return None

def get_angle_x():
    if data and 'Angle_X' in data:
        return data['Angle_X']
    else:
        return None
    
def get_angle_y():
    if data and 'Angle_Y' in data:
        return data['Angle_Y']
    else:
        return None
    
def get_angle_z():
    if data and 'Angle_Z' in data:
        return data['Angle_Z']
    else:
        return None
    
def get_pressure():
    if data and 'Pressure' in data:
        return data['Pressure']
    else:
        return None

if __name__ == "__main__":
    download_data(server_url)
    temperature = get_temperature()
    angle_x = get_angle_x()
    if temperature is not None:
        print(f"Temperature: {temperature}")
    else:
        print("Temperature data not available.")
    
    if angle_x is not None:
        print(f"Angle_X: {angle_x}")
    else:
        print("Angle_X data not available.")
