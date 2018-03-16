import wx
class TestFrame(wx.Frame):
  def __init__(self, parent, title):
    wx.Frame.__init__(self, parent, title=title, size=(500,300))
    self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
if __name__ == '__main__':
  app = wx.App()
  frame = TestFrame(None, 'Editor de Texto')
  frame.Center()
  frame.Show()
  app.MainLoop()

#asd