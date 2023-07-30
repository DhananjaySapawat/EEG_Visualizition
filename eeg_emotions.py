from imports import *

def emotions_plot_graph(self, layout):
    if self.stop_state == False:
        return
    self.stop_state = False

    self.emotion_labels = ["Enagement", "Excitement", "Enjoyment", "Boredom", "Confusion", "Frustration"]
    self.sampling_rate = 128
    graph_data = np.array(data2, dtype=float)

    self.plot_widgets = []
    self.labels = []
    for i in range(len(self.emotion_labels)):
        # Create a new PlotWidget
        plot_widget = pg.PlotWidget()
        plot_widget.setMouseEnabled(x=False, y=False)

        # Disable auto-ranging
        plot_widget.plotItem.autoRangeEnabled = False
        self.plot_widgets.append(plot_widget)
        self.graph_layout.addWidget(plot_widget, i, 1)

        # Create a new QLabel for the emotion label
        label = qtw.QLabel(self.emotion_labels[i])
        label.setStyleSheet(f"color: {emotion_color[i]};")  

        self.labels.append(label)
        self.graph_layout.addWidget(label, i, 0)

    layout.addLayout(self.graph_layout)

    # Start the event loop to update the plots
    self.emotions_update_plots(graph_data, 0)

def emotions_update_plots(self, graph_data, start):
    if self.stop_state:
        return

    if len(graph_data) <= start:
        self.restart_configuration()
        return

    end = start + self.sampling_rate
    data = graph_data[start:end].transpose()
    self.raw = data
    self.alpha = [self.frequency_filter(d, "Alpha") for d in data]
    self.beta  = [self.frequency_filter(d, "Beta") for d in data]
    self.gamma = [self.frequency_filter(d, "Gamma") for d in data]
    self.data_mapping = {
        "raw": self.raw,
        "alpha": self.alpha,
        "beta": self.beta,
        "gamma": self.gamma
    }

    for i in range(0, len(self.emotion_labels)):
        self.plot_widgets[i].clear()
        emotion_data = self.get_emotion_data(self.emotion_labels[i])
        self.plot_widgets[i].plot(emotion_data, pen = pg.mkPen(color=emotion_color[i], width=1.8)) 
        self.plot_widgets[i].getPlotItem().hideAxis('left')
        axis = self.plot_widgets[i].getAxis("bottom")
        axis.setRange(0, self.sampling_rate)

    # Call the update_plots function again after 100 milliseconds
    qtc.QTimer.singleShot(100, lambda: self.emotions_update_plots(graph_data, end))

def get_emotion_data(self, emotion_type):

    if emotion_type == "Enagement":
        n = self.get_region_mean("beta","O") + self.get_region_mean("beta","F")
        d = self.get_region_mean("gamma","O") + self.get_region_mean("alpha","O")

    elif emotion_type == "Excitement":
        n = self.get_region_mean("beta","O") + self.get_region_mean("beta","F")
        n = n + self.get_region_mean("alpha","O") + self.get_region_mean("alpha","F")
        n = n + self.get_region_mean("gamma","O") + self.get_region_mean("gamma","F")
        d = 1

    elif emotion_type == "Enjoyment":
        n = self.get_region_mean("beta","O") + self.get_region_mean("beta","F")
        d = self.get_region_mean("alpha","O") + self.get_region_mean("alpha","F")
        d = d + self.get_region_mean("gamma","O") + self.get_region_mean("gamma","F")

    elif emotion_type == "Boredom":
        n = self.get_region_mean("alpha","F")
        d = self.get_region_mean("beta","O") + self.get_region_mean("beta","F")

    elif emotion_type == "Confusion":
        n = self.get_region_mean("beta","O") + self.get_region_mean("beta","F")
        n = n + self.get_region_mean("gamma","O") + self.get_region_mean("gamma","F")
        d = 1

    elif emotion_type == "Frustration":
        n = self.get_region_mean("gamma","F") + self.get_region_mean("beta","F")
        n = n + self.get_region_mean("alpha","O") 
        d = self.get_region_mean("gamma","O") + self.get_region_mean("beta","O")

    else:
        n = self.raw[0]
        d = 1 

    return n / d
def get_region_mean(self, data_frequency, brain_region):

    data_frequency = data_frequency.lower()
    if data_frequency not in ["raw", "alpha", "beta", "gamma"]:
        print("Error: unknown frequency")
        return 
        
    brain_region = brain_region.lower()
    if brain_region not in ["t","o","p","f","af","fc","all"]:
        print("Error: unknown brain region")
        return 

    wave = self.data_mapping.get(data_frequency)
    mean_data = np.zeros(len(wave[0]), dtype = float)
    total = 0.000000 

    for i in range(0, len(self.electrode_labels)):
        if self.is_brain_region(brain_region, self.electrode_labels[i]) == False:
            continue
        
        mean_data = np.add(mean_data, np.absolute(wave[i]))
        total = total + 1

    return mean_data / total