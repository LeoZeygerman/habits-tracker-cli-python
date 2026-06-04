from storage import save_data, load_data
from habits_logic import add_habit

while True:
    try:
        print('1.Добавить привычку')
        print('2.Показать привычки')
        print('3.Отметить выполнение привычки')
        print('3.Удалить привычку')
        
        choice = int(input('Ваш выбор: '))
        
        if choice == 1:
            add_habit()
        
        if choice == 2:
            pass
        
        if choice == 3:
            pass
        
        if choice == 4:
            pass
        
    except ValueError:
        print('Ошибка при вводе.')