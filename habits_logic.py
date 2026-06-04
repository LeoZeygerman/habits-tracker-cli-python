from storage import save_data, load_data

def add_habit():
    name = input('Введите название привычки: ')
    data = load_data()
    if len(data) == 0:
        new_id = 1
    else:
        new_id = data[-1]['new_id'] + 1
    habit = {
        'id': new_id,
        'name': name,
        'completed': False
    }
    data.append(habit)
    save_data(data)
    print('Привычка успешно добавлена.')