import sys, os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def _distance1(df, a, abar):
    values = np.array(df).T
    print(values.shape)
    Sig = df.cov()
    Sig2 = np.cov(values)
    print(np.linalg.norm(Sig-Sig2))
    Sigm1 = np.linalg.inv(Sig)
    mean = np.array(df.mean(axis=0))
    # return np.array(df - mean) @ Sigm1 @ np.array((df - mean).T)
    return np.array(np.abs(a - abar)) @ Sigm1 @ np.array(np.abs(a - abar).T)

def _distance2(df):
    mean = df.mean(axis=0)
    a_max = np.max(df - mean, axis=1)
    return (df - mean).dot((df - mean).T) / a_max

def distance1(a, abar, Sigm1):
    diff = np.array(a - abar)
    return diff @ Sigm1 @ diff.T


def distance2(a, abar, Mm1):
    diff = np.array(a - abar)
    return diff @  Mm1 @ diff.T


def computeM(df):
    mean = df.mean(axis=0)
    a_max = np.max(np.abs(df - mean), axis=0)
    return np.diag(a_max**2)



def getDistances(df_true, df):

    try:
        Sig = np.linalg.inv(np.array(df.cov()))
    except np.linalg.LinAlgError as err:
        if 'Singular matrix' in str(err):
            print("Singular matrix")
            Sig = np.eye(df.shape[1])

    abar = df.mean(axis=0)

    M = computeM(df)
    Mm1 = np.linalg.inv(M)

    d1 = []
    d2 = []
    d_theta = [[], [], []]
    for i in range(df.shape[0]):
        d1_ = distance1(df_true.iloc[i], abar, Sig)
        d2_ = distance2(df_true.iloc[i], abar, Mm1)
        d1.append( d1_ )
        d2.append( d2_ )
        for i, theta in enumerate([0.25, 0.5, 0.75]):
            d_theta[i].append( theta * d1_ + (1-theta) * d2_ )

    return d1, d2, d_theta