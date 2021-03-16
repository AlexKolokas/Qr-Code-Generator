import wx
import qrcode

class MyFrame(wx.Frame):
    def __init__(self):
        # lets put some text
        super().__init__(parent=None,title='QrCode Generator') #window title
        panel = wx.Panel(self)
        my_sizer=wx.BoxSizer(wx.VERTICAL)
        txt1 = wx.StaticText(panel,0, "Qr Code Text or Link Field")
        my_sizer.Add(txt1,0, wx.ALL | wx.CENTER, 5)  #vertically size the text
        self.text_ctrl = wx.TextCtrl(panel) #Text box for qr text
        self.text_ctrl2 = wx.TextCtrl(panel) # Text box
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5) #size the first textbox
        txt2 = wx.StaticText(panel,0, "File Name Field")
        my_sizer.Add(txt2,0, wx.ALL | wx.CENTER, 5)#vertically size the text
        my_sizer.Add(self.text_ctrl2, 0, wx.ALL | wx.EXPAND, 5)#size the seccond Text
        my_btn2 = wx.Button(panel, label='Generate QR Code') #BUtton to add file name
        my_btn2.Bind(wx.EVT_BUTTON, self.on_press)#add on press event on second button
        my_sizer.Add(my_btn2, 0, wx.ALL | wx.CENTER, 5)#size the seccond button
        panel.SetSizer(my_sizer)
        self.Show()

    def on_press(self, event):
        value = self.text_ctrl.GetValue() #VALUE IS THE TEXT THAT USER GIVES
        value2 = self.text_ctrl2.GetValue() #VALUE2 IS THE NAME OF THE FILE
        #------you must write all ----------
        while (not value):
            #print('Give QR Code text')
            text_ctrl2.disable()
            my_btn2.disable()
        while (not value2):
            #print('Give File Name')
            my_btn2.disable()
    #-------------------------------------------------------------------------------------------------------------------------
        qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5,
        )
        qr.add_data(value)
        qr.make(fit=True)
            #colors for the qrcode
        img = qr.make_image(fill_color='black', back_color='white')
            #adds a .png to the saving name (so the qrcode is saved as png)
        inputfilenamefinal=value2+'.png'
        img.save(inputfilenamefinal) #save the qr code as png



if __name__ == '__main__':
    app=wx.App()
    frame=MyFrame()
    app.MainLoop()
