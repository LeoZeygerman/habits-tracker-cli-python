class Habit:
    
    def __init__(self, id, name, completed, streak, last_complete):
        self.id = id
        self.name = name
        self.completed = completed
        self.streak = streak
        self.last_complete = last_complete
        
    def show_habit(self):
        print(f'Номер привычки: {self.id} | Привычка: {self.name} | Выполнение: {self.completed} \n Серия: {self.streak} \n Последнее выполнение: {self.last_complete}')