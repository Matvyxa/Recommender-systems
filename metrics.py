import pandas as pd
import numpy as np

def recall(recommended_list, bought_list):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(bought_list, recommended_list)

    recall = flags.sum() / len(bought_list)

    return recall

def recall_at_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    if k < len(recommended_list):
        recommended_list = recommended_list[:k]

    flags = np.isin(bought_list, recommended_list)
    recall = flags.sum() / len(bought_list)

    return recall

def precision(recommended_list, bought_list):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)

    flags = np.isin(bought_list, recommended_list)

    precision = flags.sum() / len(recommended_list)

    return precision
	
def precision_at_k(recommended_list, bought_list, k=5):
    
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    

    bought_list = bought_list  # Тут нет [:k] !!
    
    if k < len(recommended_list):
        recommended_list = recommended_list[:k]

    flags = np.isin(bought_list, recommended_list)

    precision = flags.sum() / len(recommended_list)

    return precision

def hit_rate_at_k(recommended_list, bought_list, k):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list[:k])
    
    flags = np.isin(bought_list, recommended_list)
    
    hit_rate = (flags.sum() > 0) * 1
    
    return hit_rate

def money_precision_at_k(recommended_list, bought_list, prices_recommended, k):
        

    
    bought_list = bought_list
    recommended_list = np.array(recommended_list[:k])
    prices_recommended = np.array(prices_recommended[:k])
    
    flags = np.isin(recommended_list, bought_list)
    
    precision = np.dot(flags, prices_recommended) / prices_recommended.sum()
    
    
    return precision

def money_recall_at_k(recommended_list, bought_list, prices_recommended, prices_bought, k):
    bought_list = np.array(bought_list)
    prices_bought = np.array(prices_bought)
    recommended_list = np.array(recommended_list[:k])
    prices_recommended = np.array(prices_recommended[:k])
    
    flags = np.isin(recommended_list, bought_list)
    
    r1 = np.dot(flags,prices_recommended)
    r2 = prices_bought.sum()
    recall = r1 / r2
  
    return recall
	
def reciprocal_rank(recommended_list, bought_list):
    
    flags = np.isin(recommended_list, bought_list)
    
    if sum(flags) == 0:
        return 0
    
    sum_ = 0
    count = 0
    for i in range(1, len(flags)+1):
        if flags[i-1]:
            sum_ += 1/i
            print(f'iteration:{i}',f'rank (1/i):{1/i}')
            count += 1
    result = sum_ / count
    
    return result