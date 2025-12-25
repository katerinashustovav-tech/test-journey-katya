######## 1. Дана строка. Очистить её от дублей символов
str = "abcdeabc"
result = " "
for i in str:
    if i not in result:
        result += i
print(result)

######## 2. Дан список с числами. Оставьте в нем только положительные числа
nums = [12, 10, 33, -20, 5, -8, 35, -10, 80, 101]
positive_nums = []

for num in nums:
    if num > 0:
        positive_nums.append(num)
        
print(positive_nums)

###### 3. Дана строка. Удалите предпоследний символ из этой строки.
a = "I want to break free"
result = a[:-2] + a[-1:]
print(result)

######## 4. Дан список с дробями. Округлите эти дроби до одного знака в дробной части.
b = [1.456, 2.125, 3.32, 4.1, 5.34]
result = []

for number in b:
    rounded_number = round(number, 1)
    result.append(rounded_number)
    
print(result)

####### 5. Даны два списка. Объедините эти списки в один:
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = [*lst1, *lst2]
print(lst3)

####### 6. Даны два словаря. Объедините эти словари в один
dct1 = {
	'a': 1,
	'b': 2,
}
dct2 = {
	'c': 3, 
	'd': 4,
}

dct3 = {}

for key in dct1:
    dct3[key] = dct1[key]
    
for key in dct2:
    dct3[key] = dct2[key]
    
print(dct3)

######### 7. Дано некоторое слово. Проверьте, 
# что это слово читается одинаково с любой стороны.

word = "abcba"
if word[0:] == word[::-1]:
    print("Yes")
else:
    print("No")

######### 8. Дано число. Получите список делителей этого числа.
n = int(input())
n_list = []

for i in range(1, n + 1):
    if i % 2 == 0:
        n_list.append(i)
        
print(n_list)

####### 9. Дан список. Удалите из него каждый пятый элемент.
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
new_list = []
position = 1

for num in list:
    if position % 5 != 0:
        new_list.append(num)
    position += 1
        
print(new_list)

####### 10. Дана некоторая строка. Смените регистр букв этой строки на противоположный.

c = "AbCdE"
print(c.swapcase())

