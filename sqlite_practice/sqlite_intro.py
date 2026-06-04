import sqlite3

# ========== ЗАДАНИЕ 2-9: БАЗОВЫЕ ОПЕРАЦИИ ==========
print("=" * 50)
print("ЗАДАНИЯ 2-9: Работа с таблицей users")
print("=" * 50)

# Подключаемся к базе данных
conn = sqlite3.connect('mybase.db')
cursor = conn.cursor()

# Задание 3: Создаём таблицу users
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
''')
conn.commit()
print("✓ Таблица users создана!")

# Задание 4: Добавляем данные (INSERT)
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Анна', 25))
users = [('Иван', 30), ('Мария', 22), ('Петр', 35)]
cursor.executemany('INSERT INTO users (name, age) VALUES (?, ?)', users)
conn.commit()
print("✓ Пользователи добавлены!")

# Задание 5: Читаем данные (SELECT)
cursor.execute('SELECT * FROM users')
all_users = cursor.fetchall()
print("\n--- Все пользователи ---")
for user in all_users:
    print(f"  id: {user[0]}, имя: {user[1]}, возраст: {user[2]}")

# Задание 6: Читаем с условием (WHERE)
cursor.execute('SELECT * FROM users WHERE age > 25')
older_users = cursor.fetchall()
print("\n--- Пользователи старше 25 ---")
for user in older_users:
    print(f"  id: {user[0]}, имя: {user[1]}, возраст: {user[2]}")

# Задание 7: Изменяем данные (UPDATE)
cursor.execute('UPDATE users SET age = age + 1')
conn.commit()
cursor.execute('SELECT * FROM users')
updated_users = cursor.fetchall()
print("\n--- После увеличения возраста на 1 год ---")
for user in updated_users:
    print(f"  id: {user[0]}, имя: {user[1]}, возраст: {user[2]}")

# Задание 8: Удаляем данные (DELETE)
cursor.execute('DELETE FROM users WHERE id = ?', (2,))
conn.commit()
cursor.execute('SELECT * FROM users')
remaining_users = cursor.fetchall()
print("\n--- После удаления id=2 ---")
for user in remaining_users:
    print(f"  id: {user[0]}, имя: {user[1]}, возраст: {user[2]}")

# Закрываем соединение (Задание 9)
conn.close()
print("\n✓ Соединение закрыто.")

# ========== ЗАДАНИЕ 10-17: ТАБЛИЦА PRODUCTS ==========
print("\n" + "=" * 50)
print("ЗАДАНИЯ 10-17: Работа с таблицей products")
print("=" * 50)

# Открываем новое соединение
conn = sqlite3.connect('mybase.db')
cursor = conn.cursor()

# Задание 10: Создаём таблицу products
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price INTEGER NOT NULL,
        quantity INTEGER DEFAULT 0
    )
''')
conn.commit()
print("✓ Таблица products создана!")

# Задание 11: Добавляем товары
products_data = [
    ('Яблоки', 50, 100),
    ('Бананы', 80, 50),
    ('Молоко', 70, 30),
    ('Хлеб', 40, 0),
    ('Сыр', 150, 20)
]
cursor.executemany('INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)', products_data)
conn.commit()
print("✓ Товары добавлены!")

# Задание 12: Выводим все товары
cursor.execute('SELECT * FROM products')
print("\n--- Все товары ---")
for product in cursor.fetchall():
    print(f"  {product[0]}. {product[1]} - {product[2]} руб, в наличии: {product[3]}")

# Задание 13: Товары с ценой меньше 100 рублей
cursor.execute('SELECT * FROM products WHERE price < 100')
print("\n--- Товары дешевле 100 руб ---")
for product in cursor.fetchall():
    print(f"  {product[1]} - {product[2]} руб")

# Задание 14: Товары, которых нет в наличии
cursor.execute('SELECT * FROM products WHERE quantity = 0')
print("\n--- Товары, которых нет в наличии ---")
for product in cursor.fetchall():
    print(f"  {product[1]}")

# Задание 15: Увеличиваем цену всех товаров на 10 рублей
cursor.execute('UPDATE products SET price = price + 10')
conn.commit()
cursor.execute('SELECT * FROM products')
print("\n--- После увеличения цены на 10 руб ---")
for product in cursor.fetchall():
    print(f"  {product[1]} - {product[2]} руб (было {product[2]-10} руб)")

# Задание 16: Удаляем товары с ценой выше 100 рублей
cursor.execute('DELETE FROM products WHERE price > 100')
conn.commit()
print("\n✓ Товары с ценой выше 100 руб удалены!")

# Проверяем результат удаления
cursor.execute('SELECT * FROM products')
print("\n--- Оставшиеся товары ---")
for product in cursor.fetchall():
    print(f"  {product[1]} - {product[2]} руб, в наличии: {product[3]}")

# Задание 17: Добавляем поле category
cursor.execute('ALTER TABLE products ADD COLUMN category TEXT DEFAULT "другое"')
conn.commit()
print("\n✓ Поле 'category' добавлено!")

# Заполняем категории
categories = [
    ('фрукты', 'Яблоки'),
    ('фрукты', 'Бананы'),
    ('молочные', 'Молоко'),
    ('выпечка', 'Хлеб')
]
for category, name in categories:
    cursor.execute('UPDATE products SET category = ? WHERE name = ?', (category, name))
conn.commit()
print("✓ Категории заполнены!")

# Выводим финальный результат
cursor.execute('SELECT * FROM products')
print("\n--- Финальная таблица products ---")
for product in cursor.fetchall():
    print(f"  id:{product[0]}, {product[1]}, цена:{product[2]} руб, в наличии:{product[3]}, категория:{product[4]}")

# Закрываем соединение
conn.close()
print("\n✓ Соединение закрыто.")

# ========== ВОПРОСЫ ДЛЯ ПРОВЕРКИ ==========
print("\n" + "=" * 50)
print("ВОПРОСЫ ДЛЯ ПРОВЕРКИ ЗНАНИЙ")
print("=" * 50)
questions = [
    "1. Как подключиться к базе данных SQLite в Python?",
    "2. Что делает cursor.execute()?",
    "3. Зачем нужен conn.commit()?",
    "4. Что означает '?' в запросе INSERT INTO users (name, age) VALUES (?, ?)?",
    "5. Как получить все строки из таблицы?",
    "6. Чем отличается fetchone() от fetchall()?",
    "7. Как обновить данные в таблице?",
    "8. Как удалить данные из таблицы?"
]
for q in questions:
    print(f"  {q}")
print("\n  Ответы в конце файла!")
