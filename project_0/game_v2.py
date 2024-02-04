import numpy as np

def binary_search(number: int = 1) -> int:
    """Угадываем число методом бинарного поиска
    
    Args:
        number (int, optional): Загаданное число. По умолчанию 1.

    Returns:
        int: Число попыток
    """
    count = 0 
    low = 1
    high = 100
    
    while low <= high:
        count += 1
        guess = (low + high) // 2
        if guess < number:
            low = guess + 1
        elif guess > number:
            high = guess - 1
        else:
            break
    
    return count


def score_game(binary_search) -> int:
    """Оценка алгоритма угадывания числа методом бинарного поиска
    
    Args:
        binary_search (function): Функция для угадывания числа

    Returns:
        int: Среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости 
    random_array = np.random.randint(1, 101, size=(1000))  # загадываем список чисел
    
    for number in random_array:
        count_ls.append(binary_search(number))
        
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score


score_game(binary_search)
# print('Количество попыток: ', (binary_search(10)))

# Run
if __name__ == '__main__':
    score_game(binary_search) 