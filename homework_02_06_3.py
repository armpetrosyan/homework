hour = int(input('Enter hour: '))
am_pm = input('am or pm: ')
hr_ahead = int(input('How many hours ahead: 121'))

new_hour = (hour + hr_ahead) % 12

if new_hour == 0:
    new_hour = 12

if am_pm == 'am' and hour + hr_ahead > 12:
    print(new_hour, 'pm')
else:
    print(new_hour, 'am')
