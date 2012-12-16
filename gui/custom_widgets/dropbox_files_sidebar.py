import wx

class DropboxFilesSidebar(wx.Panel):
    def __init__(self, parent, file_list=[]):
        wx.Panel.__init__(self, parent, 0, style=wx.SIMPLE_BORDER)

        self.hide_button = wx.Button(self, label="Hide")
        self.list_box = wx.CheckListBox(choices=file_list, parent=self)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.hide_button, 1, wx.CENTER)
        self.sizer.Add(self.list_box, 10, wx.GROW)

        self.SetSizer(self.sizer)

        self.hide_button.Bind(wx.EVT_BUTTON, self.on_hide)

    def on_hide(self, event):
        self.Hide()

    def modify_file_list(self, file_list):
        self.list_box = wx.CheckListBox(choices=file_list, parent=self)
        self._redraw()

    def _redraw(self):
        self.Refresh()

