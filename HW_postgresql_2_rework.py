import psycopg2     


def connect_db(database, user, password):  
    global conn
    conn = psycopg2.connect(database, user, password)
    with conn.cursor() as cur:
        print('Подключение установлено')     


def create_table(conn):     
    with conn.cursor() as cur:
        cur.execute("CREATE TABLE if not exist client(client_id SERIAL PRIMARY KEY, first_name TEXT, last_name TEXT, email TEXT);")
        print("Таблица создана") 


def create_table_phones(conn):     
    with conn.cursor() as cur:
        cur.execute("CREATE TABLE if not exist phones(client_id SERIAL PRIMARY KEY, client_id SERIAL foreign key references client(client_id), phone_number varchar (15) not null);")
        print("Таблица создана")
        conn.commit()      


def add_client():
    with conn.cursor() as cur:
        cur.execute("insert into client (client_id, first_name, last_name, email) values (%s, %s, %s, %s);", (1, "James", "Bond", "007@mi6.uk"))
        print("Данные клиента добавлены")


def add_phone():
    with conn.cursor() as cur:
        cur.execute("insert into phones (client_id, phone_number) values (%s, %s);", (1, "555-4444-333"))
        print("Добавлен  номер телефона клиента")


def update_data(tb_name, set_valeu, def_row, change_value, change_row):
        with conn.cursor() as cur:
            cur.execute(f"update {tb_name} set {set_row}=%s where {def_row}=%s;", (change_value, change_row))
            print("Данные клиента добавлены")


def del_phone(del_tb_name, del_def_row, del_row):
    with conn.cursor() as cur:
        cur.execute(f"delete from {del_tb_name} where {del_def_row}=%s;", (del_row))
        print("Телефон клиента удален")


def del_client(del_cl_tb, del_cl_row, del_cl_def):
    with conn.cursor() as cur:
        cur.execute(f"delete from {del+cl_tb} where {del_cl_row}=%s;", (del_cl_def))
        print("Клиент удален")


def find_client(fd_cl_row, fd_cl_tb, set_cl_row, fd_item):
    with conn.cursor() as cur:
        cur.execute(f"select {fd_cl_row} from {fd_cl_tb} where {set_cl_row}=%s;", (fd_item))
        print("Клиент найден")
        print(cur.fetchone())


database="clients_db"
user="postgres"
password="131313Zz"

tb_name = 'client'
set_value = 'email'
def_row = 'id'
change_value = '007@mi-6.uk'
change_row = 1

del_tb_name = 'phones'
del_def_row = 'phone_number'
del_row = '555-4444-333'

del_cl_tb = 'client'
del_cl_row = 'id'
del_cl_def = '1'

fd_cl_row = 'client_id' 
fd_cl_tb = 'client' 
set_cl_row = 'first_name'
fd_item = 'James'

if __name__ == "__main__":
    connect_db(database, user, password)
    create_table(conn)
    create_table_phones(conn)
    add_client()
    add_phone()
    update_data(db_name, set_value, def_row, change_value, change_row)
    del_phone(del_db_name, del_def_row, del_row)
    del_client(del_cl_tb, del_cl_row, del_cl_def)
    find_client(fd_cl_row, fd_cl_tb, set_cl_row, fd_item)
    conn.close()

