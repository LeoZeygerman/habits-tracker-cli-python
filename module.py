from datetime import date

class Habit:
    
    def __init__(self, id, name, completed, streak, last_complete, best_streak):
        self.id = id
        self.name = name
        self.completed = completed
        self.streak = streak
        self.last_complete = date.fromisoformat(last_complete)
        self.best_streak = best_streak
        
    def show_habit(self):
        print(f'Номер привычки: {self.id} | Привычка: {self.name} | Выполнение: {self.completed} \n Серия: {self.streak} \n Последнее выполнение: {self.last_complete}')
        
    def days_for_streak(self):
        today = date.today()
        difference = (today - self.last_complete).days
        
        if difference == 1:
            self.streak += 1
            print(f'Ваша серия составляет: {self.streak}')
        elif difference == 0:
            print('Отмечено сегодня')
        elif difference > 0:
            self.streak = 0
            print(f'Серия утеряна: {self.streak}')
            