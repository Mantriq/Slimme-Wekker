from __future__ import print_function
from datetime import datetime, date
from genericpath import exists
import os.path
import sys

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from not_calendar import calendarId

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
        doc = open('textDocs/calendarId.txt', 'r')
        Id = doc.read()
        doc.close()

       # Call the Calendar API
        now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        events_result = service.events().list(calendarId=Id, timeMin=now,
                                              maxResults=1, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        
        for event in events:

            start = event['start'].get('dateTime')

            time = start[11:16]
            print(time)
            times = open("textDocs/times.txt", "r")
            tim = times.read().splitlines()
            timeBefore = tim[0]
            timeLatest = tim[1]
            normal = "00:00"
            FMT = '%H:%M'
            timeAlarm = datetime.strptime(time, FMT) - datetime.strptime(timeBefore, FMT)
            timeAlarm = str(timeAlarm)
            if (timeAlarm[1] == ":"):
                timeAlarm = "0" + timeAlarm
            timeLatest = datetime.strptime(timeLatest, FMT) - datetime.strptime(normal, FMT)
            timeLatest = str(timeLatest)

            datumnu = date.today()
            datum = start[0:10]
            datumnu = str(datumnu)
            datum = str(datum)

            if (datumnu != datum):
                alarm = open("textDocs/alarmtime.txt", 'w')
                alarm.write(timeLatest)
                alarm.close()
            elif (timeAlarm < timeLatest):
                alarm = open("textDocs/alarmtime.txt", 'w')
                alarm.write(timeAlarm)
                alarm.close()
            else:
                alarm = open("textDocs/alarmtime.txt", 'w')
                alarm.write(timeLatest)
                alarm.close()
            

    except HttpError as error:
        print('An error occurred: %s' % error)

def shutdown():
    sys.exit(0)


if __name__ == '__main__':
    main()