from storage import save_data, load_data
from module import Habit
from datetime import date

def add_habit():
    name = input('Введите название привычки: ')
    data = load_data()
    if len(data) == 0:
        new_id = 1
    else:
        new_id = data[-1]['id'] + 1
    habit = {
        'id': new_id,
        'name': name,
        'completed': False,
        'streak': 0,
        'last_complete': None
    }
    data.append(habit)
    save_data(data)
    print('Привычка успешно добавлена.')
    
def show_habits():
    data = load_data()
    completed = None
    last_complete = None
    for item in data:
        if item['completed'] == False:
            completed = 'Не выполнена.'
        else:
            completed = 'Выполнена.'
        if item['last_complete'] == None:
            last_complete = 'Нет'
        else:
            last_complete = item['last_complete']
        habit_object = Habit(item['id'], item['name'], completed, item['streak'], last_complete)
        habit_object.show_habit()    
    
def completed():
    data = load_data()
    today = date.today()
    show_habits()
    choice = int(input('Введите номер привычки, которую выполнили: '))
    for item in data:
        if choice == item['id']:
            item['completed'] = True
            item['last_complete'] = today.isoformat()
            save_data(data)
        else:
            print('Привычка отсутствует')
    print('Привычка отмечена!')
    
def delete():
    data = load_data()
    show_habits()
    choice = int(input('Введите номер привычки, которую хотите удалить: '))
    for item in data:
        if choice == item['id']:
            data.remove(item)
            save_data(data)
    print('Привычка успешно удалена.')
    