from supermileagebench.gui.windows.bench_panel import BenchPanel

class PostTreatmentPanel(BenchPanel):
    def __init__(self, sub_data_plots, parent, width=1280, height=720, dpi=100):
        super(PostTreatmentPanel, self).__init__(sub_data_plots, parent, width, height, dpi)