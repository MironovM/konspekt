#word=input('Введите слово:')
#print(word)

#word_length=len(word)
#print(word_length)

#if word_length > 5:
    #print('Looooong!')
#print('End.')

num=input('Введите год:')
print(num)
#num2=input('Введите еще одно число:')
#print(num2)
num=int(num)
#num2=int(num2)
#if num > 0:
    #print(num*10)
#if num > 0 and num<=5:
    #print('(0;5]')
#else:
    #print('Меньше нуля или равно ему')
    #print(-num)
    #if num>-2:
        #print('Больше -2')
#if num%2==0:
 #   print('Первое число четное')
#else:
 #   print('Первое число нечетное')
#if num2%2==0:
 #   print('Второе число четное')
#else:
 #   print('Второе число нечетное')
#if num>0:
 #   print('1')
#elif num==0:
 #       print('0')
#elif num<0:
 #       print('-1')
if num%4==0 and num%100!=0 or num%400==0:
    print('Этот год високосный')
else:
    print('Этот год не високосный')
print('End')
