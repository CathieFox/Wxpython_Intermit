import wx
import time
import requests

server_url = 'http://207.148.93.106:5000/download'  # 使用服务器IP地址

from download import *

# 声明全局变量

class WelcomeFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(WelcomeFrame, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)

        welcome_text = wx.StaticText(panel, label="Welcome to the System Controller")
        welcome_text.SetPosition((50, 20))

        self.start_button = self.create_button(panel, "Start", self.on_start, (100, 60))
        self.exit_button = self.create_button(panel, "Exit", self.on_exit, (100, 100))

        self.SetTitle('Welcome')
        self.SetSize((300, 200))
        self.Centre()
        self.Show(True)

    def create_button(self, parent, label, handler, pos):
        button = wx.Button(parent, label=label, pos=pos)
        button.Bind(wx.EVT_BUTTON, handler)
        return button

    def on_start(self, event):
        self.Hide()
        main_frame = Client(None)
        main_frame.Show()

    def on_exit(self, event):
        self.Close(True)
        wx.GetApp().ExitMainLoop()

class Client(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Client, self).__init__(*args, **kwargs)
        self.InitUI()
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update_data, self.timer)
        self.timer.Start(2000)  # 每隔2秒更新一次

    def InitUI(self):
        panel = wx.Panel(self)

        # 设置窗口大小并居中
        self.SetSize((700, 400))
        self.Centre()

        # 第一个文本框和标题
        title1 = wx.StaticText(panel, label="TEMPERATURE")
        title1.SetPosition((20, 20))
        self.data_display_1 = self.create_text_ctrl(panel, (20, 40), (200, 100))

        # 第二个文本框和标题
        title2 = wx.StaticText(panel, label="PRESSURE")
        title2.SetPosition((240, 20))
        self.data_display_2 = self.create_text_ctrl(panel, (240, 40), (200, 100))

        # 第三个文本框和标题
        title3 = wx.StaticText(panel, label="ANGLE")
        title3.SetPosition((460, 20))
        self.data_display_3 = self.create_text_ctrl(panel, (460, 40), (200, 100))

        # 输入框和按钮居中
        frame_width, frame_height = self.GetSize()
        input_width, input_height = 350, 50
        button_width, button_height = 100, 50

        input_x = (frame_width - input_width) // 2
        input_y = (frame_height // 2) + 20
        button_x = (frame_width - button_width) // 2
        button_y = input_y + input_height + 10

        self.text_input = wx.TextCtrl(panel, pos=(input_x, input_y), size=(input_width, input_height))
        self.add_button = self.create_button(panel, "Send CMD", self.send_cmd, (button_x, button_y))

        # 额外两个按钮
        self.button1 = self.create_button(panel, "Turn ON", self.on_button1_click, (100, 300))
        self.button2 = self.create_button(panel, "Shutdown", self.on_button2_click, (550, 300))

        # 退出按钮居中
        exit_button_x = (frame_width - button_width) // 2
        exit_button_y = frame_height - button_height - 40
        self.exit_button = self.create_button(panel, "Exit", self.on_exit, (exit_button_x, exit_button_y))

        self.SetTitle('Client')
        self.Show(True)

    def create_text_ctrl(self, parent, pos, size):
        text_ctrl = wx.TextCtrl(parent, style=wx.TE_MULTILINE | wx.TE_READONLY, pos=pos, size=size)
        font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        text_ctrl.SetFont(font)
        return text_ctrl

    def create_button(self, parent, label, handler, pos):
        button = wx.Button(parent, label=label, pos=pos)
        button.Bind(wx.EVT_BUTTON, handler)
        return button

    def send_cmd(self, event):
        command = self.text_input.GetValue()
        self.execute_custom_command(command)
        self.text_input.Clear()

    def execute_custom_command(self, command):
        # 这里是您自定义的命令执行逻辑
        # 例如，将命令打印到控制台并在第一个文本框中显示
        print(f"Executing command: {command}")
        self.data_display_1.AppendText(f"Executed: {command}\n")

    def update_display(self, message):
        # 在三个窗口中循环显示数据
        self.data_display_1.AppendText(message + '\n')
        self.data_display_2.AppendText(message + '\n')
        self.data_display_3.AppendText(message + '\n')

    def get_temperature_display(self):
        global data
        # 获取温度数据
        if data:
            temperature = get_temperature()
            if temperature is not None:
                return f"Temp: {temperature:.2f} °C\n"
        return "Temp: N/A\n"


    def get_pressure_display(self):
        # 模拟获取压力数据
        return f"Pressure: {time.time() % 1000:.2f} hPa\n"


    def get_angle_display(self):
        global data
        # 获取三轴姿态角数据吗和
        if data:
            angle_x = get_angle_x()
            if angle_x is not None:
                return f"Angle_X: {angle_x:.2f} °\n"
        return "Angle_X: N/A\n"

    def update_data(self, event):
        download_data(server_url)
        self.data_display_1.SetValue(self.get_temperature_display())
        self.data_display_2.SetValue(self.get_pressure_display())
        self.data_display_3.SetValue(self.get_angle_display())

    def on_exit(self, event):
        self.timer.Stop()
        self.Close(True)
        wx.GetApp().ExitMainLoop()

    def on_button1_click(self, event):
        # 在这里添加按钮1的处理逻辑
        print("TurnON Clicked!")
        self.data_display_1.AppendText("TurnON Clicked!\n")

    def on_button2_click(self, event):
        # 在这里添加按钮2的处理逻辑
        print("Shutdown Clicked!")
        self.data_display_1.AppendText("Shutdown Clicked!\n")

if __name__ == '__main__':
    app = wx.App(False)
    welcome_frame = WelcomeFrame(None)
    app.MainLoop()
