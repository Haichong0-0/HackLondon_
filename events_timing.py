import openai
import json
import user_request_processor

# 碰到有 or 的情况, 进行事件选择或拆分

PROMPT_FOR_RESOLVING_DILEMMA="""
You are a chatbot that interprets plans submitted in the JSON dictionary for various appointments and commitments, analyzes and categorizes tasks, assigns priorities, and schedules timings effectively. Determining the nature of the 
event, check if the input contains “or”或类似需要让用户继续自己做选择的模糊字眼. If so, 一定要为用户只选择其中的一项, 不要让用户陷入选择困难症!
"""


PROMPT_FOR_TIMING="""
You are a chatbot that interprets plans submitted in the JSON dictionary for various appointments and commitments, analyzes and categorizes tasks, assigns priorities, and schedules timings effectively. Determining the nature of the 
event, reasonably schedules events into the user's timetable.
JSON keys with the prefix "DAILY_" stands for it being planned daily
JSON keys with the prefix "WKEND_" stands for it being planned on the weekend
JSON keys with the prefix "FIXED_" stands for it should be exactly added to the calendar with the exact specified date and time slot
If there is no any prefixs above, then schedule the event only once! only once! only once! for example:{"0007": "Mahjong at Chinatown Casino or Elephant & Castle"}, the output should look like this: {"Friday 8pm-10pm": "Mahjong at Chinatown Casino"}

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
#         # 如果找到了" or"，就返回其前面的内容；否则，返回整个字符串
#         if or_index != -1:
#             result[k]=v[:or_index]


def timing(generic_plan):
    openai.api_key = user_request_processor.API_KEY
    

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={"type": "json_object"},

        max_tokens=2000,
        messages=[
            {"role": "system", "content": PROMPT_FOR_RESOLVING_DILEMMA+PROMPT_FOR_TIMING},
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


print(timing(new_examples))