import wx
import matplotlib       # Provides the graph figures
matplotlib.use('WXAgg') # matplotlib needs a GUI (layout), we use wxPython

from supermileagebench.GUI import MainFrame
from supermileagebench.DynoEncoder import DynoEncoder
from supermileagebench.Data import AccelerationDatabase

class MainClass(wx.App):
    def OnInit(self):
        self.database = AccelerationDatabase(5000, 100)
        
        self.frame = MainFrame(None, -1,  self.database, 'Position Graph')
        self.frame.Show(True)
        self.frame.Centre()
        
        self.encoder = DynoEncoder()
        self.encoder.addAttachDetachObserver(self)
        self.encoder.addChangeObserver(self)        

        return True

    def startTimer(self):
        self.frame.startTimer()
    
    def updatePosition(self, position, time):
        self.database.addPoint(position, time)
        
        
app = MainClass(0)
app.MainLoop()