import random

def game():
    # Загадываем случайное число
    hidden_number = random.randint(1, 100)

    print(f"Я загадал целое число от 1 до 100.")
    attempts = 0

    while True:
        # Вариант пользователя
        response = int(input(f"Угадайте число: "))

        attempts += 1

        if response == hidden_number:
            # Угадал число
            print(f"Вы угадали число! Потребовалось {attempts} попыток.")
            break
        elif response < hidden_number:
            # Число меньше загаданного
            print(f"Загаданное число больше {response}")
        else:
            # Число больше загаданного
            print(f"Загаданное число меньше {response}")

game()