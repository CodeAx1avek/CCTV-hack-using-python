#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#github.com/CodeAvek
import requests, re , colorama
colorama.init()
print("""
\033[1;31m\033[1;37m   ____          _  
 / ___|___   __| | ___   / \   __  _/ |
| |   / _ \ / _` |/ _ \ / _ \  \ \/ / |
| |__| (_) | (_| |  __// ___ \  >  <| |
 \____\___/ \__,_|\___/_/   \_\/_/\_\_|
                                       
select the option given below!                                                          CODEAX!
\033[1;31m1) \033[1;37mUnited States
\033[1;31m2) \033[1;37mJapan
\033[1;31m3) \033[1;37mItily
\033[1;31m4) \033[1;37mKorea
\033[1;31m5) \033[1;37mFRANCE
\033[1;31m6) \033[1;37mIndia
\033[1;31m7) \033[1;37mRussia
\033[1;31m8) \033[1;37mThailand
\033[1;31m9) \033[1;37mPakistan
\033[1;31m10) \033[1;37mSriLanka
""")

try:
    print()
    countries = ["US", "JP", "IT", "KR", "FR", "IN", "RU", "TH", "PK", "LK"]
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}
    countname = ["UNITED STATES - BY CODEAX1!", "JAPAN - BY CODEAX1!", "ITILY - BY CODEAX1!", "KOREA - BY CODEAX1!", "FRANCE - BY CODEAX1!", "INDIA - BY CODEAX1!", "RUSSIA - BY CODEAX1!", "THAILAND - BY CODEAX1!", "PAKISTAN - BY CODEAX1!", "SRILANKA - BY CODEAX1!"]
    num = int(input("OPTIONS : "))
    print("You Have Selected Option",countname[num-1])
    if num not in range(1, 10+1):
        raise IndexError

    country = countries[num-1]
    res = requests.get(
        f"http://www.insecam.org/en/bycountry/{country}", headers=headers
    )
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

    for page in range(int(last_page)):
        res = requests.get(
            f"http://www.insecam.org/en/bycountry/{country}/?page={page}",
            headers=headers
        )

        find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
        for ip in find_ip:
            print("\033[1;31m", ip,"\033[3;95m",countname[num-1])
    print('We Have Showed all the the Camera ip ')
    print('CodeAx1!')
except:
    pass
finally:
    print("\033[1;37m")
    exit()
