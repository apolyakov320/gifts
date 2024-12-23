from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


# база данных
def init_db():
    conn = sqlite3.connect('gifts.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gifts (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            gift TEXT NOT NULL,
            price REAL NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    cursor.executemany('''
        INSERT INTO gifts (name, gift, price, status) VALUES (?, ?, ?, ?)
    ''', [
        ('Фомичёв Аверкий Рудольфович', 'Часы', 2150.00, 'не куплен'),
        ('Фролов Исак Мартынович', 'Книга', 1500.00, 'куплен'),
        ('Смирнов Леонид Еремеевич', 'Духи', 1330.00, 'не куплен'),
        ('Ермаков Игнат Авдеевич', 'Подарочная карта', 2500.00, 'куплен'),
        ('Рыбаков Юлиан Фролович', 'Наушники', 1750.00, 'не куплен'),
        ('Владимирова Дарьяна Ильяновна', 'Кофейные зерна', 1600.00, 'куплен'),
        ('Кириллова Галина Мэлсовна', 'Настольная игра', 2220.00, 'не куплен'),
        ('Котова Вида Феликсовна', 'Кактус', 1330.00, 'куплен'),
        ('Потапова Елизавета Митрофановна', 'Кружка', 1520.00, 'не куплен'),
        ('Суворова Юланта Оскаровна', 'Худи', 2000.00, 'куплен')
    ])
    conn.commit()
    conn.close()

    @app.route('/')
    def index():
      conn = sqlite3.connect('gifts.db')
      cursor = conn.cursor()
      cursor.execute('SELECT * FROM gifts')
      gifts = cursor.fetchall()
      conn.close()
      return render_template('index.html', gifts=gifts)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)