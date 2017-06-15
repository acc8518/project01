#!/usr/bin/python2
# -*- coding:UTF-8 -*-
# code related at: http://blog.mckelv.in/articles/1453.html

import sys

distance = lambda a,b : 0 if a==b else 1

def dtw(sa,sb):
    '''
    >>>dtw(u"話說我想查的旅遊地點是陽明山", u"陽明山")
    2
    '''
    MAX_COST = 1<<32
    #初始化一個len(sb) 行(i)，len(sa)列(j)的二維矩陣
    len_sa = len(sa)
    len_sb = len(sb)
    # BUG:這樣是錯誤的(淺拷貝): dtw_array = [[MAX_COST]*len(sa)]*len(sb)
    dtw_array = [[MAX_COST for i in range(len_sa)] for j in range(len_sb)]
    dtw_array[0][0] = distance(sa[0],sb[0])
    for i in range(0, len_sb):
        for j in range(0, len_sa):
            if i+j==0:
                continue
            nb = []
            if i > 0: nb.append(dtw_array[i-1][j])
            if j > 0: nb.append(dtw_array[i][j-1])
            if i > 0 and j > 0: nb.append(dtw_array[i-1][j-1])
            min_route = min(nb)
            cost = distance(sa[j],sb[i])
            dtw_array[i][j] = cost + min_route
    return dtw_array[len_sb-1][len_sa-1]


def main(argv):
    '''
    s1 = u'話說我想查的旅遊地點是陽明山'
    s2 = u'陽明山'
    d = dtw(s1, s2)
    print (d)
    return 0
    '''
    location = ['陽明山','故宮','石門水庫','大溪老街','慈湖','太魯閣','墾丁','士林夜市','赤崁樓','日月潭','台北101','龍山寺','西門町','中正紀念堂','圓山大飯店','六合夜市','合歡山','高雄85大樓','阿里山','安平古堡','義大','鵝鑾鼻','雪山','海博館','台南孔廟','紅毛城','九族','野柳','十分','清境','金瓜石','平溪','愛河','九份','六福村','饒河夜市','漁人碼頭','玉山','逢甲夜市','國父紀念館'] #旅遊地名
    d = [] #查詢目的與旅遊地名之距離
##    print ('目前資料庫裡旅遊地名的數量：', len(location))
    inputtext = input('請輸入您想查詢的台灣旅遊地名：')
    for i in range(len(location)):
        d.append(dtw(inputtext, location[i])) 
##        print (d[i]) #print查詢目的與旅遊地名之距離
##    print('查詢目的與旅遊地名之最小距離：', min(d))
##    print('最小距離對應的index：', d.index(min(d)))
    print('您想查詢的旅遊地點應為：', location[d.index(min(d))])

if __name__ == '__main__':
    sys.exit(main(sys.argv))
