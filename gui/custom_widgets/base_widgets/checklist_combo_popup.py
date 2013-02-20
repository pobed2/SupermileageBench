from wx.combo import ComboPopup
from gui.custom_widgets.base_widgets.custom_check_list_box import CustomCheckListBox
from gui.mvc_helpers.observable import Observable
from gui.mvc_helpers.observable_events import   PlotTypesChangedObservableEvent
from gui.mvc_helpers.observer import Observer

class CheckListComboPopup(ComboPopup, Observable, Observer):
    def __init__(self, list_of_items, chosen_items):
        super(CheckListComboPopup, self).__init__()
        Observable.__init__(self)
        self.list_of_items = list_of_items
        self.chosen_items = chosen_items

    def Create(self, parent):
        self.checklistbox = CustomCheckListBox(parent, choices=self.list_of_items, checked=self.chosen_items,
            observer=self)
        self.checklistbox.add_observer(self)

    def manage_checkbox_event(self):
        list_of_plots = self.checklistbox.get_checked()
        self.notify_observers(PlotTypesChangedObservableEvent(list_of_plots))