from ics import Calendar
from datetime import date
from dotenv import load_dotenv

import requests
import arrow
import os

load_dotenv()
url = os.getenv('URL')

r = requests.get(url).text
time_now = arrow.utcnow()
c = Calendar(r)

today_lessons = list(c.timeline.today())
nxt_lesson = list(c.timeline.start_after(time_now))[0]

def next_lesson(lesson=nxt_lesson):
    local = local_time(lesson.begin)
    name = lesson.name
    location = lesson.location

    if location == "Digital undervisning":
        return f'Nästa lektion är "{name}", den börjar {local} och den är på Zoom'
    else:
        return f'Nästa lektion är "{name}", den börjar {local} och är i sal {location}'

def this_day(lesson=today_lessons):
    items = []
    if not lesson:
        items.append("Inga lektioner idag.")
        return items

    else:
        items.append("Dagens schema:")
        for item in lesson:
            local_begin = local_time(item.begin)
            local_end = local_time(item.end)

            if item.location == "Digital undervisning":
                items.append(f'{local_begin} - {local_end}, "{item.name}", på Zoom')
            else:
                items.append(f'{local_begin} - {local_end}, "{item.name}", i sal {item.location}')
        return items

def local_time(utctime):
    time = arrow.get(utctime)
    local = time.to('local').format('HH:mm')
    return local

print(next_lesson())