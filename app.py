from flask import Flask, render_template
import calendar
import datetime
import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

app = Flask(__name__)


@app.route('/')
def index():
    # Create Calendar
    today = datetime.date.today()
    c = calendar.TextCalendar(calendar.SUNDAY)
    month = c.monthdatescalendar(today.year, today.month)
    monthTitle = today.strftime("%B %Y")
    return render_template('test2.html', month=month, today=today, monthTitle=monthTitle)


if __name__ == '__main__':
    app.run()
