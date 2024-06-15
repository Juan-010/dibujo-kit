import csv

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Path to the CSV file
csv_file = 'C:/Users/juanc/Desktop/repos/dibujo-kit/dat/clapp.csv'

# Lists to store the data
x_data = []
y_data = []

# Read data from the CSV file
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row if present
    for row in reader:
        x_data.append(float(row[0]))
        y_data.append(float(row[1]))

# Plot the data
#set min x value
#add grid with dotted line
plt.grid(True, linestyle=':')
plt.xlim(0.2,0.25)
#plt.ylim(0.2e-6,0.25e-6)
#dont interpolate data, only samples    
#plt.plot(x_data, y_data, marker='.', linestyle='None')
plt.plot(x_data, y_data)
#plot dotted line at 0.36V
plt.axhline(y=0.36, color='r', linestyle='--')

#plot vline at 0.22us and 0.2379us
#list possible matplotlib colors in comment below
#['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
plt.axvline(x=0.22, color='g', linestyle='--')
plt.axvline(x=0.22879, color='m', linestyle='--')

#add markers values to legend
plt.legend(['Señal','m1 = 0.36V','m2 = 0.22us','m3 = 0.22879us'], loc='upper right')
#add padding below xlabel
#remove scale at the bottom
# change 1e-6 to 1us
plt.subplots_adjust(bottom=0.2)
plt.xlabel('time[us]\nFrequency: 113.7MHz')
plt.ylabel('amplitude[V]')
plt.title('Oscilador Clapp')
plt.show()
#plt.savefig('C:/Users/juanc/Desktop/repos/dibujo-kit/img/TP-EA3/Clapp.png')