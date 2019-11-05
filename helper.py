import numpy as np
import pandas as pd
import math

def get_data(stock_name, window_size):
    df = pd.read_csv("./data/"+stock_name+".csv")
    train = list(df[(df['timestamp'] >= '1995-1-1 01:00:00') & (df['timestamp'] <= '2013-12-31 04:00:00')]['close'])
    # train2 = train[:-(len(train)%window_size)]
    test = list(df[(df['timestamp'] >= '2018-1-1 01:00:00') & (df['timestamp'] <= '2018-12-31 12:00:00')]['close'])
    # test2 = test[:-(len(test)%window_size)]
    return train, test

def get_state(data, t, n):
	d = t - n + 1
	block = data[d:t + 1] if d >= 0 else -d * [data[0]] + data[0:t + 1] # pad with t0
	res = []
	for i in range(n - 1):
		res.append(sigmoid(block[i - 1] - block[i]))

	return np.array([res])

def sigmoid(x):
    return 1 / (1+math.exp(-x))
