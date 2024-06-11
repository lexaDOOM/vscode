def from_tiny_to_large (avscore, drscore, count, mark):
    counter = 0 # Счётчик
    if (avscore > 5 or avscore < 2) or (drscore > 5 or drscore < 2):
        return 'Error #1: Ср. балл или желаемый балл ∉ [2; 5]'
    if avscore >= drscore: # Исключение ненужной работы
        return 0
    else: # Основной алгоритм
        while avscore <= drscore:
            summ = avscore * count
            summ += mark
            count += 1
            avscore = summ / count
            counter += 1
    return counter


#Сбор данных
average_score = float(input('Введите ср. балл >> '))
dream_score = float(input('Введите желаемый ср. балл >> '))
count_marks = int(input('Введите количество оценок >> '))
mark_for_solve = int(input('Введите оценку для исправления >> '))

# Исключение бесконечного цикла
if dream_score % 1 == 0:
    round_number = 1 - float(input('Введите минимальную дробную часть для огругления итоговой оценки в большую сторону >> '))
    dream_score -= round_number

# Использование ф-ции "from_tiny_to_large" и вывод результата на экран
print(from_tiny_to_large(average_score, dream_score, count_marks, mark_for_solve))
