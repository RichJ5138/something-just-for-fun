import wx
app=wx.App()
class Myframe(wx.Frame):
    def __init__(self):
        super().__init__(None,title='Quastion',pos=(500,500),size=(400,200))
        panel=wx.Panel(parent=self)
        self.statictext=wx.StaticText(parent=panel,label='FUCK YOU!!!')
        ButtonYes=wx.Button(parent=panel,label='THANK YOU!!!')
        ButtonNo=wx.Button(parent=panel,label='FUCK YOU TOO!!!')
        self.Bind(wx.EVT_BUTTON,self.ChooseYes,ButtonYes)
        self.Bind(wx.EVT_BUTTON,self.ChooseNo,ButtonNo)
        Box=wx.BoxSizer(wx.HORIZONTAL)
        Box.Add(ButtonYes,proportion=1,flag=wx.ALIGN_CENTER_VERTICAL,border=10)
        Box.Add(ButtonNo,proportion=1,flag=wx.ALIGN_CENTER_VERTICAL,border=10)
        BoxAll=wx.BoxSizer(wx.VERTICAL)
        BoxAll.Add(self.statictext,proportion=1,flag=wx.ALIGN_CENTER_HORIZONTAL,border=10)
        BoxAll.Add(Box,proportion=10,flag=wx.ALIGN_CENTER_HORIZONTAL,border=10)
        panel.SetSizer(BoxAll)
    def ChooseYes(self,event):
        self.statictext.SetLabelText('YOU ARE STUPID TO CHOOSE IT!!!')
    def ChooseNo(self,event):
        self.statictext.SetLabelText('YOU ARE SHIT!!!')
frm=Myframe()
frm.Show()
app.MainLoop()