def sum_between_extremes(arr):
    if len(arr) < 2:
        return 0  # Если элементов меньше 2, между ними ничего нет

    # 1. Находим индексы максимального и минимального элементов
    max_idx = 0
    min_idx = 0

    for i in range(1, len(arr)):
        if arr[i] > arr[max_idx]:
            max_idx = i
        if arr[i] < arr[min_idx]:
            min_idx = i

    # 2. Определяем границы диапазона (между min и max)
    start = min(max_idx, min_idx) + 1
    end = max(max_idx, min_idx)

    # Если start >= end, значит между ними нет элементов
    if start >= end:
        return 0

    # 3. Суммируем отрицательные элементы строго между индексами
    total_sum = 0
    for i in range(start, end):
        if arr[i] < 0:
            total_sum += arr[i]

    return total_sum


# Пример использования
if __name__ == "__main__":
    # Можно заменить на ввод с клавиатуры или чтение из файла
    A = [3, -5, 10, -2, -8, 7, -1, 4]
    result = sum_between_extremes(A)
    print(f"Массив: {A}")
    print(f"Сумма отрицательных элементов между макс. и мин.: {result}")
