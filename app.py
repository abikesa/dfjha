from flask import Flask, render_template
import csv

app = Flask(__name__)

def load_data():
    with open('data.csv', newline='') as f:
        reader = csv.DictReader(f)
        return list(reader)

@app.route('/')
def dashboard():
    data = load_data()
    for person in data:
        cortisol = float(person['cortisol'])
        if cortisol > 20:
            person['symbol'] = '🌊 Dionysian (Frenzy)'
            person['color'] = 'red'
        elif cortisol > 15:
            person['symbol'] = '❤️ Ares (Action)'
            person['color'] = 'orange'
        else:
            person['symbol'] = '🐬 Hermes (Flow)'
            person['color'] = 'blue'
    return render_template('dashboard.html', people=data)

# 🔥 This is the part you're missing
if __name__ == '__main__':
    app.run(debug=True)
