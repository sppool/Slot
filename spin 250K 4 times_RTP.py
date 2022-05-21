# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 11:35:58 2018

@author: Pool
"""

import pandas as pd
import pickle
import matplotlib.pyplot as plt

#%matplotlib
# 500次紀錄一點  500點  25萬次 四次 共100萬次

rtp11 = pickle.load(open('case1-1_pickle.dat', 'rb'))
rtp12 = pickle.load(open('case1-2_pickle.dat', 'rb'))
rtp13 = pickle.load(open('case1-3_pickle.dat', 'rb'))
rtp14 = pickle.load(open('case1-4_pickle.dat', 'rb'))
rtp21 = pickle.load(open('case2-1_pickle.dat', 'rb'))
rtp22 = pickle.load(open('case2-2_pickle.dat', 'rb'))
rtp23 = pickle.load(open('case2-3_pickle.dat', 'rb'))
rtp24 = pickle.load(open('case2-4_pickle.dat', 'rb'))

n = 500
fig1 = plt.figure(figsize=(15, 8))
plt.plot(rtp11[:n], linewidth=3, label='case1-1')
plt.plot(rtp12[:n], linewidth=3, label='case1-2')
plt.plot(rtp13[:n], linewidth=3, label='case1-3')
plt.plot(rtp14[:n], linewidth=3, label='case1-4')
plt.title('Case1') 
plt.xlabel('spin times(x500)')
plt.ylabel('RTP')
plt.legend()
#fig1.savefig('RTP1.png')

fig2 = plt.figure(figsize=(15, 8))
plt.plot(rtp21[:n], linewidth=3, label='case2-1')
plt.plot(rtp22[:n], linewidth=3, label='case2-2')
plt.plot(rtp23[:n], linewidth=3, label='case2-3')
plt.plot(rtp24[:n], linewidth=3, label='case2-4')
plt.title('Case2') 
plt.xlabel('spin times(x500)')
plt.ylabel('RTP')
plt.legend()
#fig2.savefig('RTP2.png')

fig = plt.figure(figsize=(15, 8))
plt.plot(rtp11[:n], linewidth=3, label='case1-1')
plt.plot(rtp12[:n], linewidth=3, label='case1-2')
plt.plot(rtp13[:n], linewidth=3, label='case1-3')
plt.plot(rtp14[:n], linewidth=3, label='case1-4')
plt.plot(rtp21[:n], linewidth=3, label='case2-1')
plt.plot(rtp22[:n], linewidth=3, label='case2-2')
plt.plot(rtp23[:n], linewidth=3, label='case2-3')
plt.plot(rtp24[:n], linewidth=3, label='case2-4')
plt.title('Case1+Case2') 
plt.xlabel('spin times(x500)')
plt.ylabel('RTP')
plt.legend()
#fig.savefig('RTP.png')

def chg(lst):
    for n in range(len(lst)):
        lst[n] = lst[n]*(n+1) 
    for n in range(len(lst)-1, 0, -1):
        lst[n] = lst[n]-lst[n-1]
    return lst

chg(rtp11)
chg(rtp12)
chg(rtp13)
chg(rtp14)
chg(rtp21)
chg(rtp22)
chg(rtp23)
chg(rtp24)

rtp1 = rtp11 + rtp12 + rtp13 + rtp14
rtp2 = rtp21 + rtp22 + rtp23 + rtp24

del rtp11, rtp12, rtp13, rtp14, rtp21, rtp22, rtp23, rtp24

#pickle.dump(rtp1, open('case1_1000K_pickle.dat', 'wb'))
#pickle.dump(rtp2, open('case2_1000K_pickle.dat', 'wb'))

rtp1 = pd.Series(rtp1, name='case1')
rtp2 = pd.Series(rtp2, name='case2')

print('case1 avg RTP:%0.2f%%'%(rtp1.mean()))
print('case2 avg RTP:%0.2f%%'%(rtp2.mean()))

