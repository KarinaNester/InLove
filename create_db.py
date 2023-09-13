import psycopg2

# Параметри підключення
db_params = {
    'dbname': 'inlove',
    'user': 'postgres',
    'password': 'postgre',
    'host': 'localhost',
    'port': '5432'  # Зазвичай 5432
}

# Підключення до бази даних
try:
    conn = psycopg2.connect(**db_params)
    print("Підключено до бази даних PostgreSQL!")

    # Тут ви можете виконувати SQL-запити або інші дії з базою даних

except (Exception, psycopg2.Error) as error:
    print("Помилка при підключенні до бази даних PostgreSQL:", error)

finally:
    # Закрийте підключення після використання
    if conn:
        conn.close()
        print("Підключення до бази даних закрито.")
