from flask import Flask, render_template
import calendar

app = Flask(__name__)


@app.route('/')
def index():
    # Create Calendar
    c = calendar.TextCalendar(calendar.SUNDAY)
    month = c.monthdatescalendar(2019, 6)
    return render_template('index.html', month=month)


if __name__ == '__main__':
    app.run()
