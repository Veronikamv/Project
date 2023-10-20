import tkinter as tk
import sqlite3

# Создание соединения с базой данных
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

# Создание таблицы сотрудников
cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   full_name TEXT,
                   phone_number TEXT,
                   email TEXT,
                   salary REAL)''')

# Функция для добавления нового сотрудника
def add_employee():
    full_name = name_entry.get()
    phone_number = phone_entry.get()
    email = email_entry.get()
    salary = float(salary_entry.get())

    cursor.execute('''INSERT INTO employees (full_name, phone_number, email, salary)
                      VALUES (?, ?, ?, ?)''', (full_name, phone_number, email, salary))
    conn.commit()
    status_label.config(text="Сотрудник успешно добавлен!")

# Функция для изменения данных сотрудника
def update_employee():
    employee_id = int(id_entry.get())
    full_name = name_entry.get()
    phone_number = phone_entry.get()
    email = email_entry.get()
    salary = float(salary_entry.get())

    cursor.execute('''UPDATE employees SET full_name=?, phone_number=?, email=?, salary=?
                      WHERE id=?''', (full_name, phone_number, email, salary, employee_id))
    conn.commit()
    status_label.config(text="Данные сотрудника успешно обновлены!")

# Функция для удаления сотрудника
def delete_employee():
    employee_id = int(id_entry.get())

    cursor.execute("DELETE FROM employees WHERE id=?", (employee_id,))
    conn.commit()
    status_label.config(text="Сотрудник успешно удален!")

# Функция для поиска сотрудника по ФИО
def search_employee():
    full_name = search_entry.get()

    cursor.execute("SELECT * FROM employees WHERE full_name=?", (full_name,))
    result = cursor.fetchall()

    if len(result) > 0:
        result_text = ""
        for row in result:
            result_text += f"ID: {row[0]}\n"
            result_text += f"ФИО: {row[1]}\n"
            result_text += f"Номер телефона: {row[2]}\n"
            result_text += f"Email: {row[3]}\n"
            result_text += f"Заработная плата: {row[4]}\n"
            result_text += "----------------------\n"
        search_result_text.config(text=result_text)
    else:
        search_result_text.config(text="Сотрудник не найден.")

# Создание графического интерфейса
root = tk.Tk()
root.title("Список сотрудников компании")

# Label и Entry для ID
id_label = tk.Label(root, text="ID сотрудника:")
id_label.pack()
id_entry = tk.Entry(root)
id_entry.pack()

# Label и Entry для ФИО
name_label = tk.Label(root, text="ФИО:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

# Label и Entry для номера телефона
phone_label = tk.Label(root, text="Номер телефона:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

# Label и Entry для адреса электронной почты
email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

# Label и Entry для заработной платы
salary_label = tk.Label(root, text="Заработная плата:")
salary_label.pack()
salary_entry = tk.Entry(root)
salary_entry.pack()

# Кнопка для добавления сотрудника
add_button = tk.Button(root, text="Добавить сотрудника", command=add_employee)
add_button.pack()

# Кнопка для изменения данных сотрудника
update_button = tk.Button(root, text="Изменить сотрудника", command=update_employee)
update_button.pack()

# Кнопка для удаления сотрудника
delete_button = tk.Button(root, text="Удалить сотрудника", command=delete_employee)
delete_button.pack()

# Label и Entry для поиска сотрудника по ФИО
search_label = tk.Label(root, text="Поиск по ФИО:")
search_label.pack()
search_entry = tk.Entry(root)
search_entry.pack()
# Кнопка для поиска сотрудника
search_button = tk.Button(root, text="Найти сотрудника", command=search_employee)
search_button.pack()

# Label для вывода результатов поиска
search_result_text = tk.Label(root, text="")
search_result_text.pack()

# Status Label для вывода сообщений о статусе операции
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()

# Закрытие соединения с базой данных
conn.close()
