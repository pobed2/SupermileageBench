import wx
from matplotlib.backends.backend_wx import NavigationToolbar2Wx, _load_bitmap

class CustomNavigationToolbar(NavigationToolbar2Wx):
    def __init_toolbar(self):
        self._parent = self.canvas.GetParent()
        _NTB2_HOME = wx.NewId()
        self._NTB2_BACK = wx.NewId()
        self._NTB2_FORWARD = wx.NewId()
        self._NTB2_PAN = wx.NewId()
        self._NTB2_ZOOM = wx.NewId()
        _NTB2_SAVE = wx.NewId()
        _NTB2_SUBPLOT = wx.NewId()

        self.SetToolBitmapSize(wx.Size(24, 24))

        self.AddSimpleTool(_NTB2_HOME, _load_bitmap('home.png'),
            'Home', 'Reset original view')
        # todo: get new bitmap
        self.AddCheckTool(self._NTB2_PAN, _load_bitmap('move.png'),
            shortHelp='Pan',
            longHelp='Pan with left, zoom with right')
        self.AddCheckTool(self._NTB2_ZOOM, _load_bitmap('zoom_to_rect.png'),
            shortHelp='Zoom', longHelp='Zoom to rectangle')

        self.AddSeparator()
        self.AddSimpleTool(_NTB2_SUBPLOT, _load_bitmap('subplots.png'),
            'Configure subplots', 'Configure subplot parameters')

        self.AddSimpleTool(_NTB2_SAVE, _load_bitmap('filesave.png'),
            'Save', 'Save plot contents to file')

        wx.bind(self, wx.EVT_TOOL, self.home, id=_NTB2_HOME)
        wx.bind(self, wx.EVT_TOOL, self.zoom, id=self._NTB2_ZOOM)
        wx.bind(self, wx.EVT_TOOL, self.pan, id=self._NTB2_PAN)
        wx.bind(self, wx.EVT_TOOL, self.configure_subplot, id=_NTB2_SUBPLOT)
        wx.bind(self, wx.EVT_TOOL, self.save, id=_NTB2_SAVE)

        self.Realize()