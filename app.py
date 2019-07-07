from flask import Flask, render_template
import calendar
import datetime
import os
import psycopg2
from DBCredentials import get_credentials

credentials = get_credentials()
database_name = credentials['Database']
database_user = credentials['User']
database_password = credentials['Password']
database_host = credentials['Host']
database_port = credentials['Port']
database_url = credentials['URL']
database_cli = credentials['Heroku_Cli']


conn = psycopg2.connect(dbname=database_name,
                        user=database_user,
                        password=database_password,
                        host=database_host,
                        port=database_port)



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
