# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 00:58:48 2018

@author: Pool
"""
import pickle
import slot_func as slot

# 第一題 case1 消除掉落 演算法

allscore = 0
rtp_lst = []
spin_time = 500 # 500次記錄一次
for x in range(1,501):  # 總次數 500x500 25萬次
    for n in range(spin_time):
        arr = slot.spin()  # 一次spin 20條線都下注
        score , clr_lst = slot.spin_score(arr)  # 回傳分數,連貫的座標(消除座標)
        allscore += score  # 得分累積
        while score != 0:
            arr = slot.update_crd(arr, clr_lst)  # 消除掉落 更新牌組
            score , clr_lst = slot.spin_score(arr)  # 回傳分數.得分消除的座標
            allscore += score  # 得分累積
    print("chick %d"%x)
    rtp = allscore*100/(x*spin_time*20) # 20條線  100 百分比
    rtp_lst.append(rtp)
print('RTP:%.3f%%'%rtp)

#pickle.dump(rtp_lst, open('case1_pickle.dat', 'wb'))

