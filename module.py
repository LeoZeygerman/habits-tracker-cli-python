class Habit:
    
    def __init__(self, id, name, completed):
        self.id = id
        self.name = name
        self.completed = completed
        
    def show_habit(self):
        print(f'Номер привычки: {self.id} | Привычка: {self.name} | Выполнение: {self.completed}')