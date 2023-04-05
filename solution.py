import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 395384260 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = p
    b_alpha = np.quantile(x, alpha)
    return .026, b_alpha
