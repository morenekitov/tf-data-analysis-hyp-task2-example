import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest
import scipy.stats as st


chat_id = 287133833 # Ваш chat ID, не меняйте название переменной



def solution(x: np.array, y: np.array) -> bool:
    x = np.array(x).ravel()
    y = np.array(y).ravel()
    a = 0.01
    p_ks = st.ks_2samp(x,y,method='asymp')[1]
    return (p_ks < a)
        
