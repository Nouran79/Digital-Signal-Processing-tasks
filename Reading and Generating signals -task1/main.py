import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tkinter
from tkinter import *
from tkinter import ttk

##Test function by TAs
def SignalSamplesAreEqual(file_name,indices,samples):
    expected_indices=[]
    expected_samples=[]
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L=line.strip()
            if len(L.split(' '))==2:
                L=line.split(' ')
                V1=int(L[0])
                V2=float(L[1])
                expected_indices.append(V1)
                expected_samples.append(V2)
                line = f.readline()
            else:
                break

    if len(expected_samples)!=len(samples):
        print("Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(expected_samples)):
        if abs(samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Test case failed, your signal have different values from the expected one")
            return
    print("Test case passed successfully")
def generateSignal():
    x_axis_freq=np.arange(0,float(sampling_frequency.get()),1)

    if SignalType.get()=="sin":
       y = [round((float(Amplitude.get())* np.sin(2*np.pi*(float(analog_frequency.get())/float(sampling_frequency.get()))*i+ float(PhaseShift.get()))),6) for i in x_axis_freq]
    elif SignalType.get()=="cos":
       y = [round((float(Amplitude.get())* np.cos(2*np.pi*(float(analog_frequency.get())/float(sampling_frequency.get()))*i+ float(PhaseShift.get()))),6) for i in x_axis_freq]

    ###  Test
    if SignalType == "sin":
        SignalSamplesAreEqual('SinOutput.txt', x_axis_freq, y)
    elif SignalType == "cos":
        SignalSamplesAreEqual('CosOutput.txt', x_axis_freq, y)

    plt.figure(figsize=(10, 5))
    plt.plot(x_axis_freq[:20],y[:20])
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.show()

#window setup
window = tkinter.Tk()
window.title("Signal Processing task 1")
window.geometry("400x400")
frame = tkinter.Frame()

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

#The label
Title_label = tkinter.Label( frame, text="Generate your signal!",font=("Arial", 15))
Title_label.grid(row=0, column=0, columnspan=2, pady=40)
#labels for inputs
Type_label = tkinter.Label(frame, text='Signal Type', justify="left",font=("Arial", 10))
Amplitude_label = tkinter.Label(frame, text='Amplitude', justify="left",font=("Arial", 10))
PhaseShift_label = tkinter.Label(frame, text='PhaseShift', justify="left",font=("Arial", 10))
analog_frequency_label = tkinter.Label(frame, text='Analog Frequency', justify="left",font=("Arial", 10))
sampling_frequency_label = tkinter.Label(frame, text='Sampling Frequency', justify="left",font=("Arial", 10))
#fields for inputs
# SignalType = tkinter.Entry(frame)
SignalType = ttk.Combobox(frame, values=["sin", "cos"])
SignalType.current(0)
Amplitude = tkinter.Entry(frame)
PhaseShift = tkinter.Entry(frame)
analog_frequency = tkinter.Entry(frame)
sampling_frequency = tkinter.Entry(frame)
# position the widgets label-input 2lines by 2lines
Type_label.grid(row=1, column=0, sticky="w")
SignalType.grid(row=1, column=1, pady=10)
Amplitude_label.grid(row=2, column=0, sticky="w")
Amplitude.grid(row=2, column=1, pady=10)
PhaseShift_label.grid(row=3, column=0, sticky="w")
PhaseShift.grid(row=3, column=1, pady=10)
analog_frequency_label.grid(row=4, column=0, sticky="w")
analog_frequency.grid(row=4, column=1, pady=10)
sampling_frequency_label.grid(row=5, column=0, sticky="w")
sampling_frequency.grid(row=5, column=1, pady=10)
generate = tkinter.Button(frame, text = 'Generate Signal!', command = generateSignal);
generate.grid(row=6,column=0,columnspan=2,pady=20)

frame.pack()
window.mainloop()

###################################### Read signal from file and display it -Nada part start
def read_signal_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        signal_type = int(lines[0].strip())
        is_periodic = int(lines[1].strip())
        N1 = int(lines[2].strip())
        data = []
        for i in range(3, 3 + N1):
            data.append(list(map(float, lines[i].strip().split())))

    return signal_type, is_periodic, N1,data

file_path = 'signal1.txt'

signal_type, is_periodic, N1,  data = read_signal_file(file_path)

df = pd.DataFrame(data, columns=['Index', 'Amplitude'])
print("Signal Type:", signal_type)
print("Is Periodic:", is_periodic)
print("number of samples:", N1 )
print(df.head())
print(df.tail())
print(df.info())

plt.figure(figsize=(10, 5))
plt.plot(df['Index'], df['Amplitude'])
plt.title('Signal in Time Domain ')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.show()

plt.stem(df['Index'], df['Amplitude'])
plt.title('Signal in Time Domain')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.show()
################################################ end of nada part

