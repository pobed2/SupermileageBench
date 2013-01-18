#coding: utf-8

import wx

class TopFrame(wx.Frame):
    def __init__(self, controller, parent=None, id=-1, title=""):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition)
        self.controller = controller
        self._createMenu()
        self.Maximize()

    # ------------------ Top Menu

    def _createMenu(self):
        self.menu_bar = wx.MenuBar()
        self.menu_file = wx.Menu()

        menu_properties = self.menu_file.Append(-1, u"Propriétés\tCtrl+P", u"Propriétés")
        self.Bind(wx.EVT_MENU, self.controller.on_properties_click, menu_properties)

        menu_injection_table = self.menu_file.Append(-1, u"Table d'injection\tCtrl+T", u"Table d'injection")
        self.Bind(wx.EVT_MENU, self.controller.on_injection_table_menu_click, menu_injection_table)

        self.menu_bar.Append(self.menu_file, "&File")
        self.SetMenuBar(self.menu_bar)

