import sys
import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc
import PyQt6.QtGui as qtg
import numpy as np
import pyqtgraph as pg
from scipy.signal import butter, lfilter, lfilter_zi
import csv

# Define the colors for the subplots
plot_color = [
    "#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#00FFFF", "#FF00FF", "#C0C0C0", "#808080",
    "#800000", "#808000", "#008000", "#800080", "#008080", "#000080", "#FFA500", "#A52A2A",
    "#FFFFF0", "#F0FFF0", "#F0FFFF", "#F5F5DC", "#F5DEB3", "#FDF5E6", "#FFF0F5", "#FAEBD7",
    "#7CFC00", "#F0E68C", "#ADD8E6", "#E0FFFF", "#90EE90", "#D3D3D3", "#FFB6C1", "#FFA07A",
    "#20B2AA", "#87CEFA", "#778899", "#B0C4DE", "#FFFFE0", "#00FF7F", "#32CD32", "#FAF0E6",
    "#800000", "#66CDAA", "#0000CD", "#BA55D3", "#9370DB", "#3CB371", "#7B68EE", "#00FA9A",
    "#48D1CC", "#C71585", "#191970", "#F5FFFA", "#FFE4E1", "#FFE4B5", "#FFDEAD", "#000080",
    "#FDF5E6", "#808000", "#6B8E23", "#FFA500", "#FF4500", "#DA70D6", "#EEE8AA", "#98FB98",
    "#AFEEEE", "#DB7093", "#FFEFD5", "#FFDAB9", "#CD853F", "#FFC0CB", "#DDA0DD", "#B0E0E6"
]

emotion_color = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF']

label1 = ['AF3', 'F7', 'F3', 'FC5', 'T7', 'P7', 'O1', 'O2', 'P8', 'T8', 'FC6', 'F4', 'F8', 'AF4']
with open('raw.csv', newline='') as csvfile:
    data1 = list(csv.reader(csvfile))

label2 = ['FC5', 'FC3', 'FC1', 'FCZ', 'FC2', 'FC4', 'FC6', 'C5', 'C3', 'C1', 'CZ', 'C2', 'C4', 'C6', 'CP5', 'CP3', 'CP1', 'CPZ', 'CP2', 'CP4', 'CP6', 'FP1', 'FPZ', 'FP2', 'AF7', 'AF3', 'AFZ', 'AF4', 'AF8', 'F7', 'F5', 'F3', 'F1', 'FZ', 'F2', 'F4', 'F6', 'F8', 'FT7', 'FT8', 'T7', 'T8', 'T9', 'T10', 'TP7', 'TP8', 'P7', 'P5', 'P3', 'P1', 'PZ', 'P2', 'P4', 'P6', 'P8', 'PO7', 'PO3', 'POZ', 'PO4', 'PO8', 'O1', 'OZ', 'O2', 'IZ']
with open('raw2.csv', newline='') as csvfile:
    data2 = list(csv.reader(csvfile))
