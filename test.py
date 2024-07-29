import wx

message1 = 'test'



class Client(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Client, self).__init__(*args, **kwargs)
        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        # 创建三个文本控件来显示数据
        self.data_display_1 = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        vbox.Add(self.data_display_1, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

        self.data_display_2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        vbox.Add(self.data_display_2, proportion=1, flag=wx.EXPAND | wx.ALL, border=2)

        self.data_display_3 = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        vbox.Add(self.data_display_3, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.text_input = wx.TextCtrl(panel)
        hbox.Add(self.text_input, proportion=1, flag=wx.EXPAND)
        send_button = wx.Button(panel, label='Add Data')
        send_button.Bind(wx.EVT_BUTTON, self.add_data)
        hbox.Add(send_button, flag=wx.LEFT, border=5)

        vbox.Add(hbox, flag=wx.EXPAND | wx.ALL, border=5)

        panel.SetSizer(vbox)

        self.SetTitle('Cli')
        self.SetSize((300, 300))
        self.Centre()
        self.Show(True)
        
        self.data_display_1.AppendText(message1 + '\n')

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

if __name__ == '__main__':
    app = wx.App(False)
    Client(None)
    app.MainLoop()