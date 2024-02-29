import sqlite3


def display_menu(conn):
    print('Вы можете отобразить список учеников по выбранному '
          'id города из перечня городов ниже, для выхода из программы введите 0:')
    sql = ''' SELECT cities.id, cities.title FROM cities '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        list_cities = cursor.fetchall()
        for citi in list_cities:
            print(f'{citi}')
    except sqlite3.Error as err:
        print(f"Error {err}")


def get_students_by_city(conn, city_id):
    sql = '''SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area FROM students 
    INNER JOIN countries ON cities.country_id = countries.id
    INNER JOIN cities ON cities.id = students.city_id WHERE cities.id = ?  
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (city_id,))
        lis_student = cursor.fetchall()
        for student in lis_student:
            print(student)
    except sqlite3.Error as err:
        print(f"Error {err}")


def main(conn):
    while True:
        display_menu(conn)
        selected_option = int(input("Введите id города (от 1 до 7): "))
        if selected_option == 0:
            print("Выход из программы.")
            break
        elif selected_option <= 7:
            get_students_by_city(conn, selected_option)

        else:
            print("Неверный ввод. Пожалуйста, введите число от 0 до 7.")


conn = sqlite3.connect('HW8.db')

if conn:
    main(conn)
    conn.close()
