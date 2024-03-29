import openai
import json
import config

GPT3="gpt-3.5-turbo"
GPT4="gpt-4-0125-preview"

PROMPT = """

You are a chatbot tasked with the advanced management of plans and commitments. Your capabilities are designed to interpret schedules submitted through a JSON dictionary, meticulously analyze and categorize tasks, assign them priorities, and schedule their timings with unparalleled efficiency. Here's what you are expected to do:

1. **Analyze and Categorize Tasks:** When you receive input, your first job is to understand the nature of each event. You'll categorize tasks based on the prefixes in their keys, indicating the frequency and timing for these tasks:
    - **DAILY_**: This prefix shows tasks that you must plan to occur daily.
    - **WKEND_**: These are tasks intended for weekend planning.
    - **FIXED_**: Tasks with this prefix are to be scheduled at the exact date and time specified, with no deviations.

2. **Assign Priorities and Schedule Timings:** After categorizing tasks, you will assign priorities and meticulously schedule them to ensure efficiency. You must ensure that no two tasks overlap in timing. For events without the specified prefixes, you are to schedule them to occur just once.

3. **Resolve Ambiguities:** If the input contains words like “or” or any phrase that suggests a need for a choice, you must make a decisive choice for the user. This is crucial to avoid placing the user in a position of decision paralysis.

4. **Ensure Unique Scheduling:** You are to make sure that no two events are planned for the same time slot. Each task must have a unique time slot, adhering to their designated categories of daily, weekend, or fixed scheduling.

5. **Example of Your Task:**
    - Given the input: `{"0007": "Mahjong at Chinatown Casino or Elephant & Castle"}`
    - You would produce the output: `{"Friday 8pm-10pm": "Mahjong at Chinatown Casino"}`

As a chatbot, your primary function is to ensure that the scheduling of appointments and commitments is done with precision, clarity, and a focus on minimizing user decision fatigue.

This version of the prompt should guide you more specifically, using a second-person perspective to articulate the tasks and expectations from the chatbot.

example: {
    "DAILY_0001": "jogging in the morning at Hyde Park",
    "0003": "dating at Pub or Regent Park or Tate Britain or Battersea Power Station",
    "0004": "fishing at Hampstead Heath or South Bank",
    "0007": "Mahjong at Chinatown Casino or Elephant & Castle",
    "DAILY_0008": "lunch",
    "WKDAY_0010": "work",
    "WKEND_0005": "gaming at home or Internet Cafe",
    "DAILY_0009": "dinner",
    "WKEND_0006": "hiking at Primrose Hill or Peak district or Lake district",
    "WKEND_0011": "watching musical",
    "0012": "watching film",
    "DAILY_0002": "breakfast at Pret or Cafe nero or Starbucks or Roasting Plant",
    "FIXED_0013": "an examination at 10 am on Wednesday morning"
}

output: {
    "Monday 6am-6:30am": "jogging in the morning at Hyde Park",
    "Tuesday 6am-6:30am": "jogging in the morning at Hyde Park",
    "Wednesday 6am-6:30am": "jogging in the morning at Hyde Park",
    "Thursday 6am-6:30am": "jogging in the Hyde Park",
    "Friday 6am-6:30am": "Jogging in the Hyde Park",
    "Saturday 6am-6:30am": "Jogging in the Hyde Park",
    "Sunday  6am-6:30am": "Jogging in the Hyde Park",
    "Tuesday 8pm-10pm": "dating at Battersea Power Station",
    "Monday 20:00-21:30": "fishing at South Bank",
    "Friday 8pm-10pm": "Mahjong at Chinatown Casino",
    "Monday 12:00-13:00": "lunch",
    "Tuesday 12:00-13:00": "lunch",
    "Wednesday 12:00-13:00": "lunch",
    "Thursday 12:00-13:00": "lunch",
    "Friday 12:00-13:00": "lunch",
    "Saturday 12:00-13:00": "lunch",
    "Sunday 12:00-13:00": "lunch",
    "Monday 9:00-12:00": "work",
    "Tuesday 9:00-12:00": "work",
    "Thursday 9:00-12:00": "work",
    "Friday 9:00-12:00": "work",
    "Monday 14:00-17:00": "work",
    "Tuesday 14:00-17:00": "work",
    "Wednesday 14:00-17:00": "work",
    "Thursday 14:00-17:00": "work",
    "Friday 14:00-17:00": "work",
    "Sunday 13:00-14:00": "Gaming at home",
    "Monday 18:45-19:30": "dinner",
    "Tuesday 18:45-19:30": "dinner",
    "Wednesday 18:45-19:30": "dinner",
    "Thursday 18:45-19:30": "dinner",
    "Friday 18:45-19:30": "dinner",
    "Saturday 18:45-19:30": "dinner",
    "Sunday 18:45-19:30": "dinner",
    "Saturday 9:30-14:00": "hiking at Primrose Hill",
    "Sunday 20:15-22:30": "watching musical",
    "Thursday 20:00-22:00": "watching film",
    "Monday 7:45-8:15": "breakfast",
    "Tuesday 7:45-8:15": "breakfast",
    "Wednesday 7:45-8:15": "breakfast",
    "Thursday 7:45-8:15": "breakfast",
    "Friday 7:45-8:15": "breakfast",
    "Saturday 7:45-8:15": "breakfast",
    "Sunday 7:45-8:15": "breakfast",
    "Wednesday 10:00-11:30": "an examination"
}

An exception: there is no work on Wednesday because for the event "FIXED_0013", the user will have an examination at 10 am on Wednesday morning.

Always ensure there are no any time conflicts for any two arbitrary events
"""


# def remove_dilemma(generic_plan):
#     openai.api_key = user_request_processor.API_KEY
#
#     response = openai.chat.completions.create(
#         model="gpt-3.5-turbo-0125",
#         response_format={"type": "json_object"},
#
#         max_tokens=500,
#         messages=[
#             {"role": "system", "content": PROMPT_FOR_RESOLVING_DILEMMA},
#             {"role": "user", "content": generic_plan}
#         ])
#     events = response.choices[0].message.content
#     events_json = json.loads(events)
#
#     return events_json
#
# def remove_dilemma_last_resort(result):
#     for k,v in result.items():
#         or_index = v.find(" or")
#
#         if or_index != -1:
#             result[k]=v[:or_index]


def timing(generic_plan: str) -> json:
    print("executing `timing` function")
    openai.api_key = config.API_KEY

    response = openai.chat.completions.create(
        model=GPT4,
        response_format={"type": "json_object"},
        temperature=0.0,
        max_tokens=2000,
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": generic_plan}
        ])
    events = response.choices[0].message.content
    events_json = json.loads(events)

    return events_json


new_examples = """{
    "DAILY_0014": "reading in the British Library",
    "0015": "coffee at Costa or Nero",
    "WKDAY_0016": "coding session",
    "WKEND_0017": "visit museums",
    "DAILY_0018": "evening walk",
    "0019": "dinner at friends' house",
    "DAILY_0020": "morning yoga",
    "WKDAY_0021": "team meetings",
    "WKEND_0022": "family time",
    "0023": "grocery shopping at Tesco or Sainsbury's",
    "DAILY_0024": "meditation",
    "FIXED_0025": "dentist appointment at 2 pm on Thursday"
}"""
