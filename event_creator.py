import json
import pprint
from service_account_setup import create_service

with open('timetable.json', 'r') as inputFile:
    # Loading timetable data
    data = inputFile.read()
    timetable = json.loads(data)

    # Reformat event
    timeZone = 'Asia/Bangkok'
    event_list = []
    for subject in timetable:
        for item in timetable[subject]:
            event = {
                'summary': subject,
                'description': 'Room: '+item['room'],
                'start': {
                    'dateTime': item['start_time'],
                    'timeZone': timeZone,
                },
                'end': {
                    'dateTime': item['end_time'],
                    'timeZone': timeZone,
                },
                # READ DOC ABOUT THIS
                'recurrence': [
                    'RRULE:FREQ=ONCE;COUNT=1',
                ],
                # READ DOC ABOUT THIS
                'reminders': {
                    'useDefault': False,
                    'overrides': [
                        {'method': 'pop', 'minutes': 45},
                    ],
                },
            }
            event_list.append(event)

# USING GOOGLE CALENDAR API TO CREATE EVENT
SUBJECT = 'ubuntu@fap-scraping-298512.iam.gserviceaccount.com '
service = create_service(SUBJECT)
for item in event_list:
    event = service.events().insert(calendarId=SUBJECT, body=item).execute()
    print("Event created:", event.get('htmlLink'))

#with open('event.json', 'w') as outputFile:
#    json.dump(event_list, outputFile, ensure_ascii=False, indent=4)
