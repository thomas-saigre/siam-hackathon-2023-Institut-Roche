import numpy as np
import pandas as pd
import os, sys

def convert(x):
    if x.dtype not in [np.int64, np.float64]:
        return x.factorize()[0]
    else:
        return x
    
def convertNan(x):
    return x.fillna(x.min()-100)


def convertDataFrame(df):
    return df.apply(convert).apply(convertNan)


if __name__ == '__main__':
    path = sys.argv[1]
    directory = os.listdir(path)
    for path, subdirs, files in os.walk(path):
        for name in files:
            file = os.path.join(path, name)
            if file.endswith(".csv"):
                df = pd.read_csv(file)
                df = convertDataFrame(df)
                df.to_csv(os.path.join("../data-conv", file), index=False)