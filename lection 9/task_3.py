# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

all_purchase_sum = []
purchase_sum = 0
with open('test_file/task_3.txt', mode='r', encoding='utf-8') as f_start:
    for line in f_start:
        line_strip = line.strip()
        if line_strip:
            purchase_sum += int(line_strip)
        else:
            all_purchase_sum.append(purchase_sum)
            purchase_sum = 0
all_purchase_sum.sort()
three_most_expensive_purchases = sum(all_purchase_sum[-3:])

assert three_most_expensive_purchases == 202346
if three_most_expensive_purchases == 202346:
    print('Все ок')
else:
    print('Не ок')