# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 20:49:42 2018

@author: Pool
"""

import numpy as np
import pandas as pd
cards = 'WABCDEFGHI' # 卡牌可能
line_way = pd.read_csv('line_way.csv') # 賠付線
card_score = pd.read_csv('card_score.csv').set_index('pay_table') # 卡牌賠率表
crdset = {(1,1),(1,2),(1,3),(1,4),(1,5),(2,1),(2,2),(2,3),(2,4),(2,5), # 所有座標
             (3,1),(3,2),(3,3),(3,4),(3,5)}

def spin(): #產生一組 3X5 隨機卡牌組 column可重複!!  p:調整每張牌出現機率!!  輸出數字方便運算
    arr = np.random.choice(
            [1,2,3,4,5,6,7,8,9,10], 15
            , p=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,]
            ).reshape(3, 5) # 隨機抽取 3x5 array 可重複
    return arr

# =============================================================================
# def spin2(): #產生一組 3X5 隨機卡牌組 column不重複 (本專案不使用)
#     arr = np.array(random.sample(cards,3),ndmin=2).T # 10選3 不重複 3x1 array
#     for n in range(4):
#         arr =  np.hstack((arr,np.array(random.sample(cards,3),ndmin=2).T)) # 合併3x5
#     return arr
# =============================================================================

# =============================================================================
# def numtocrd_lst(lst): # 數字list 轉 Cards 字母list (本專案不使用)
#     for n in range(5):
#         lst[n] = cards[lst[n]-1]
#     return lst
# =============================================================================

def numtocrd_arr(numarr): # 數字(int)array 轉 Cards 字母(str)array
    arr = np.full((3, 5),'')
    for n in range(3):
        for m in range(5):
            arr[n][m] = cards[numarr[n, m]-1]
    return arr

def line(arr, num): # 讀取賠付線 line (3x5卡牌array, line_number(1~20))
    x_ind = line_way.iloc[num-1]
    arr = numtocrd_arr(arr)
    lst = []
    for n in range(5):
        lst.append(arr[(x_ind[n]-1), n])
    return lst

def same_test(lst_a): # 計算沒有 W line的連貫數 func(func( )) 就能獲得足夠資訊判斷連貫數
    count = len(lst_a) # AABBD -> ANBN -> NNN   AAABB -> AANB -> ANN 1A 3連貫
    lst_b = []  # AAAAB -> AAAN -> AAN 2A 4連貫   AAAAA -> AAAA -> AAA 3A 5連貫
    for n in range(count-1): # 鄰近相同輸出卡牌編號 不同輸出N
        if lst_a[n] == lst_a[n+1]: 
            lst_b.append(lst_a[n])
        else:
            lst_b.append('N')
    return lst_b

def same_test_W_in(lst_a): # 計算有 W line的連貫數 func(func( )) 就能獲得足夠資訊判斷連貫數
    count = len(lst_a) # WABWD -> ANBD -> NNN   WAABW -> AANB -> ANN A 3連貫 AAWBB AB雙3連貫
    lst_b = [] # AWWWB -> AWWB -> AWB AB 雙4連貫 AWWBW -> AWBB -> ABB A 3連貫 B 4連貫
    for n in range(count-1): # 鄰近相同輸出卡牌編號 不同輸出N
        if lst_a[n] == 'W':
            lst_b.append(lst_a[n+1])
        elif lst_a[n+1] == 'W':
            lst_b.append(lst_a[n])
        elif lst_a[n] == lst_a[n+1]:
            lst_b.append(lst_a[n])
        else:
            lst_b.append('N')
    return lst_b

def line_score(line): # 計算分數 輸出分數 和 連貫資料
    if 'W' not in line:  # 沒有 W 情況
        lst = same_test(same_test(line)) # 用無W函式
        if lst.count('N') == 3: # 三數小於3
            card, get_num, card2, get_num2 = 'W', 1, 'W', 1
        elif lst.count('N') == 2: # 無 W 3連貫
            same_card = (set(lst) & set(cards)).pop()
            card, get_num, card2, get_num2 =  same_card, 3, 'W', 1
        elif lst.count('N') == 1: # 無 W 4連貫
            same_card = (set(lst) & set(cards)).pop()
            card, get_num, card2, get_num2 =  same_card, 4, 'W', 1
        else: # 無 W 5連貫
            same_card = (set(lst) & set(cards)).pop()
            card, get_num, card2, get_num2 =  same_card, 5, 'W', 1        
    else: # 1~5個 W
        lst = same_test_W_in(same_test_W_in(line)) # 用有W函式
        if lst.count('N') == 3: # 連貫數小於3
            card, get_num, card2, get_num2 = 'W', 1, 'W', 1
        elif lst.count('N') == 2: # 3連貫 單張卡
            same_card = (set(lst) & set(cards)).pop()
            card, get_num, card2, get_num2 =  same_card, 3, 'W', 1
        elif lst.count('N') == 1: # 4連貫 或 雙3連貫
            if len(set(lst)-{'N', 'W'}) == 1: # 4連貫
                same_card = list(set(lst)-{'N', 'W'}).pop()
                card, get_num, card2, get_num2 =  same_card, 4, 'W', 1
            else: #雙3連貫
                set_pop = set(lst) & set(cards)
                same_card = set_pop.pop()
                same_card2 = set_pop.pop()
                card, get_num, card2, get_num2 =  same_card, 3, same_card2, 3
        else: # 5連貫 或 雙4連貫 或 3連貫+4連貫 
            set_a = set(lst)
            set_a.discard('W')
            if len(set_a) == 0: # W 5連貫
                card, get_num, card2, get_num2 =  'W', 5, 'W', 1
            elif len(set_a) == 1: # 5連貫
                same_card = (set(lst) & set(cards)).pop()
                card, get_num, card2, get_num2 =  same_card, 5, 'W', 1
            elif len(set(lst)) == 3: # 雙4連貫
                set_pop = set(lst) & set(cards)
                set_pop.remove('W')
                same_card = set_pop.pop()
                same_card2 = set_pop.pop()
                card, get_num, card2, get_num2 =  same_card, 4, same_card2, 4
            else: # 3連貫+4連貫
                if lst[0] == lst[1]:
                    card, get_num, card2, get_num2 = lst[0], 4, lst[2], 3 
                else:
                    card, get_num, card2, get_num2 = lst[1], 4, lst[0], 3
    # 取得連貫資料和卡種 用卡牌賠率表card_score 計算得分!!
    score = card_score.loc[card][get_num-1] + card_score.loc[card2][get_num2-1]
    return score, lst

def spin_score(arr):#3x5卡牌 spin輸出一次 20條連貫 所有得分 及 消除卡片座標總計
    score = 0
    lst = []
    for n in range(1,21): # 20條線編號
        linscore, data = line_score(line(arr,n))
        if linscore > 0:
            score += linscore # 分數加總
            x_ind = line_way.iloc[n-1]  # 由連貫資料 換算賠付線中array位置(消除座標)
            for m in range(3):
                if data[m] != 'N':
                    lst.append((x_ind[m],m+1))
                    lst.append((x_ind[m+1],m+2))
                    lst.append((x_ind[m+2],m+3))
    lst = list(set(lst))
    return score, lst

def clear_crd(arr, lst, a): # 消除卡片:n = 0   更換 W: n = 1 
    for n, m in lst:
        arr[n-1][m-1] = a
    return arr

def drop_crd(arr): # 卡片落下
    for n in range(5):
        if arr[2,n] == 0:
            arr[2,n] = arr[1,n]
            arr[1,n] = 0
        if arr[1,n] == 0:
            arr[1,n] = arr[0,n]
            arr[0,n] = 0
        if arr[2,n] == 0:
            arr[2,n] = arr[1,n]
            arr[1,n] = 0
    return arr

def find_W(arr): # 尋找3x5中的W 回傳卡片座標
    lst = []    
    for n in range(3):
        for m in range(5):
            if arr[n][m] == 1: # W=1
                lst.append((n+1, m+1))
    return lst

def move_W(): # 八方向移動 隨機選取 輸出移動座標
    mov = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]
    return mov[np.random.choice([0,1,2,3,4,5,6,7])]

def after_mov(lst): # W 移動後座標
    lst_W=[]
    chick = 0
    for a, b in lst:
        mov = move_W() # 隨機移動座標
        lst_W.append((a+mov[0], b+mov[1])) # 新座標=原座標+隨機移動座標
    lst_W = list(set(lst_W)) # 檢查有相同的新座標整合為一
    if len(set(lst_W) - crdset) != 0: # 若有坐標系外的座標 len != 0
        chick = 1
    lst_W = list(set(lst_W) & crdset) # 整合在坐標系內的座標
    return lst_W, chick
    
def update_crd(arr, lst): # 更新卡片 消除掉落
    arr = clear_crd(arr, lst, 0)
    arr = drop_crd(arr)
    ar = spin()
    arr = ar*((arr == 0).astype(np.int)) + arr # arr 中 0的部分(消除的座標)換上新隨機數
    return arr

def update_wmov(arr):# 更新卡片 W 移動
    lst_W = find_W(arr)
    af_W, chick =  after_mov(lst_W)
    arr = np.full_like(arr, 0)
    arr = clear_crd(arr, af_W, 1)
    ar = spin()
    arr = ar*((arr == 0).astype(np.int)) + arr # arr 中 0的部分(消除的座標)換上新隨機數
    return arr, chick
# =============================================================================
# func UP
# =============================================================================

# =============================================================================
# 不消除  演算法 (本專案不使用)
# allscore = 0
# rtp_lst = []
# spin_time = 100
# for x in range(1,101):
#     for n in range(spin_time):
#         arr = spin()
#         score = spin_score(arr)[0]
#         allscore += score
#     print("chick %d"%x)
#     rtp = allscore*100/(x*spin_time*20) # 20條線  100 百分比
#     rtp_lst.append(rtp)
#    
# =============================================================================



