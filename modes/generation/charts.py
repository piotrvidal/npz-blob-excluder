import csv
import numpy as np
import matplotlib.pyplot as plt
from tools import names
import numpy.ma as ma
import matplotlib.cm as cm

class Generator:

    def __init__(self, filename, chart_type):
        self.filename = filename
        
        if chart_type == names.TRAJECTORY:
            outputs = self.read_csv(filename, params=[names.X, names.Y])
            self.plot_trajectory(outputs[0], outputs[1])

    def plot_trajectory(self, x, y):

        x = np.array(x, dtype=float)
        y = np.array(y, dtype=float)

        masked_x = ma.masked_invalid(x)
        masked_y = ma.masked_invalid(y)

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        ax.scatter(x, y, c=x, cmap=cm.jet, s=0.3)

        plt.savefig('test.png')
        plt.show()

    def read_csv(self, filename, params):
        with open('./output/{}'.format(filename), newline='') as csv_file:
            reader = csv.DictReader(csv_file)

            outputs = []
            for length in params:
                outputs.append([])

            for row in reader:
                for length in range(0, len(params)):
                    outputs[length].append(row[params[length]])
        
        return outputs