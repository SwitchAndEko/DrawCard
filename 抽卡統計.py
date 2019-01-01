import random
import matplotlib.pyplot as plot
import scipy.stats as stats
import numpy as np

print("抽卡統計")

testTimes = int(input("要連抽幾次?\n"))
takeCardTimes = int(input("要測試幾次的抽卡?\n"))
takePricePercent = float(input("大獎機率為?(請填百分比，不要填%符號)\n")) / 100

result = []

for i in range(takeCardTimes):
    result.append(0)
    for j in range(testTimes):
        result[i] += (1 if random.random() < takePricePercent else 0)

result = sorted(result)

mean = np.mean(result)
std = np.std(result)
print("此次試驗結果：")
print("平均數：%f" % (mean))
print("標準差：%f" % (std))
print("取得大獎最多的張數：%d張" % (np.max(result)))
print("取得大獎最多的張數：%d張" % (np.min(result)))

ndLine = stats.norm.pdf(result, mean, std)
plot.plot(result, ndLine, '-o')
plot.hist(result)
plot.show()
