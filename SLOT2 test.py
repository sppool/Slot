# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 00:58:48 2018

@author: Pool
"""
import pickle
import slot_func as slot
import numpy as np
np.random.seed(5)
# 第二題 case2 W 移動 演算法  沒有說明在沒有萬用卡的情況 計算得分是否會重新洗牌! 假設不會並結束回合
#%timeit
lst = []
spin_time = 100 # 500次記錄一次
for x in range(1,10):  # 總次數 500x500 25萬次
    allscore = 0
    for n in range(spin_time):
        arr = slot.spin()  # 一次spin 20條線都下注
        chick = 0  # 判斷 W 有沒有跑出去框架
        score = slot.spin_score(arr)[0]  # 回傳分數
        allscore += score  # 得分累積
        if len(slot.find_W(arr)) != 0: # 沒有W 回合結束
            while chick == 0:  # 有W
                arr, chick = slot.update_wmov(arr) # 回傳更新牌組, 和W有沒有跑出框架判斷
                score = slot.spin_score(arr)[0]  # 回傳分數
                allscore += score  # 得分累積
    lst.append(allscore)
    print("chick %d"%x)
#pickle.dump(lst, open('case207_pickle.dat', 'wb'))

