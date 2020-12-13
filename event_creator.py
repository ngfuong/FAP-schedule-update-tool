import json
import os.path
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pprint

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

# USING GOOGLE CALENDAR API TO CREATE EVENT
SCOPES = ['https://www.googleapis.com/auth/calendar']

flow = InstalledAppFlow.from_client_secrets_file(
    'credentials-fap.json', SCOPES
)
creds = flow.run_local_server(port=0)

service = build('calendar', 'v3', credentials=creds)

for item in event_list:
    event = service.events().insert(calendarId='primary', body=item).execute()
    print("Event created:", event.get('htmlLink'))

#with open('event.json', 'w') as outputFile:
#    json.dump(event_list, outputFile, ensure_ascii=False, indent=4)
