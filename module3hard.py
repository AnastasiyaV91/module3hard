def calculate_structure_sum(*args, **kwargs):
    sum = 0
    for argum in args:                                    # Для каждого аргумента в args
        if isinstance(argum, int):                        # если аргумент является целочисленным значением
            sum += argum                                  # увеличиваем sum на значение argum
        elif isinstance(argum, str):                      # А так же если аргумент является строкой
            sum += len(argum)                             # увеличиваем sum на длинну строки argum
        elif isinstance(argum, tuple):                    # А так же если аргумент является кортежем
            sum += calculate_structure_sum(*argum)        # увеличиваем sum на каждый численный элемент
        elif isinstance(argum, list):                     # А так же если аргумент является списком
            sum += calculate_structure_sum(*argum)        # увеличиваем sum на каждый численный элемент
        elif isinstance(argum, set):                      # А так же если аргумент является множеством
            sum += calculate_structure_sum(*argum)        # увеличиваем sum на каждый численный элемент
        elif isinstance(argum, dict):                     # А так же если аргумент является словарем
            for value in argum.values():                  # Для каждого значения словоря
                if isinstance(value, int):                # Для каждого значения словаря целочисленного значения value
                    sum += value                          # увеличиваем sum на значение value
                elif isinstance(value, str):              # А так же для каждого значения элемента списка строка
                    sum += len(value)                     # увеличиваем sum на длинну value
            for key in argum.keys():                      # Для каждого значения ключа
                if isinstance(key, str):                  # Для каждого значения ключа целочисленного значения key
                    sum += len(key)                       # увеличиваем sum на длинну значения ключа key
    return sum

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)