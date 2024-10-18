import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


##SignalSamplesAreEqual function is made by TAs
def SignalSamplesAreEqual(file_name, indices, samples):
    expected_indices = []
    expected_samples = []
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L = line.strip()
            if len(L.split(' ')) == 2:
                L = line.split(' ')
                V1 = int(L[0])
                V2 = float(L[1])
                expected_indices.append(V1)
                expected_samples.append(V2)
                line = f.readline()
            else:
                break

    if len(expected_samples) != len(samples):
        print("Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(expected_samples)):
        if abs(samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Test case failed, your signal have different values from the expected one")
            return
    print("Test case passed successfully")
def testAndPlot(signalType,xAxis,yAxis):
    print("Test case failed, your signal have different length from the expected one")

    if signalType == "sin":
        SignalSamplesAreEqual('SinOutput.txt', xAxis, yAxis)
    elif signalType == "cos":
        SignalSamplesAreEqual('CosOutput.txt', xAxis, yAxis)

    plt.figure(figsize=(10, 5))
    plt.plot(xAxis[:20], yAxis[:20])
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.show()
def read_signal_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        signal_type = int(lines[0].strip())
        is_periodic = int(lines[1].strip())
        N1 = int(lines[2].strip())
        data = []
        for i in range(3, 3 + N1):
            data.append(list(map(float, lines[i].strip().split())))
    return signal_type, is_periodic, N1, data
def Buton():
    file_path = filedialog.askopenfilename(title="Select Signal File",
                                           filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))

    if file_path:
        signal_type, is_periodic, N1, data = read_signal_file(file_path)

        df = pd.DataFrame(data, columns=['Index', 'Amplitude'])

        signal_type_text = 'Discrete' if signal_type == 0 else 'Continuous'
        print("Signal Type:", signal_type_text)
        print("Is Periodic:", 'Yes' if is_periodic else 'No')
        print("Number of samples:", N1)
        print(df.head())

        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)  # row 1, col 2 index 1
        plt.plot(df['Index'], df['Amplitude'], label="Signal Data")
        # plt.title(f'Analog Signal in Time Domain ({signal_type_text})')
        plt.title(f'Analog Signal in Time Domain')
        plt.xlabel('Sample Index')
        plt.ylabel('Amplitude')

        if signal_type == 0:
            plt.subplot(1, 2, 2)  # row 1, col 2 index 1
            plt.stem(df['Index'], df['Amplitude'])
            plt.title('Digital Signal in Time Domain')
            plt.xlabel('Sample Index')
            plt.ylabel('Amplitude')
            plt.show()
def generateSignal():
    x_axis_freq = np.arange(0, float(sampling_frequency.get()), 1)
    print("Test  failed, your signal have different length from the expected one")
    print(SignalType_box.get()+"hkhk")
    print(sampling_frequency.get() + "hkhk")
    if SignalType_box.get() == "sin":
        y = [round((float(Amplitude.get()) * np.sin(
            2 * np.pi * (float(analog_frequency.get()) / float(sampling_frequency.get())) * i + float(
                PhaseShift.get()))), 6) for i in x_axis_freq]
        print("Test case failed, your signal have different length from the expected one")

        testAndPlot("sin", x_axis_freq, y)
    elif SignalType_box.get() == "cos":
        y = [round((float(Amplitude.get()) * np.cos(
            2 * np.pi * (float(analog_frequency.get()) / float(sampling_frequency.get())) * i + float(
                PhaseShift.get()))), 6) for i in x_axis_freq]
        print("Test case failed, your signal have different length from the expected one")

        testAndPlot("cos", x_axis_freq, y)
# window setup
window = tkinter.Tk()
window.title("Signal Processing task 1")
window.geometry("600x600")
frame = tkinter.Frame(window, highlightbackground="gray", highlightthickness=2)

## adding menu
menubar = Menu(window)
window.config(menu=menubar)
file_menu = Menu(
    menubar,
    tearoff=0
)
file_menu.add_command(label='Sin wave')
file_menu.add_separator()
file_menu.add_command(label='Cos wave')
menubar.add_cascade(
    label="Signal generation",
    menu=file_menu
)

# The label
Title_label = tkinter.Label(frame, text="Generate your signal!", font=("Arial", 15), width=38)
Title_label.grid(row=0, column=0, columnspan=2, pady=40)
# labels for inputs
Type_label = tkinter.Label(frame, text='Signal Type', justify="left", font=("Arial", 10), padx=20)
Amplitude_label = tkinter.Label(frame, text='Amplitude', justify="left", font=("Arial", 10), padx=20)
PhaseShift_label = tkinter.Label(frame, text='PhaseShift', justify="left", font=("Arial", 10), padx=20)
analog_frequency_label = tkinter.Label(frame, text='Analog Frequency', justify="left", font=("Arial", 10), padx=20)
sampling_frequency_label = tkinter.Label(frame, text='Sampling Frequency', justify="left", font=("Arial", 10), padx=20)
# fields for inputs
# SignalType = tkinter.Entry(frame)
SignalType_box = ttk.Combobox(frame, values=["sin", "cos"])
Amplitude = tkinter.Entry(frame)
PhaseShift = tkinter.Entry(frame)
analog_frequency = tkinter.Entry(frame)
sampling_frequency = tkinter.Entry(frame)

# position the widgets label-input 2lines by 2lines
Type_label.grid(row=1, column=0, sticky="w")
SignalType_box.grid(row=1, column=1, pady=10)
Amplitude_label.grid(row=2, column=0, sticky="w")
Amplitude.grid(row=2, column=1, pady=10)
PhaseShift_label.grid(row=3, column=0, sticky="w")
PhaseShift.grid(row=3, column=1, pady=10)
analog_frequency_label.grid(row=4, column=0, sticky="w")
analog_frequency.grid(row=4, column=1, pady=10)
sampling_frequency_label.grid(row=5, column=0, sticky="w")
sampling_frequency.grid(row=5, column=1, pady=10)
generate = tkinter.Button(frame, text='Generate Signal!', command=generateSignal);
generate.grid(row=6, column=0, padx=0, pady=20)

######for reading file
SignalType = tkinter.Entry(frame)
btn = tkinter.Button(frame, text='Load  Signal from device', bg='gray', command=Buton)
btn.grid(row=6, column=1, padx=10, pady=10)

frame.pack(padx=40, pady=40)
window.mainloop()
