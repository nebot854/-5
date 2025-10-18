import sqlite3
from config import DATABASE

skills = [(_,) for _ in (['мало денег', 'норм денег', 'много денег', 'Бизнесмен'])]
statuses = [(_,) for _ in (['еда', 'одежда', "ипотека или кредит", "крупная покупка"])]

class DB_Managr:
    def __init__(self, database):
        self.database = database

    def create_tables(self):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute('''CREATE TABLE projects (
                            project_id INTEGER PRIMARY KEY,
                            user_id INTEGER,
                            eat TEXT NOT NULL,
                            pokypka TEXT ,
                            tratu ,                                                                        
                            status_id INTEGER,                          
                            FOREIGN KEY(status_id) REFERENCES status(status_id)
                        )''')                                  
            conn.execute('''CREATE TABLE status (
                            status_id INTEGER PRIMARY KEY,
                            uzvest TEXT
                        )''')
            conn.commit()
        print("База данных успешно создана.")

    def __executemany(self, sql, data):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.executemany(sql, data)
            conn.commit()

    def __select_data(self, sql, data=tuple()):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute(sql, data)
            return cur.fetchall()
            
        sql = 'INSERT OR IGNORE INTO status (uzvest) values(?)'
        data = statuses
        self.__executemany(sql, data)

    def insert_project(self, data):
        sql = 'INSERT OR IGNORE INTO projects (user_id, eat, tratu, status_id) values(?, ?, ?, ?)'
        self.__executemany(sql, data)


    def get_statuses(self):
        sql='SELECT uzvest from status'
        return self.__select_data(sql)

    def get_status_id(self, uzvest):
        sql = 'SELECT status_id FROM status WHERE uzvest = ?'
        res = self.__select_data(sql, (uzvest,))
        if res: 
            return res[0][0]
        else: 
            return None

    def get_projects(self, user_id):
                return self.__select_data(sql='SELECT * FROM projects WHERE user_id = ?', data=(user_id,))

    def get_project_id(self, eat, user_id):
        return self.__select_data(sql='SELECT project_id FROM projects WHERE eat = ? AND user_id = ?', data=(eat, user_id))[0][0]


if __name__ == '__main__':
    manager = DB_Managr(DATABASE)
    manager.create_tables() 