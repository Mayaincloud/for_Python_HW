# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.




num = int(input('Введите число от 0 до 100001: '))

if 1 < num <= 100000:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print('Вы ввели составное число')
            break
        else:
            print('Вы ввели простое число')
            break
else:
   print('Ошибка!Попробуйте еще раз')