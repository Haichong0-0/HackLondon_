import sys
import events_enumerating
import events_timing
import events_formatting
import json_to_ical

user_input_test1 = """
- I really want to take part in a photography workshop to learn how to shoot blockbusters. Or I can also try handicraft classes, such as learning to make bracelets or small accessories, which is quite interesting.
- I'd also like to hear live music, whether it's jazz or rock, the atmosphere will definitely be amazing.
- Speaking of books, I might go to the library to see if there are any lectures on new book releases and listen to what the authors have to say about their books.
- I also really want to try street art, such as graffiti. Find a legal place to unleash your creativity.
- Participating in a charity run or environmental event is also a good way to exercise and contribute to a good cause.
- I really want to learn flower art, decorate my own room, and make my life more artistic.
- When I am alone, I might choose a quiet cafe to write in my diary or plan the future, giving myself some time to think and relax.
- I also really want to do some community service, such as helping at an animal shelter and getting along with small animals. It should feel very healing.
- I also want to try making a short short film myself to record every detail of my daily life or travels.
- On the weekend, I plan to go to the countryside for a picnic, bring some delicious food, and enjoy the tranquility of nature.
"""
user_input_test = """
Plan me a wonderful work-life balance week as a computer science university student in London"""


def processing_user_request(user_input: str):
    generic_plan = events_enumerating.enumerate_events(user_input)
    specific_events = events_timing.timing(generic_plan)

    specific_events_list = [f"{key}: {value}" for key, value in specific_events.items()]

    formatted_events_set = set() # Using set instead of list to combat Generative AI delusion - Generating repeatitive same events
    for e in specific_events_list:
        a=events_formatting.format_timed_event(e)
        formatted_events_set.add(a)

    json_to_ical.events_to_ics(formatted_events_set, "my_events.ics")


processing_user_request(user_input_test)

