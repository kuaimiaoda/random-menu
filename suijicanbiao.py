import random
import pandas as pd

menu = ['老北京烧肉饭', '木板饭', '秘制老汤拉面', '铁板炒饭', '桃源居春饼家常菜',
        '土鸡泡馍', '无名缘米粉', '铁板烧', '简单味道', '花甲粉', '麻辣香锅',
        '麻辣烫', '河南烩面', '抻面、小笼包', '鸡蛋灌饼', '烤鸭饭', '佰吉客汉堡',
        '淮南牛肉汤', '虾滑米线', '烤肉饭', '麻辣烫', '铁板饭', '萌锅蒸饭', '0090汉堡',
        '鹅汁煲饭', '见面', '韩国料理', '一碗好饭']
lunch = []
dinner = []
for item in range(0, 7):
    lunch.append(menu[random.randint(0, 27)])
    dinner.append(menu[random.randint(0, 27)])
lst = pd.DataFrame([lunch, dinner], index=['午餐', '晚餐'], columns=['周一 ', '周二 ', '周三 ', ' 周四', ' 周五', ' 周六', ' 周天'])
lst.to_excel('随机餐表.xlsx')
print('随机餐表已生成！')
