import pandas as pd
import numpy as np

from scipy import stats

chat_id = 897901830 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    pval = stats.kruskal(x, y).pvalue
    return pval < 0.05
