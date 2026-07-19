def solve_dragon_power(n):
    # Базовые случаи для малых чисел, где стратегия "только тройки" может требовать коррекции
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    if n == 4:
        # 4 лучше разбить на 2+2 (произведение 4), чем 3+1 (произведение 3) или оставить 4
        return 4
    
    # Для N >= 5 применяем стратегию с приоритетом на тройки
    quotient = n // 3
    remainder = n % 3
    
    if remainder == 0:
        return 3 ** quotient
    elif remainder == 1:
        # Если остаток 1, выгоднее заменить одну тройку и единицу на две двойки
        # (3 * 1 < 2 * 2)
        return (3 ** (quotient - 1)) * 4
    else: # remainder == 2
        # Если остаток 2, просто умножаем на 2
        return (3 ** quotient) * 2

# Чтение входных данных
try:
    line = input().strip()
    if line:
        n = int(line)
        result = solve_dragon_power(n)
        print(result)
except ValueError:
    pass
