# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 20:10:42 2018

@author: Pool
"""
# 純數學機率運算  只能算為純消除前的機率期望值!!

def c(n,m): #排列組合C n 取 m
    def p(x):
        a = 1
        for s in range(1,x+1):
            a = a*s
        return a
    return p(n)//(p(m)*p(n-m))
 #沒有W在連貫中
con3 = ((1*1*1*8*8)/100000)*3*106  # 排列方式:3 三連貫分數加總:106
con3w = ((1*1*1*8*1)/100000)*2*106  # 排列方式:2 AAANW WNAAA
con4 = ((1*1*1*1*8)/100000)*2*427  # 排列方式:2  四連貫分數加總:427
con5 = ((1*1*1*1*1)/100000)*1*4525  # 排列方式:1  五連貫分數加總:4525
 #有W在連貫中
wcon3 = ((1*1*1*8*8)/100000)*3*106*(c(3,1)+c(3,2)) # 三連貫有1和2個W
wcon3w = ((1*1*1*8*1)/100000)*2*106*(c(3,1)+c(3,2)-2) # (WWA)BW WB(WWA)
w2con3 = ((9*1*1*8*1)/100000)*2*23.556 # WAWBW 平均雙三連貫分數加總:23.556
w2con34 = ((9*1*1*8*1)/100000)*2*59.222 # AWWBW 平均三連貫四連貫分數加總:59.222 
wcon4 = ((1*1*1*1*8)/100000)*2*427*(c(4,1)+c(4,2)+c(4,3)-5) # 四連貫有1.2.3個W
w2con4 = ((9*1*1*1*8)/100000)*2*94.889 # WAWWB 平均雙四連貫分數加總:94.889*2
wcon5 = ((1*1*1*1*1)/100000)*1*4525*(c(5,1)+c(5,2)+c(5,3)+c(5,4)) # 五連貫有1.2.3.4個W

exp_val = (con3+con3w+con4+con5+wcon3+wcon3w+w2con3+w2con34+wcon4+w2con4+wcon5)
print('RTP:%f%%'%(exp_val*100))

# Ans: exp_val = 385.123048%