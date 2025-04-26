import random
def rsp():
    print("Добро пожаловать в игру 'камень, ножницы, бумага'!")
    choices = ["камень", "ножницы", "бумага"]
    computer = random.choice(choices)
    while True:
        player = input("Введите 'камень', 'ножницы' или 'бумага' (или 'стоп' для выхода):").lower()
        if player == 'стоп':
            print('Вы вышли из игры')
            exit()
        if player not in choices:
            print('Неверный ввод. Пожалуйста, попробуйте снова')
            continue
        print(f"Компьтер выбрал:{computer}")
        if player == computer:
            print('Ничья!')
        elif (player == "камень" and computer == "ножницы") or (player == "ножницы" and computer == "бумага") or (player == "бумага" and computer == "камень"):
            print('Вы выиграли!')
        else:
            print('Вы проиграли!')
while True:
    rsp()
    
                     
    
    