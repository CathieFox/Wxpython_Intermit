import wx

message1 = 'test'

class WelcomeFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(WelcomeFrame, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        welcome_text = wx.StaticText(panel, label="Welcome to the Client Application")
        vbox.Add(welcome_text, flag=wx.ALIGN_CENTER | wx.TOP, border=20)

        self.start_button = self.create_button(panel, "Start", self.on_start)
        vbox.Add(self.start_button, flag=wx.ALIGN_CENTER | wx.ALL, border=20)

        self.exit_button = self.create_button(panel, "Exit", self.on_exit)
        vbox.Add(self.exit_button, flag=wx.ALIGN_CENTER | wx.ALL, border=20)

        panel.SetSizer(vbox)

        self.SetTitle('Welcome')
        self.SetSize((300, 200))
        self.Centre()
        self.Show(True)

    def create_button(self, parent, label, handler):
        button = wx.Button(parent, label=label)
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

    def InitUI(self):
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox = wx.BoxSizer(wx.HORIZONTAL)  # 水平布局

        # 第一个文本框和标题
        box1 = wx.BoxSizer(wx.VERTICAL)
        title1 = wx.StaticText(panel, label="TEMPERATURE")
        self.data_display_1 = self.create_text_ctrl(panel, size=(200, 100))  # 设置大小
        box1.Add(title1, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        box1.Add(self.data_display_1, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
        hbox.Add(box1, proportion=1, flag=wx.EXPAND)

        # 第二个文本框和标题
        box2 = wx.BoxSizer(wx.VERTICAL)
        title2 = wx.StaticText(panel, label="PRESSURE")
        self.data_display_2 = self.create_text_ctrl(panel, size=(200, 100))  # 设置大小
        box2.Add(title2, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        box2.Add(self.data_display_2, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
        hbox.Add(box2, proportion=1, flag=wx.EXPAND)

        # 第三个文本框和标题
        box3 = wx.BoxSizer(wx.VERTICAL)
        title3 = wx.StaticText(panel, label="ANGLE")
        self.data_display_3 = self.create_text_ctrl(panel, size=(200, 100))  # 设置大小
        box3.Add(title3, flag=wx.ALIGN_CENTER | wx.ALL, border=5)
        box3.Add(self.data_display_3, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
        hbox.Add(box3, proportion=1, flag=wx.EXPAND)

        vbox.Add(hbox, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

        input_hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.text_input = wx.TextCtrl(panel, size=(20, 25))  # 设置输入框大小
        input_hbox.Add(self.text_input, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
        self.add_button = self.create_button(panel, "Add Data", self.add_data)
        input_hbox.Add(self.add_button, flag=wx.LEFT | wx.ALL, border=5)

        vbox.Add(input_hbox, flag=wx.EXPAND | wx.ALL, border=5)

        self.exit_button = self.create_button(panel, "Exit", self.on_exit)
        vbox.Add(self.exit_button, flag=wx.ALIGN_CENTER | wx.ALL, border=10)

        panel.SetSizer(vbox)

        self.SetTitle('Client')
        self.SetSize((800, 600))
        self.Centre()
        self.Show(True)
        self.data_display_1.AppendText(message1 + '\n')

    def create_text_ctrl(self, parent, size):
        return wx.TextCtrl(parent, style=wx.TE_MULTILINE | wx.TE_READONLY, size=size)

    def create_button(self, parent, label, handler):
        button = wx.Button(parent, label=label)
        button.Bind(wx.EVT_BUTTON, handler)
        return button

    def add_data(self, event):
        message = self.text_input.GetValue()
        self.update_display(message)
        self.text_input.Clear()
        self.data_display_1.AppendText(message1 + '\n')

    def update_display(self, message):
        # 在三个窗口中循环显示数据
        self.data_display_1.AppendText(message + '\n')
        self.data_display_2.AppendText(message + '\n')
        self.data_display_3.AppendText(message + '\n')

    def on_exit(self, event):
        self.Close(True)
        wx.GetApp().ExitMainLoop()

if __name__ == '__main__':
    app = wx.App(False)
    welcome_frame = WelcomeFrame(None)
    app.MainLoop()
