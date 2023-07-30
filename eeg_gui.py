from imports import * 
from eeg_channel import * 
from eeg_emotions import * 
from eeg_others import *  
from style import *

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EEG Simulator")
        self.setGeometry(250, 100, 1000, 666)
        self.stop_state = True 
        self.electrode_labels = label2
        self.eeg_data = data2
        # Create a central widget and a layout
        central_widget = qtw.QWidget(self)
        layout = qtw.QVBoxLayout(central_widget)

        # Create a horizontal layout for the items
        items_layout = qtw.QHBoxLayout()

        # Create the dropdown menus
        dropdown1 = qtw.QComboBox()
        dropdown1.addItems(["Raw", "Alpha", "Beta", "Gamma"])
        dropdown1.setFixedWidth(0)
        dropdown1.setCursor(qtg.QCursor(qtc.Qt.CursorShape.PointingHandCursor)) 
        items_layout.addWidget(dropdown1)

        dropdown2 = qtw.QComboBox()
        drop_down_options = [*set(["".join(filter(str.isalpha, j)).upper() for j in self.electrode_labels])]
        drop_down_options.sort()
        drop_down_options = ["ALL"] + drop_down_options
        dropdown2.addItems(drop_down_options)
        dropdown2.setFixedWidth(0)
        dropdown2.setCursor(qtg.QCursor(qtc.Qt.CursorShape.PointingHandCursor)) 
        items_layout.addWidget(dropdown2)

        # Create the checkbox
        checkbox = qtw.QCheckBox("Binary")
        checkbox.setCursor(qtg.QCursor(qtc.Qt.CursorShape.PointingHandCursor)) 
        items_layout.addWidget(checkbox)

        # Add the items layout to the main layout
        layout.addLayout(items_layout)

        # Create a horizontal layout for the button
        button_layout = qtw.QHBoxLayout()

        # Create the button
        button = qtw.QPushButton("Plot")
        button.clicked.connect(lambda: self.plot_graph(dropdown1, dropdown2, checkbox, layout))
        button.setCursor(qtg.QCursor(qtc.Qt.CursorShape.PointingHandCursor)) 
        button_layout.addWidget(button)

        # Create the button 2
        button2 = qtw.QPushButton("Emotions")
        button2.clicked.connect(lambda: self.emotions_plot_graph(layout))
        button2.setCursor(qtg.QCursor(qtc.Qt.CursorShape.PointingHandCursor)) 
        button_layout.addWidget(button2)

        # Create the restart button
        restart_button = qtw.QPushButton("Restart")
        restart_button.clicked.connect(self.restart_configuration)
        restart_button.setCursor(qtg.QCursor(qtc.Qt.CursorShape.PointingHandCursor)) 
        button_layout.addWidget(restart_button)

        # Add the button layout to the main layout
        layout.addLayout(button_layout)

        self.graph_layout = qtw.QGridLayout()
        self.graph_layout.setSpacing(0)

        # Create a scroll area and set the graph layout as its widget
        self.scroll_area = qtw.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        scroll_widget = qtw.QWidget()
        
        scroll_widget.setLayout(self.graph_layout)
        self.scroll_area.setWidget(scroll_widget)
        self.scroll_area.setFixedHeight(600)  # Set the minimum height of the scroll area
        layout.addWidget(self.scroll_area)

        # Add a vertical spacer item to align the layout at the top
        layout.addStretch(1)
        self.setCentralWidget(central_widget)

        # Connect the resize event of the window to a custom slot
        self.resizeEvent = self.onResize

    def onResize(self, event):
        # Retrieve the current window height
        window_height = self.height() - 684
        self.scroll_area.setFixedHeight(600 + window_height)  # Set the minimum height of the scroll area

# plot functions 
MainWindow.plot_graph = plot_graph
MainWindow.update_plots = update_plots
MainWindow.convert_data = convert_data
MainWindow.is_brain_region = is_brain_region
MainWindow.frequency_filter = frequency_filter
MainWindow.butter_bandpass_filter = butter_bandpass_filter
MainWindow.butter_bandpass = butter_bandpass

# emotions functions
MainWindow.emotions_plot_graph = emotions_plot_graph
MainWindow.emotions_update_plots = emotions_update_plots
MainWindow.get_emotion_data = get_emotion_data
MainWindow.get_region_mean = get_region_mean

# other functions 
MainWindow.restart_configuration = restart_configuration

# styling 

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    app.setStyleSheet(style_sheet)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
