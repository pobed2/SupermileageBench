#coding: utf-8

import wx
from configuration.properties_parser import PropertiesParser
from gui.custom_widgets.custom_check_list_box import CustomCheckListBox

class PropertiesDialog(wx.Dialog):
    def __init__(self, controller):
        super(PropertiesDialog, self).__init__(parent=None, title=u"Propriétés")
        self.controller = controller
        self.properties_parser = PropertiesParser()
        self.inertia_ctrl, self.friction_ctrl, self.real_time_checkboxes, self.post_processing_checkboxes = self._init_ui()
        self.Center()

    def _init_ui(self):
        dialog_panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        properties_sizer = wx.BoxSizer(wx.HORIZONTAL)

        #Constants
        constant_box = wx.StaticBox(dialog_panel, label=u'Constantes')
        constant_box_sizer = wx.StaticBoxSizer(constant_box, orient=wx.VERTICAL)
        fgs = wx.FlexGridSizer(4, 1, 9, 25)
        inertia = wx.StaticText(self, label="Inertie")
        friction = wx.StaticText(self, label="Constante de friction")
        inertia_text_ctrl = wx.TextCtrl(self)
        inertia_text_ctrl.AppendText(self.properties_parser.get_property("Inertia"))
        friction_text_ctrl = wx.TextCtrl(self)
        friction_text_ctrl.AppendText(self.properties_parser.get_property("Friction"))
        fgs.AddMany([(inertia), (inertia_text_ctrl, 1, wx.EXPAND), (friction),
                     (friction_text_ctrl, 1, wx.EXPAND)])
        constant_box_sizer.Add(fgs)

        #Real-time plots properties
        real_time_plots_box = wx.StaticBox(dialog_panel, label=u'Temps-réel')
        real_time_box_sizer = wx.StaticBoxSizer(real_time_plots_box, orient=wx.VERTICAL)
        real_time_checkboxes = CustomCheckListBox(self, [u"Position", u"Vitesse", u"Accélération", u"Torque"],
            self.properties_parser.get_property("Real-Time Plots"))
        real_time_box_sizer.Add(real_time_checkboxes)

        #Post-processing plots properties
        post_processing_plots_box = wx.StaticBox(dialog_panel, label=u'Post-traitement')
        post_processing_box_sizer = wx.StaticBoxSizer(post_processing_plots_box, orient=wx.VERTICAL)
        post_processing_checkboxes = CustomCheckListBox(self, [u"Torque", u"Puissance"],
            self.properties_parser.get_property("Post-Processing Plots"))
        post_processing_box_sizer.Add(post_processing_checkboxes)

        properties_sizer.Add(constant_box_sizer)
        properties_sizer.Add(real_time_box_sizer)
        properties_sizer.Add(post_processing_box_sizer)

        dialog_panel.SetSizer(properties_sizer)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        okButton = wx.Button(self, label='Ok')
        closeButton = wx.Button(self, label='Close')
        hbox2.Add(okButton)
        hbox2.Add(closeButton, flag=wx.LEFT, border=5)

        vbox.Add(dialog_panel, proportion=1,
            flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(hbox2,
            flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)

        self.SetSizer(vbox)

        okButton.Bind(wx.EVT_BUTTON, self.OnClose)
        closeButton.Bind(wx.EVT_BUTTON, self.OnClose)

        return inertia_text_ctrl, friction_text_ctrl, real_time_checkboxes, post_processing_checkboxes

    def OnClose(self, e):
        self.controller.save_properties(self.inertia_ctrl.GetValue(), self.friction_ctrl.GetValue(),
            self.real_time_checkboxes.get_checked(), self.post_processing_checkboxes.get_checked())
        self.Destroy()