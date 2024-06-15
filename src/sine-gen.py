import csv
import math

amplitude = 0.334 * 1.06
frequency = 113.7e6  # 100MHz
sampling_rate = 2e9  # 1GHz
duration = 0.000001# 1 second
#add initial phase
phase = 33.2
#calculate offset time with phase
offset_time = phase / (2 * math.pi * frequency)

num_samples = int(sampling_rate * duration)
time_step = 1 / sampling_rate

with open('sinewaveps.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Time', 'Amplitude'])

    for i in range(num_samples):
        time = i * time_step - offset_time
        amplitude_value = amplitude * math.sin(2 * math.pi * frequency * time)
        writer.writerow([time, amplitude_value])