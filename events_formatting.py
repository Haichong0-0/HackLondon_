import openai
import config
import datetime

GPT3="gpt-3.5-turbo"
GPT4="gpt-4-0125-preview"


PROMPT = f"""
You are a chatbot that interprets plans submitted in JSON dictionary for various appointments and commitments, and
 then analyze and categorize tasks, assign priorities, and schedule timings effectively. Determining the nature of the 
 event (summary), location, start time, end time, and any additional details (description).  You should always 
 meticulously format this information into a precise JSON structure, as shown in the example provided, with fields for
 summary, location (if any), start and end times in the standard format of the examples below, and a description (if any). 
 The output should always be a JSON dictionary of JSON-formatted events, 
 which is then to be used to create events in the user's digital calendar, 
 ensuring that the user's schedule is organized and readily accessible.

Each piece of JSON structure stand for an event for the user's planning.
You must strictly follow the formatting conventions. Given today’s date is {datetime.datetime.now().strftime("%Y-%m-%d")}
and it's the {datetime.datetime.now().weekday()} day of the week, all scheduled events must commence after today’s date. 
You are to focus on arranging timings that are forthcoming, emphasizing the importance of near-term planning.
""" + """
for example: {
  "summary": "Team meeting",
  "location": "Office 1",
  "start": "20240310T100000",
  "end": "20240310T110000",
  "description": "Discuss project progress"
}
N.B. In "20240310T100000", the first 4 characters stand for the current year, then 2 characters stand for the month, 
then 2 characters stand for the day of the month, then followed by the letter "T".
Then 2 characters stand for the hour of the day, then 2 characters stand for the minute of the hour, then 2 characters stand for the second of the minute.
or{
  "summary": "Lunch",
  "location": "Chinatown",
  "start": "20240310T120000",
  "end": "20240310T130000",
  "description": ""
}
or{
  "summary": "Nap",
  "location": "Office 1",
  "start": "20240310T133000",
  "end": "20240310T140000",
  "description": "Re-energize"
}


"""


def format_timed_event(event: str) -> str:
    print("executing `format_timed_event` function")

    openai.api_key = config.API_KEY

    response = openai.chat.completions.create(
        model=GPT4,
        response_format={"type": "json_object"},
        temperature=0.0,
        max_tokens=500,
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": event}
        ]
    )

    events = response.choices[0].message.content

    return events


test_events = {'Monday 8:30-9am': 'reading in the British Library',
               'Tuesday 8:30-9am': 'reading in the British Library',
               'Wednesday 8:30-9am': 'reading in the British Library',
               'Thursday 8:30-9am': 'reading in the British Library',
               'Friday 8:30-9am': 'reading in the British Library',
               'Saturday 8:30-9am': 'reading in the British Library',
               'Sunday 8:30-9am': 'reading in the British Library', 'Monday 10:00-10:30': 'coffee at Costa',
               'Tuesday 10:00-10:30': 'coffee at Costa', 'Wednesday 10:00-10:30': 'coffee at Costa',
               'Thursday 10:00-10:30': 'coffee at Costa', 'Friday 10:00-10:30': 'coffee at Costa',
               'Saturday 10:00-10:30': 'coffee at Costa', 'Sunday 10:00-10:30': 'coffee at Costa',
               'Monday 9:00-12:00': 'coding session', 'Tuesday\xa09:00-12:00': 'coding session',
               'Thursday 9:00-12:00': 'coding session', 'Friday 9:00-12:00': 'coding session',
               'Monday 14:30-17:30': 'coding session', 'Tuesday 14:30-17:30': 'coding session',
               'Wednesday 14:30-17:30': 'meeting', 'Thursday 13:30-14:30': 'dentist appointment',
               'Monday 18:00-18:30': 'visit museums', 'Friday 18:00-18:30': 'visit museums',
               'Saturday 18:00-18:30': 'visit museums', 'Sunday 18:00-18:30': 'visit museums',
               'Monday 19:00-19:30': 'evening walk', 'Tuesday 19:00-19:30': 'evening walk',
               'Wednesday 19:00-19:30': 'evening walk', 'Thursday 19:00-19:30': 'evening walk',
               'Friday 19:00-19:30': 'evening walk', 'Saturday 19:00-19:30': 'evening walk',
               'Sunday 19:00-19:30': 'evening walk', 'Monday 20:00-21:00': "dinner at friends' house",
               'Tuesday 20:00-21:00': "dinner at friends' house", 'Wednesday 20:00-21:00': "dinner at friends' house",
               'Thursday 20:00-21:00': "dinner at friends' house", 'Friday 20:00-21:00': "dinner at friends' house",
               'Saturday 20:00-21:00': "dinner at friends' house", 'Sunday 20:00-21:00': "dinner at friends' house",
               'Monday 6:30-7am': 'morning yoga', 'Tuesday 6:30-7am': 'morning yoga',
               'Wednesday 6:30-7am': 'morning yoga', 'Thursday 6:30-7am': 'morning yoga',
               'Friday 6:30-7am': 'morning yoga', 'Saturday 6:30-7am': 'morning yoga',
               'Sunday 6:30-7am': 'morning yoga', 'Monday 9:00-10:00': 'team meetings',
               'Tuesday 9:00-10:00': 'team meetings', 'Thursday 9:00-10:00': 'team meetings',
               'Friday 9:00-10:00': 'team meetings', 'Monday 7:00-8:00': 'grocery shopping at Tesco',
               'Tuesday 7:00-8:00': 'grocery shopping at Tesco', 'Wednesday 7:00-8:00': 'grocery shopping at Tesco',
               'Thursday 7:00-8:00': 'grocery shopping at Tesco', 'Friday 7:00-8:00': 'grocery shopping at Tesco',
               'Saturday 7:00-8:00': 'grocery shopping at Tesco', 'Sunday 7:00-8:00': 'grocery shopping at Tesco',
               'Monday 8:00-8:45': 'meditation', 'Tuesday 8:00-8:45': 'meditation', 'Wednesday 8:00-8:45': 'meditation',
               'Thursday 8:00-8:45': 'meditation', 'Friday 8:00-8:45': 'meditation',
               'Saturday 8:00 -8:45': 'meditation', 'Sunday 8:00-8:45': 'meditation'}
