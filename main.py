from datetime import datetime
from dateutil import relativedelta
from dateutil import parser


start_working = datetime(1900, 1, 1, 9)
finish_working = datetime(1900, 1, 1, 21)
session_endurance = 30
pattern = ('%H:%M')
result = []

busy = [
{'start' : '10:30',
'stop' : '10:50'
},
{'start' : '18:40',
'stop' : '18:50'
},
{'start' : '14:40',
'stop' : '15:50'
},
{'start' : '16:40',
'stop' : '17:20'
},
{'start' : '20:05',
'stop' : '20:20'
}
]

while start_working <= finish_working - relativedelta.relativedelta(minutes=session_endurance):
    window_start = start_working
    window_end = window_start + relativedelta.relativedelta(minutes=session_endurance)
    for busy_time in busy:
        flag = True
        busy_start = datetime.strptime(busy_time['start'], pattern)
        busy_end = datetime.strptime(busy_time['stop'], pattern)

        if busy_start <= window_start < busy_end or busy_start < window_end <= busy_end or (window_start <= busy_start and window_end >= busy_end):
            flag = False
            start_working = busy_end
            break
    if flag == True:
        result.append([window_start, window_end])
        start_working = window_end

print(*map(lambda time: f'{time[0].strftime(pattern)} - {time[1].strftime(pattern)}', result), sep='\n')