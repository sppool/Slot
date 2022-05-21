# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 10:07:15 2018

@author: Pool
"""

import pandas as pd
import pickle
import matplotlib.pyplot as plt
# 500次紀錄一點  500點  25萬次 四次 共100萬次

p1 = pickle.load(open('case201_pickle.dat', 'rb'))
p2 = pickle.load(open('case202_pickle.dat', 'rb'))
p3 = pickle.load(open('case203_pickle.dat', 'rb'))
p4 = pickle.load(open('case204_pickle.dat', 'rb'))
p5 = pickle.load(open('case205_pickle.dat', 'rb'))
p6 = pickle.load(open('case211_pickle.dat', 'rb'))
p7 = pickle.load(open('case212_pickle.dat', 'rb'))
p8 = pickle.load(open('case213_pickle.dat', 'rb'))
p9 = pickle.load(open('case214_pickle.dat', 'rb'))
p10 = pickle.load(open('case215_pickle.dat', 'rb'))

n = 500
fig1 = plt.figure(figsize=(15, 8))
plt.plot(p1[:n], 'o', linewidth=3, label='case-1')
plt.plot(p2[:n], 'o', linewidth=3, label='case-2')
plt.plot(p3[:n], 'o', linewidth=3, label='case-3')
plt.plot(p4[:n], 'o', linewidth=3, label='case-4')
plt.plot(p5[:n], 'o', linewidth=3, label='case-5')
plt.plot(p6[:n], 'o', linewidth=3, label='case-6')
plt.plot(p7[:n], 'o', linewidth=3, label='case-7')
plt.plot(p8[:n], 'o', linewidth=3, label='case-8')
plt.plot(p9[:n], 'o', linewidth=3, label='case-9')
plt.plot(p10[:n], 'o', linewidth=3, label='case-10')

plt.legend()


#def chg(lst):
#    for n in range(len(lst)):
#        lst[n] = lst[n]*(n+1) 
#    for n in range(len(lst)-1, 0, -1):
#        lst[n] = lst[n]-lst[n-1]
#    return lst

#chg(p1)
#chg(p2)
#chg(p3)
#chg(p4)
#chg(p5)

lst1 = []
lst1.extend(p1)
lst1.extend(p2)
lst1.extend(p3)
lst1.extend(p4)
lst1.extend(p5)
lst2 = []
lst2.extend(p6)
lst2.extend(p7)
lst2.extend(p8)
lst2.extend(p9)
lst2.extend(p10)
lst =[]
lst.extend(lst1)
lst.extend(lst2)
#del p1, p2, p3, p4, p5

lst = pd.Series(lst, name='run')
lst = lst/20
lst1 = pd.Series(lst1, name='run')
lst1 = lst1/20
lst2 = pd.Series(lst2, name='run')
lst2 = lst2/20

#lsst = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]
#for n in lsst:
#    n = pd.Series(n, name='run')
#for n in lsst:
#    n = n/20
#for n in lsst:
#    print(n.describe())

p1 = pd.Series(p1, name='run')
p2 = pd.Series(p2, name='run')
p3 = pd.Series(p3, name='run')
p4 = pd.Series(p4, name='run')
p5 = pd.Series(p5, name='run')
p6 = pd.Series(p6, name='run')
p7 = pd.Series(p7, name='run')
p8 = pd.Series(p8, name='run')
p9 = pd.Series(p9, name='run')
p10 = pd.Series(p10, name='run')
p1 = p1/20
p2 = p2/20
p3 = p3/20
p4 = p4/20
p5 = p5/20
p6 = p6/20
p7 = p7/20
p8 = p8/20
p9 = p9/20
p10 = p10/20

fig2 = plt.figure(figsize=(15, 8))
plt.plot(lst1, 'o',  markersize=5, label='600')
plt.plot(lst2, 'o',  markersize=5, label='600')
plt.title('Case') 
plt.xlabel('time')
plt.ylabel('RTP')
plt.legend()

#print(lst.describe())
#print(p1.describe())
#print(p2.describe())
#print(p3.describe())
#print(p4.describe())
#print(p5.describe())

#rtp1 = pd.Series(rtp1, name='case1')
#rtp2 = pd.Series(rtp2, name='case2')
#
#print('case1 avg RTP:%0.2f%%'%(rtp1.mean()))
#print('case2 avg RTP:%0.2f%%'%(rtp2.mean()))