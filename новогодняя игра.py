import random

def guess_the_number():
    print("🎄 Добро пожаловать в новогоднюю игру 'Угадай число'! 🎄")
    print("🎊Я загадал число от 1 до 100. Попробуй угадать его!🎊")

    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            player = int(input("🎅Введите ваше число🎅: "))
            attempts += 1

            if player < number:
                print("Слишком низко! Попробуй еще раз.")
            elif player > number:
                print("Слишком высоко! Попробуй еще раз.")
            else:
                print(f"🎉 Поздравляем! Вы угадали число {number} за {attempts} попыток! желаю тебе {number} подарков и хорошего нового года!! до свидания!🎉")
                break
        except ValueError:
            print("Пожалуйста, введите целое число.")

if __name__ == "__main__":
    guess_the_number()
    