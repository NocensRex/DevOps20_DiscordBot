from ics import Calendar
from datetime import date
import requests
import arrow

url = "https://cloud.timeedit.net/nackademin/web/1/ri6855Qy1098n6QZ2YQ3Q7ZQZ6607.ics"
r = requests.get(url).text
time_now = arrow.utcnow()

c = Calendar(r)

today_lessons = list(c.timeline.today())

nxt_lesson = list(c.timeline.start_after(time_now))[0]

def next_lesson(lesson=nxt_lesson):
    time_begin = arrow.get(lesson.begin)
    local = time_begin.to('local').format('YYYY-MM-DD HH:mm')
    name = lesson.name
    location = lesson.location

    if location == "Digital undervisning":
        return f'Nästa lektion är "{name}", den börjar {local} och den är på Zoom'
    else:
        return f'Nästa lektion är "{name}", den börjar {local} och är i sal {location}'

def this_day(lesson=today_lessons):
    items = []
    items.append("Dagens schema:")
    for item in lesson:
        time_begin = arrow.get(item.begin)
        time_end = arrow.get(item.end)
        local_begin = time_begin.to('local').format('HH:mm')
        local_end = time_end.to('local').format('HH:mm')

        if item.location == "Digital undervisning":
            items.append(f'{local_begin} - {local_end}, "{item.name}", på Zoom')
        else:
            items.append(f'{local_begin} - {local_end}, "{item.name}", i sal {item.location}')
    return items

def local_time():
    pass