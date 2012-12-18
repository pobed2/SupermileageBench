import wx
from gui.mvc_helpers.observable import Observable
from gui.mvc_helpers.observable_events import FileCheckedObservableEvent, FileUncheckedObservableEvent

class DropboxFilesSidebar(wx.Panel, Observable):
    def __init__(self, parent, file_list=[]):
        wx.Panel.__init__(self, parent, 0, style=wx.SIMPLE_BORDER)
        Observable.__init__(self)

        self.file_list = file_list
        self.hide_button = wx.Button(self, label="Hide")
        self.list_box = wx.CheckListBox(choices=file_list, parent=self)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.hide_button, 1, wx.CENTER)
        self.sizer.Add(self.list_box, 10, wx.GROW)

        self.SetSizer(self.sizer)

        self.hide_button.Bind(wx.EVT_BUTTON, self.on_hide)

        self.list_box.Bind(wx.EVT_CHECKLISTBOX, self.on_check_or_uncheck)

    def on_hide(self, event):
        self.Hide()

    def on_check_or_uncheck(self, event):
        filename = self.file_list[event.GetSelection()]

        if self.list_box.IsChecked(event.GetSelection()):
            self.notify_observers(FileCheckedObservableEvent(filename))
        else:
            self.notify_observers(FileUncheckedObservableEvent(filename))




