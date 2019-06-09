from flask import Flask, render_template
import calendar
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    # Create Calendar
    today = datetime.date.today()
    c = calendar.TextCalendar(calendar.SUNDAY)
    month = c.monthdatescalendar(today.year, today.month)
    return render_template('index.html', month=month, today=today)


if __name__ == '__main__':
    app.run()
