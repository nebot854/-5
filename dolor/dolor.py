import sqlite3
import matplotlib.pyplot as plt


def get_data(start_date, end_date):
    con = sqlite3.connect('./dolor/data.db')
    cur = con.cursor()
    cur.execute("""
CREATE TABLE IF NOT EXISTS data (
    data TEXT
    price REAL)""")
    cur.execute("SELECT * FROM data WHERE date BETWEEN ? AND ? ORDER BY date ", (start_date, end_date))
    res = cur.fetchall()
    con.close()
    dates = [res[i][0] for i in range(len(res))]
    prices = [res[i][1] for i in range(len(res))]
    return dates, prices

def dolor_date(dates,prices):
    
    plt.figure(figsize=(8, 6))
    plt.plot(dates[::100], prices[::100], marker='o', color='r', linestyle='--')
    plt.title('курс долора')
    plt.xlabel('дата')
    plt.ylabel('цена в рублях')
    plt.grid(True)
    plt.show()

dates , prices = get_data('2018','2022')
dolor_date(dates,prices)