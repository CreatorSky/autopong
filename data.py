import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle

train_data = np.load('training_data.npy')
print('loaded')
df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))
