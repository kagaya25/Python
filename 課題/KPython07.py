# -*- coding: utf-8 -*-
"""
0H02014 岸本和哉
"""
cnt = 1
cnt1 = 1
cnt2 = 1

print(" ", end = "")
while cnt <= 9:
    print("　 ", cnt, end = "")
    cnt = cnt + 1

print("")
while cnt2 <= 9:
    print (cnt2, end = "")
    while cnt1 <= 9:
        if cnt1 * cnt2 <= 9:
            print(" ", end = "")
        print("　", cnt1 * cnt2, end = "")
        cnt1 = cnt1 + 1
    cnt1 = 1
    cnt2 = cnt2 + 1
    print("")
    