from bs4 import BeautifulSoup
import re
import json

timetable = {}
subject_list = []
with open("soup.html", "r") as soup_html:
    soup = BeautifulSoup(soup_html, "html.parser")
    subjects = soup.find_all(id='id')
    for subject in subjects:
        subject_name = str(subject.find('caption').text)
        timetable[subject_name] = list()
        schedules = subject.find_all('tr')
        date_list = []
        slot_list = []
        room_list = []
        for schedule in schedules[1:]:
            values = schedule.find_all('td')
            date_href = values[0].find('a').get('href')
            date = re.search('day=(.+)', date_href)
            date_list.append(date.group(1))
            slot_list.append(values[1].text)
            room_list.append(values[2].find('a').text)

        # Start Time (date):
        # ISO 8601 format: YYYY-MM-DDThh:mm:ss+00:00.
        # The +00:00 is the timezone offset.
        # E.g: 2019-10-12T07:20:50.52Z
        #      2019-10-12T07:20:50.52+00:00 (UTC+0)
        #      2019-10-12T14:20:50.52+07:00 (UTC+7)
        #      2019-10-12T03:20:50.52-04:00 (UTC-4)
        # T stands for the signal of the end of date
        # Z stands for Zero timezone, the UTC+0 (or GTM+0) timezone
        #
        # RFC 3339 format: omission of T is acceptable
        # E.g: 2019-10-12 07:20:50.52Z

        start_time =\
            {'1': '07:00:00+07:00',
             '2': '08:45:00+07:00',
             '3': '10:30:00+07:00',
             '4': '12:30:00+07:00',
             '5': '14:15:00+07:00',
             '6': '16:00:00+07:00'}
        end_time =\
            {'1': '08:30:00+07:00',
             '2': '10:15:00+07:00',
             '3': '12:00:00+07:00',
             '4': '14:00:00+07:00',
             '5': '15:45:00+07:00',
             '6': '17:30:00+07:00'}

        for i in range(len(date_list)):
            timetable[subject_name].append(
                {#"date": date_list[i],
                 "start_time": date_list[i]+"T"+start_time[slot_list[i]],
                 "end_time": date_list[i]+"T"+end_time[slot_list[i]],
                 "room": room_list[i]})

with open('timetable.json', 'w') as file:
    json.dump(timetable, file, ensure_ascii=False, indent=4)
