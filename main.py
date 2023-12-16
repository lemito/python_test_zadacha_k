import math


someDict: dict[int, list] = dict()
newTmp: dict[int, float] = dict()
cnt: int = 1

# Считывание и запись в некий словарь
with open("test.txt", "r") as f:
    for i in f.readlines():
        someDict[cnt] = i.split()
        cnt += 1

# Сохранение промежуточного результата
for i in someDict.keys():
    if (
        float(someDict[i][1]) != 0.0
        and float(someDict[i][3]) != 0.0
        and float(someDict[i][0]) > 0
        and float(someDict[i][1]) > 0
        and float(someDict[i][2]) > 0
        and float(someDict[i][3]) > 0
    ):
        preRes = (float(someDict[i][0]) / float(someDict[i][1])) ** (
            float(someDict[i][2]) / float(someDict[i][3])
        )
        newTmp[i] = round(preRes, 8)
print(newTmp)

# Вывод результатов
for i in newTmp.keys():
    if math.isclose(newTmp[i], 1.00000000):
        print(
            f"{i}: Основание {(float(someDict[i][0]) / float(someDict[i][1]))} и степень {float(someDict[i][2]) / float(someDict[i][3])}."
        )
        print(newTmp[i])
        print(
            round(
                (float(someDict[i][0]) / float(someDict[i][1]))
                ** (float(someDict[i][2]) / float(someDict[i][3]))
            ),
            0,
        )

del someDict
del newTmp
