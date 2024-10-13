'''Функція для знаходження підпослідовностей довжиною length зі списку numbers'''
def find_subsequences(length: int, numbers: list) -> list:
    result = []
    _dict_added = {}
    different = 0
    l_ptr = 0
    r_ptr = 0
    '''Цикл досягнення правого вказівника кінця списку numbers'''
    while l_ptr < len(numbers) and r_ptr < len(numbers):
        if different != length:
            if _dict_added.get(numbers[r_ptr]) is None:
                _dict_added[numbers[r_ptr]] = 'added'
                different += 1
            r_ptr += 1
        else:
            result.append([l_ptr, r_ptr - l_ptr])
            _dict_added = {}
            different = 0
            l_ptr += 1
            r_ptr = l_ptr
    result.append([l_ptr, len(numbers) - l_ptr])
    return result


'''Функція для зчитування введених даних від користувача
та перевірка на пустий рядок та білі символи'''
def read_input() -> tuple[int, list]:
    length = int(input('Please enter the N: '))
    numbers = []
    while (a := input()).strip(' \r\f\t\v\n') != '':
        elements = a.split()  # Розбиваємо рядок на окремі елементи
        for element in elements:
            number = int(element)
            if number < 1 or number > length:
                raise ValueError(f'Input error: {number} is not in the range 1 to {length}')
            numbers.append(number)

    '''Підрахунок частоти кожного числа'''
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    '''фільтрування чисел, які зустрічаються менше двох разів'''
    filtered_numbers = [num for num in numbers if frequency[num] >= 2]
    
    return length, filtered_numbers


'''Функція для виведення результату роботи програми'''
def print_result(length: int, numbers: list, indeces: list[list]) -> None:
    print('THE WORK IS DONE')
    print(len(numbers))
    print(length)
    min_length = min(map(lambda item: item[1], indeces))
    for start_index, length in filter(lambda item: item[1] == min_length, indeces):
        print(start_index, length)


def main():
    '''Виведення інформації про автора та
    обробка помилок при натисканні виняткових комбінацій клавіш'''
    try:
        print(
            '''
            The author of this program is Kozhevnyk Ivan.
            Variant 114.
            This program searches for subsequences of different numbers from a sequence 
            '''
        )
        length, numbers = read_input()
        indeces = find_subsequences(length=length, numbers=numbers)
        print_result(length=length, numbers=numbers, indeces=indeces)
    except KeyboardInterrupt:
        print('\nprogram aborted')
    except Exception as e:
        print('***** error')
        print(str(e))


if __name__ == '__main__':
    main()
