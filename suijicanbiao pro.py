import random
import pandas as pd

menu = []
dish = input("向菜谱中添加一道菜品名称：")
menu.append(dish)
num = 1
while dish != "stop":
    dish = input("继续添加菜品（输入stop停止）：")
    if dish != 'stop':
        menu.append(dish)
        num = num + 1
lunch = []
dinner = []
for item in range(0, 7):
    lunch.append(menu[random.randint(0, num - 1)])
    dinner.append(menu[random.randint(0, num - 1)])
lst = pd.DataFrame([lunch, dinner], index=['午餐', '晚餐'], columns=['周一 ', '周二 ', '周三 ', ' 周四', ' 周五', ' 周六', ' 周天'])
print(lst)
print('随机餐表已生成！')
