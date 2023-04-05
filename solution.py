import pandas as pd
import numpy as np

from scipy.stats import chi2


chat_id = 395384260 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
   df = 1
    left = np.var(x) / (26 * chi2.ppf(1 - p / 2, df))
    right = np.var(x) / (26 * chi2.ppf(p / 2, df))
    return np.sqrt(left), np.sqrt(right)
