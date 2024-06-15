import csv
import numpy as np

def calculate_frequency(csv_file):
    # Read the CSV file
    data = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        #skip the header row if present
        next(reader)
        for row in reader:
            data.append(float(row[0]))

    # Calculate the frequency using Fast Fourier Transform (FFT)
    fft_result = np.fft.fft(data)
    frequency = np.argmax(np.abs(fft_result))

    return frequency

# Replace 'path/to/your/csv/file.csv' with the actual path to your CSV file
csv_file = 'C:/Users/juanc/Desktop/repos/dibujo-kit/sinewave.csv'
frequency = calculate_frequency(csv_file)
print(f"The frequency of the sinusoidal data is: {frequency} Hz")