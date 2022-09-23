import psycopg2     


def connect_db():  
    try:
        global conn
        conn = psycopg2.connect(database="clients_db", user="postgres", password="131313Zz")
        with conn.cursor() as cur:
            print('Подключение установлено')
            conn.commit()        
    except:
        print("Подключение не установлено")


def create_table(conn):     
    try:
        with conn.cursor() as cur:
            cur.execute("CREATE TABLE client(client_id SERIAL PRIMARY KEY, first_name TEXT, last_name TEXT, email TEXT,phones ARRAY);")
            print("Таблица создана")
            conn.commit()      
    except:
        print("Таблица уже существует либо произошла ошибка")


def add_client():
    try:
        with conn.cursor() as cur:
            cur.execute("insert into client (client_id, first_name, last_name, email) values (%s, %s, %s, %s);", (1, "James", "Bond", "007@mi6.uk",))
            print("Данные клиента добавлены")
            conn.commit()      
    except:
        print("Данные клиента уже существуют либо произошла ошибка")


def add_phone():
    try:
        with conn.cursor() as cur:
            cur.execute("insert into client (phones) values (%s);", ("555-4444-333",))
            print("Добавлен один номер клиента")
            conn.commit()      
    except:
        print("Этот номер уже указан либо произошла ошибка")


def update_data():
    try:
        with conn.cursor() as cur:
            cur.execute("update client set email=%s where id=%s;", ('007@mi6.uk', 1))
            print("Данные клиента добавлены")
            conn.commit()      
    except:
        print("Данные клиента уже существуют либо произошла ошибка")


def del_phone():
    try:
        with conn.cursor() as cur:
            cur.execute("update client set phones=%s where id=%s;", (phones[2],Null))
            print("Телефон клиента удален")
            conn.commit()      
    except:
        print("Этот номер уже удален либо произошла ошибка")


def del_client():
    try:
        with conn.cursor() as cur:
            cur.execute("delete from client where id=%s;", (1,))
            print("Клиент удален")
            conn.commit()      
    except:
        print("Клиент уже удален либо произошла ошибка")


def find_client():
    try:
        with conn.cursor() as cur:
            cur.execute("select client_id from client where first_name=%s;", ('James',))
            print("Клиент найден")
            print(cur.fetchone())
            conn.commit()      
    except:
        print("Клиент не найден либо произошла ошибка")


connect_db()
create_table(conn)
add_client()
add_phone()
update_data()
del_phone()
del_client()
find_client()

conn.close()
