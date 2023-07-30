from imports import *

def plot_graph(self, dropdown1, dropdown2, checkbox, layout):
    if self.stop_state == False:
        return

    self.stop_state = False

    self.frequency_band = dropdown1.currentText()
    self.brain_region = dropdown2.currentText()
    self.bin = checkbox.isChecked()

    self.sampling_rate = 128
    graph_data = np.array(self.eeg_data, dtype=float).transpose()

    # Create 14 plot widgets and labels
    self.plot_widgets = []
    self.labels = []
    for i in range(len(self.electrode_labels)):
        if self.is_brain_region(self.brain_region, self.electrode_labels[i]) == False:
            continue

        plot_widget = pg.PlotWidget()
        plot_widget.setMouseEnabled(x=False, y=False)

        # Disable auto-ranging
        plot_widget.plotItem.autoRangeEnabled = False
        self.plot_widgets.append(plot_widget)
        self.graph_layout.addWidget(plot_widget, i, 1)

        label = qtw.QLabel(self.electrode_labels[i])
        label.setStyleSheet(f"color: {plot_color[i]};")  

        self.labels.append(label)
        self.graph_layout.addWidget(label, i, 0)

    layout.addLayout(self.graph_layout)

    # Start the event loop to update the plots
    self.update_plots(graph_data, 0)


def update_plots(self, graph_data, start):
    if self.stop_state:
        return

    if len(graph_data[0]) <= start:
        self.restart_configuration()
        return

    end = start + self.sampling_rate
    i = 0
    k = -1
    while i < len(self.plot_widgets):
        k += 1
        if self.is_brain_region(self.brain_region, self.electrode_labels[k]) == False:
            continue

        self.plot_widgets[i].clear()

        # get the graph data
        data = graph_data[i][start:end]
        data = self.frequency_filter(data, self.frequency_band)
        if self.bin:
            data = self.convert_data(data)

        self.plot_widgets[i].plot(data, pen = pg.mkPen(color=plot_color[i], width=1.8)) 
        self.plot_widgets[i].getPlotItem().hideAxis('left')
        axis = self.plot_widgets[i].getAxis("bottom")
        axis.setRange(0, self.sampling_rate)

        i += 1

    # Call the update_plots function again after 100 milliseconds
    qtc.QTimer.singleShot(100, lambda: self.update_plots(graph_data, end))


def convert_data(self, data):
    result = [1]
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            result.append(1)  # Element is increasing
        elif data[i] < data[i - 1]:
            result.append(0)  # Element is decreasing
        else:
            result.append(result[-1])  # Same as the previous element
    return result


def is_brain_region(self, brain_region1, brain_region2):
    brain_region2 = ''.join([i for i in brain_region2 if not i.isdigit()])
    return brain_region1.lower() == "all" or brain_region1.lower() == brain_region2.lower()


def frequency_filter(self, data, frequency_band):
    if frequency_band == "Alpha":
        return self.butter_bandpass_filter(data, 8, 12, self.sampling_rate)
    if frequency_band == "Beta":
        return self.butter_bandpass_filter(data, 12, 33, self.sampling_rate)
    if frequency_band == "Gamma":
        return self.butter_bandpass_filter(data, 33, 63, self.sampling_rate)
    else:
        return data


def butter_bandpass_filter(self, data, lowcut, highcut, fs, order=5):
    b, a = self.butter_bandpass(lowcut, highcut, fs, order=order)
    zi = lfilter_zi(b, a) * data[0]
    y, _ = lfilter(b, a, data, zi=zi)
    return y


def butter_bandpass(self, lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a
