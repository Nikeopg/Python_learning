m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

f, s, t = map(int,input().split())

array = [m[f-1], m[s-1], m[t-1]]
for check in array:
    if check == 'до':
        print(f"#{check}", end=' ')
    elif check == 'фа':
        print(f"#{check}", end=' ')
    else:
        print(check, end=' ')
'''
Имеется список базовых нот:
m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

Вводятся три целых числа в диапазоне от 1 до 7 - номера нот, в одну строчку через пробел. 
Необходимо отобразить указанные ноты в виде строки через пробел, но перед нотами до и фа дополнительно ставить символ диеза '#'. Реализовать эту программу с использованием тернарного условного оператора (он может использоваться несколько раз).

Sample Input:
1 6 7

Sample Output:
#до ля си
'''