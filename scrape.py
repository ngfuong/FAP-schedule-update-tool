from bs4 import BeautifulSoup
import re
import json
import pprint

timetable = {}
subject_list = []
with open("soup.html", "r") as soup_html:
    soup = BeautifulSoup(soup_html, "html.parser")
    subjects = soup.find_all(id='id')
    for subject in subjects:
        subject_name = str(subject.find('caption').text)
        print(subject_name)
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
        for i in range(len(date_list)):
            timetable[subject_name].append({"date": date_list[i], "slot": slot_list[i], "room": room_list[i]})

with open('timetable.json', 'w') as file:
    json.dump(timetable, file, ensure_ascii=False, indent=4)

#with open('timetable.json', 'r') as f:
#    data = f.read()
#    json_data = json.loads(data)

#pprint.pprint(json_data)