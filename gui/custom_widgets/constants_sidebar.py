import wx

class ConstantsSidebar(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, style=wx.SIMPLE_BORDER)

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        fgs = wx.FlexGridSizer(4, 1, 9, 25)

        inertia = wx.StaticText(self, label="Inertie")
        friction = wx.StaticText(self, label="Constante de friction")

        inertia_text_ctrl = wx.TextCtrl(self)
        friction_text_ctrl = wx.TextCtrl(self)

        fgs.AddMany([(inertia), (inertia_text_ctrl, 1, wx.EXPAND), (friction),
                     (friction_text_ctrl, 1, wx.EXPAND)])

        hbox.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
        self.SetSizer(hbox)