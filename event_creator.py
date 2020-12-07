import json
import pprint

timeZone = 'Asia/Bangkok'
with open('timetable.json', 'r') as inputFile:
    # Loading data
    data = inputFile.read()
    timetable = json.loads(data)

    # Creating event
    event_list = []
    for subject in timetable:
        for item in timetable[subject]:
            event = {
                'summary': subject,
                'description': 'Room: '+item['room'],
                'start': {
                    'dateTime': item['start_time'],
                    'timeZone': timeZone
                },
                'end': {
                    'dateTime': item['end_time'],
                    'timeZone': timeZone
                },
                # READ DOC ABOUT THIS
                'recurrence': [
                    'RRULE:FREQ=ONCE;COUNT=1'
                ],
                # READ DOC ABOUT THIS
                'reminders': {
                    'useDefault': False,
                    'overrides': [
                        {'method': 'pop', 'minutes': 45}
                    ]
                }
            }
            event_list.append(event)

with open('event.json', 'w') as outputFile:
    json.dump(event_list, outputFile, ensure_ascii=False, indent=4)
