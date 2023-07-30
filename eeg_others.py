from imports import *

def restart_configuration(self):
    self.stop_state = True

    # Closing and removing plot widgets
    for plot_widget in self.plot_widgets:
        self.graph_layout.removeWidget(plot_widget)
        plot_widget.close()

    # Removing widgets from the graph layout
    while self.graph_layout.count():
        item = self.graph_layout.takeAt(0)
        widget = item.widget()
        if widget is not None:
            widget.setParent(None)

    self.plot_widgets = []
