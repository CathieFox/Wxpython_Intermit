import re
import serial
import json
import requests
import subprocess

from config import *

server_url = 'http://207.148.93.106:5000/webhook'  # 替换为你的Webhook服务器URL

def read_from_serial(port='/dev/ttyRPMSG0', baudrate=115200, timeout=1):
    try:
        with serial.Serial(port, baudrate, timeout=timeout) as ser:
            while True:
                line = ser.readline().decode('utf-8').strip()
                if line:
                    print("接收到的数据：", line)
                    data = parse_data(line)
                    if data:
                        print("解析后的字典：", data)
                        upload_data(server_url, data)
    except serial.SerialException as e:
        print(f"Error reading from serial port: {e}")

def parse_data(serial_data):
    pattern = r'\{Temperature\s*=\s*(\d+),\s*Pressure\s*=\s*(\d+),\s*Angle_X\s*=\s*(-?\d+),\s*Angle_Y\s*=\s*(\d+),\s*Angle_Z\s*=\s*(\d+)\}'
    match = re.search(pattern, serial_data)
    if match:
        data = {
            "Type": 'server',
            "Temperature": float(match.group(1)),
            "Pressure": float(match.group(2)),
            "Angle_X": float(match.group(3)),
            "Angle_Y": float(match.group(4)),
            "Angle_Z": float(match.group(5)),
        }
        return data
    else:
        print("数据解析失败")
        return None

def upload_data(url, data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print("数据上传成功！")
    else:
        print(f"数据上传失败，状态码：{response.status_code}")





def init():
  subprocess.call(cmd_mnt,   shell=True)
  subprocess.call(cmd_start, shell=True)
  subprocess.call(cmd_open,  shell=True)

def shutdown():
    subprocess.call(cmd_stop, shell=True)
  
def command():
    print("Commander Started!")
    command = input("Enter Your Command here!")
    
    if command == Init:
        init()
        
    if command == Shutdown:
        shutdown()



if __name__ == "__main__":
    read_from_serial()
