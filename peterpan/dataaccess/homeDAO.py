from peterpan.dataaccess.db_helper import execute_sql
from peterpan.events.models import Event
import datetime

def getUpcomingEvent():
    sql = "SELECT * from event where eventDate >= date('now') Order by eventDate LIMIT 1"
    row = execute_sql (sql,(), False, True)
    if not row == None:
        event = Event()
        event.eventTitle = row['title']
        event.eventDesc = row['description']
        event.eventLocation = row['location']
        event.eventDate = datetime.datetime.strptime(row['eventdate'],'%Y-%m-%d').strftime('%m/%d/%Y')
        event.startTime = row['startTime']
        event.endTime = row['endTime']
        return event
