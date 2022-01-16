import wx

class WxUI(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="MatPy")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)

        self.text_ctrl = wx.TextCtrl(panel, pos=(5,5))
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)
           
        my_btn = wx.Button(panel, label="Press Me", pos=(5,55))
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(my_sizer)

        self.Show()

    def on_press(self, event):
        value = self.text_ctrl.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print(f'You type: "{value}"')