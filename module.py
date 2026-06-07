from datetime import date, datetime

class Habit:
    
    def __init__(self, id, name, completed, streak, last_complete, best_streak):
        self.id = id
        self.name = name
        self.completed = completed
        self.streak = streak
        self.last_complete = last_complete
        self.best_streak = best_streak
        
    def show_habit(self):
        print(f'Номер привычки: {self.id} | Привычка: {self.name} | Выполнение: {self.completed} \n Серия: {self.streak} \n Последнее выполнение: {self.last_complete}')
        
    def days_for_streak(self):
        today = date.today()
        if self.last_complete is None:
            self.streak = 1
            return
        last_date = datetime.strptime(self.last_complete, '%Y-%m-%d').date()
        difference = (today - last_date).days
        if difference == 1:
            self.streak += 1
            print(f'Ваша серия составляет: {self.streak}')
        elif difference == 0:
            print('Отмечено сегодня')
        elif difference > 0:
            self.streak = 0
            print(f'Серия утеряна: {self.streak}')
            