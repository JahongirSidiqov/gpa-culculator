import psycopg2.extras
import psycopg2


def connect_db():
    conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user='postgres',
        password='123456')
    return conn


def insert_data(culculs, english, fizika, as1, philosophy, programming):
    conn = connect_db()
    cur = conn.cursor()
    print("DATA ENTRING", culculs)
    cur.execute('INSERT INTO gpa1 (calculus, english, fizika, akademik_nutq, falsafa, dasturlash)'
                'VALUES (%s, %s, %s, %s, %s, %s)',
                (int(culculs), int(english), int(fizika), int(as1), int(philosophy), int(programming))
                )
    conn.commit()
    cur.close()
    conn.close()

def select_data():
    conn = connect_db()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("""
        SELECT AVG(calculus),AVG(english),AVG(fizika),AVG(falsafa),AVG(akademik_nutq),AVG(dasturlash) FROM gpa1;
        """)
    marks = cur.fetchall()
    cur.close()
    conn.close()
    return marks