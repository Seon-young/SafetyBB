import math

def v(nowlon, nowlat, lastlon, lastlat) :
    

    a1 = nowlon
    b1 = nowlat

    a2 = lastlon
    b2 = lastlat
    

    a1 = round(a1,4)
    b1 = round(b1,4)

    a2 = round(a2,4)
    b2 = round(b2,4)


    ia = int(a1)-int(a2) 
    ib = int(b1)-int(b2) 


    ia = abs(ia)
    ib = abs(ib)

    a1 = (a1 - int(a1))*100
    b1 = (b1 - int(b1))*100

    a2 = (a2 - int(a2))*100
    b2 = (b2 - int(b2))*100

    iia = int(a1)-int(a2) 
    iib = int(b1)-int(b2) 


    iia = abs(iia)
    iib = abs(iib)

    a1 = (a1 - int(a1))*100
    b1 = (b1 - int(b1))*100

    a2 = (a2 - int(a2))*100
    b2 = (b2 - int(b2))*100

    iiia = int(a1)-int(a2) 
    iiib = int(b1)-int(b2) 


    iiia = abs(iiia)
    iiib = abs(iiib)

    kd = ia * 88.8
    kb = iia * 1.48
    kc = iiia * 0.025
    kk = round(kd + kb + kc, 2)

    wd = ib * 111
    wb = iib * 1.85
    wc = iiib * 0.031
    ww = round(wd + wb + wc, 2)

    
    kk = kk**2
    ww = ww**2

    s = kk + ww
    
    #print "kmkmkmkmkmkmkmkmkm" 
    #print round(math.sqrt(s),2)
    return round(math.sqrt(s),2)
