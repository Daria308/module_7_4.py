team1_num = 5 # количество участников 1й команды
team2_num = 6 # количество участников 2й команды

score_1 = 40 # кол-во задач, решенных командой 1
score_2 = 42 # кол-во задач, решенных командой 2

team1_time = 1552.512 # время, за которое команда 1 решила задачи

team2_time = 2153.31451 # время, за которое команда 2 решила задачи

print('В команде Мастера кода участников: %s!' % team1_num)
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))

print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print('Волшебники данных решили задачи за {} с!'.format(team2_time))

print(f'Команды решили {score_1} и {score_2} задач.')

# Исход соревнования
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'

elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'

else:
    challenge_result = 'Ничья!'

print(f'Результат битвы: {challenge_result}')


# Количество задач, среднее время решения
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')