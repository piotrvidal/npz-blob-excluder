import numpy as np
import csv

class Converter:
    def __init__(self, filename):
        self.filename = filename
    
    def convert_and_merge(self):
        filename = self.filename

        with np.load('input/{}'.format(filename)) as npz:

            headers = []
            ignored_headers = ['frame_segments', 'segment_vxys']
            rows = []

            for header in npz.files:
                if header not in ignored_headers:
                    headers.append(header)
                    rows.append(npz[header])
            rows = np.array(rows, dtype=object)

        with open('output/{}_merged_data.csv'.format(filename), 'w') as f:
            writer = csv.writer(f)
            writer.writerow(headers)  
            writer.writerows(rows.T)
