from datetime import datetime
from time import time 

def calculate_bpm(time_deltas):
    mean_tap = (sum([dt.total_seconds() for dt in time_deltas])/len(time_deltas))
    return int(60/mean_tap)

time_deltas = []
while True:
    start = datetime.now()
    i = input()
    if i == "q":
        break
    end = datetime.now()
    elapsed = end - start
    if len(time_deltas) < 8:
        time_deltas.append(elapsed)
    else:
        time_deltas.append(elapsed)
        time_deltas.pop(0)  
    print(calculate_bpm(time_deltas))

