import json

def load_data():
    try:
        with open ('data/habits.json', 'r') as f:
            return json.load(f)
    except:
        return []
    
def save_data(data):
    with open('data/habits.json', 'w') as f:
        json.dump(data, f)