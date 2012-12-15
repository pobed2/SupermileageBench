import wx

class FilterTestingFrame(wx.Frame):
    def __init__(self, parent=None, id=-1, title="", width=1280, height=720):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, (width, height))
