import random
import matplotlib.pyplot as plot
import scipy.stats as stats
import numpy as np

print("抽卡模擬器")
count = 0

takePricePercent = float(input("大獎機率為?(請填百分比，不要填%符號)\n")) / 100
while (1):
    count += 1
    if (random.random() < takePricePercent):
        break

print("你在第%d張抽到大獎" % (count))