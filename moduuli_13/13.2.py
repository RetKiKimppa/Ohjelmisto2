import mysql.connector
from flask import Flask, request

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='lentokentat',
    user='kim',
    password='1111',
    autocommit=True
)

app = Flask(__name__)
app@route('/kenttä/<icao>')

def lentokenttahaku(icao):
    sql = f"SELECT name FROM airport WHERE ident='{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            vastaus = {
                "Name": rivi[0],
                "ICAO": icao
            }
    else:
        vastaus = {
            "Name": 'not found',
        }
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host="127.0.0.1", port=3000)


