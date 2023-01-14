import sqlite3 as sq
from typing import NamedTuple


class Customer(NamedTuple):
    id: int
    telegram_id: int
    name: str
    city: str


class Worker(NamedTuple):
    id: int
    telegram_id: int
    name: str
    category: str
    description: str
    address: str
    contact: str


def create_table() -> None:
    with sq.connect('freelance.db') as connection:
        cursor = connection.cursor()
    cursor.execute(f""" CREATE TABLE IF NOT EXISTS customer(
                       id INTEGER DEFAULT 1 PRIMARY KEY AUTOINCREMENT, 
                       name TEXT NOT NULL ,
                       telegram_id INTEGER , 
                       city TEXT NOT NULL DEFAULT EARTH) """)


def save_customer(name: str, city: str, telegram_id: int) -> int:
    with sq.connect('freelance.db') as connection:
        try:
            cursor = connection.cursor()
            cursor.execute(f"""INSERT INTO customer (name, city, telegram_id) VALUES('{name}', '{city}', {telegram_id})""")
        except sq.IntegrityError:
            return -1


def save_worker(telegram_id: int, name: str, category: str, description: str, address: str, contact: str) -> str:
    with sq.connect('workers.db') as connection:
        try:
            cursor = connection.cursor()
            cursor.execute(f"""INSERT INTO worker 
            (telegram_id, name, category, description, address, contact) 
            VALUES({telegram_id}, '{name}', '{category}', '{description}', '{address}', '{contact}')""")
        except sq.IntegrityError:
            return 'You are already in DB'


def find_worker(category: str) -> list[Worker]:
    with sq.connect('workers.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f"""SELECT * FROM worker WHERE category='{category}'""")
        results = cursor.fetchall()
        workers = list()
        for result in results:
            worker = Worker(
                id=result[0],
                telegram_id=result[1],
                name=result[2].replace('\n', ''),
                category=result[3].replace('\n', ''),
                description=result[4].replace('\n', ''),
                address=result[5].replace('\n', ''),
                contact=result[6].replace('\n', '')
            )
            workers.append(worker)

        return workers


def is_customer_in_db(telegram_id: int) -> bool:
    with sq.connect('freelance.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f"""SELECT * FROM customer WHERE telegram_id={telegram_id}""")
        result = cursor.fetchone()
        if result:
            return True
    return False


def is_worker_in_db(telegram_id: int) -> bool:
    with sq.connect('workers.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f"""SELECT * FROM worker WHERE telegram_id={telegram_id}""")
        result = cursor.fetchone()
        if result:
            return True
    return False


def get_customer(telegram_id: int) -> Customer:
    with sq.connect('freelance.db') as connection:
        cursor = connection.cursor()
    # cursor.execute(f"""SELECT * FROM customer;""")
        cursor.execute(f"""SELECT * FROM customer WHERE telegram_ID = {telegram_id}""")
        res_tuple = cursor.fetchone()
        # if there is a customer in db return it
        if res_tuple:
            return Customer(id=int(res_tuple[0]),
                            telegram_id=int(telegram_id),
                            name=str(res_tuple[1]),
                            city=str(res_tuple[3]))
        # if there is no customer return void Customer object to
        # represent his absence
        else:
            return Customer(id=-1,
                            telegram_id=-1,
                            name='',
                            city='')


create_table()
