import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest
import scipy.stats as st


chat_id = 287133833 # Ваш chat ID, не меняйте название переменной


def solution(x: np.array, y: np.array) -> bool:
    x = np.array(x).ravel()
    y = np.array(y).ravel()
    a = 0.01
    #H0 - средние равны, x_mean = y_mean
    z_obs, p_val_mean = ztest (x,y,0,usevar='pooled')
    # print('Z-test для средних:')
    # print(f'Наблюдаемое: {z_obs}')
    # print(f'P : {p_val_mean}')

    f = np.var(x, ddof=1)/np.var(y, ddof=1)
    nun = x.size-1
    dun = y.size-1
    p_val_var = 1-st.f.cdf(f, nun, dun)
    # print(f'P для дисперсии{p_val_var}')
    return (p_val_mean < a or p_val_var < a)
     
