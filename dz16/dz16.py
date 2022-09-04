#дз16 - работа с db api
import sqlite3

connection = sqlite3.connect('sport.sqlite')
cursor = connection.cursor()

#создание таблиц
# query = '''
# create table competition
# (
# id int not null primary key,
# name varchar(20),
# world_record int,
# set_date date
# )'''
# cursor.execute(query)
# query = '''
# create table sportsman
# (
# id int not null primary key,
# name varchar(30),
# rank int, 
# year_of_birth year(4),
# personal_record int,
# country varchar(30)
# )'''
# cursor.execute(query)
# query = '''
# create table result
# (
# competition_id int not null references competition(id),
# sportsman_id int not null references sportsman(id),
# result varchar(30), 
# city varchar(30),
# hold_date date
# )'''
# cursor.execute(query)

# connection.commit()

#заполенение таблиц данными
# query = '''
# insert into competition values
# (1, 'Mister Universe', 8, '1980-03-16'),
# (2, 'Mister Olimpia', 13, '1992-04-23'),
# (3, 'Olimpia', 18, '1990-02-28'),
# (4, 'Universiada', 30, '1996-01-23')'''
# cursor.execute(query)
# query = '''
# insert into sportsman values
# (1001, 'Ivan Usachev', 3, '1972', 16, 'Russia'),
# (1002, 'Robert Fischer', 1, '1964', 10, 'USA'),
# (1003, 'Sancho Pansa', 3, '1986', 18, 'Spain'),
# (1004, 'Gallileo Ruben', 2, '1948', 15, 'France')'''
# cursor.execute(query)
# query = '''
# insert into result values
# (1, 1002, 15, 'Atlanta', '1996-04-30'),
# (1, 1003, 18, 'Atlanta', '1996-04-30'),
# (1, 1004, 8, 'Atlanta', '1996-04-30'),
# (2, 1001, 19, 'Oslo', '2000-02-18'),
# (4, 1003, 14, 'Moscow', '2008-03-11')'''
# cursor.execute(query)

# connection.commit()

#запросы
#таблица sportsman
print('Таблица sportsman')
cursor.execute('select * from sportsman')
for row in cursor.fetchall():
    print(row)
print()

#таблица competition
print('Таблица competition')
cursor.execute('select * from competition')
for row in cursor.fetchall():
    print(row)
print()

#таблица result
print('Таблица result')
cursor.execute('select * from result')
for row in cursor.fetchall():
    print(row)
print()

#наименование и мировые результаты по всем соревнованиям
print('наименование и мировые результаты по всем соревнованиям')
cursor.execute('select name, world_record from competition')
for row in cursor.fetchall():
    print(row)
print()

print ('Имена всех спортсменов, которые родились в 1990 году:')
cursor.execute('select name from sportsman where year_of_birth = "1990"')
for row in cursor.fetchall():
    print(row)
print()

print ('Наименование и мировые результаты по всем соревнованиям' + 
'установеленные 12.05.2010 или 15.05.2010:')
cursor.execute('select name, world_record from competition where set_date = "2010-05-12" or set_date = "2010-05-15"')
for row in cursor.fetchall():
    print(row)
print()

print ('Даты проведения соревнований, проводившихся в Москве и ' + 
'полученные результаты равны 10 секунд')
cursor.execute('select hold_date from result where city = "Moscow" and result = "10"')
for row in cursor.fetchall():
    print(row)
print()

print ('Имена всех спортсменов у которых персональный рекорд менее 25с')
cursor.execute('select name from sportsman where personal_record < 25')
for row in cursor.fetchall():
    print(row)
print()

print ('Список стран, спортсмены которых никогда не занимали 1-х мест')
cursor.execute('select country from sportsman where rank != 1')
for row in cursor.fetchall():
    print(row)
print()
