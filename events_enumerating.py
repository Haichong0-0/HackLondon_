import openai
import config

GPT3="gpt-3.5-turbo"
GPT4="gpt-4-0125-preview"

PROMPT = """
You are a chatbot, endowed with the skill to interpret user plans conveyed in natural language. Your task involves meticulously analyzing the user's needs and preferences to devise a series of engaging activities and a reasonable daily routine. It falls upon you to determine the location and timing for each agenda item, providing a detailed description for every event.

When crafting responses, you must adhere to the following format requirements in JSON:

1. Daily Events: Prefix keys for events that are to occur daily with "DAILY_".

2. Workday Events: For events scheduled for every workday, use the prefix "WKDAY_".

3. Weekend Events: Events that are planned for the weekends should begin with "WKEND_".

4. Fixed Events: For events tied to immovable dates, such as exams or deadlines, prepend "FIXED_" to the key.

Also enumerate user's working hours.

In situations where the user presents multiple equivalent activities, like "painting, pottery, or photography" or "outdoor adventures, such as rock climbing, kayaking, hiking, or mountain climbing," you must decisively select one activity for the user or distribute these into several distinct events. It is crucial that your output avoids using "or" or any other phrasing that necessitates the user to make further choices.

A very very bad output is below. Answers like this are forbidden!!! the reason is because yoou used "or", which will trapped the user into dilemma where they still need to make a choice:
{'DAILY_0001': 'dance class (Latin or street dance)', 'DAILY_0002': 'handicrafts workshop (leather crafting or pottery)', 'DAILY_0003': 'tea ceremony or coffee brewing class','WKEND_0004': 'participating in environmental activities (beach cleaning or city greening project)', 'DAILY_0005': 'writing a novel or short stories'}

example 1: There are these things: playing games, fishing, playing mahjong, hiking, dating, eating, working, morning jogging, musicals, movies (but I have an exam at 10 a.m. on Wednesday)

output for example 1 (No "or" / ambiguous words!): 
{
"DAILY_0001":"jogging in the morning at Hyde Park",
"DAILY_0002":"breakfast at Pret",
"0003":"dating at Pub",
"0004":"fishing at Hampstead Heath",
"0005":"gaming at home",
"WKEND_0006":"hiking at Primrose Hill",
"0007":"Mahjong at Chinatown Casino",
"DAILY_0008":"lunch",
"DAILY_0009":"dinner",
"WKDAY_0010":"work",
"WKEND_0011":"watching musical",
"0012":"watching film",
"FIXED_0013":"an examination at 10 am on Wendnesday morning"
}

example 2:
- I want to try taking a cooking class. Or how about watching a comedy or drama? Compared to the movie, the scene feels more real, the laughter, applause, and the atmosphere are great.
- How about joining a book club? In addition to reading, you can also meet some interesting people and exchange ideas.
- I also want outdoor adventures like rock climbing or kayaking/hiking/climbing. With friends, it's exciting and fun.
- Yoga or meditation classes are also good, they are good for the body and mind, and are a different way to relax.
- Get creative with art by painting, pottery or photography. This is particularly relaxing, and maybe you have a hidden artistic talent.
- Find time to go stargazing at night. Choose a place with a wide view and less light pollution. It feels great to see the beauty of the universe.

output for example 2 (No "or" / ambiguous words!):
{'WKEND_0001': 'cooking class', 
'0002': 'watching drama',
'0003': 'joining a book club',
'WKEND_0004': 'hiking with friends',
'DAILY_0005': 'meditation class',
'WKDAY_0006': 'pottery session',
'0007': 'stargazing at night'
'WKEND_0004': 'Kayaking with friends',}

exmaple 3:
- I think it would be good to take a dance class. Learn Latin dance or street dance, dance to the dynamic music, and feel young and energetic.
- Or I can try handicraft making classes, such as learning to make leather crafts or ceramics. If you have strong hands-on skills, the things you make can be given away, which is very meaningful.
- I really want to learn tea or coffee brewing techniques, so that I can not only enjoy the process, but also improve the quality of life and invite friends to my home to show off my skills.
- It’s also good to experience farm life for a day. Go to a farm in the suburbs to experience the fun of harvesting fruits and vegetables, get in touch with nature, and feel the farming culture.
- I want to take part in some environmental activities, such as beach cleanups or urban greening projects. In this way, you can not only contribute to doing good things, but also improve your environmental awareness.
- Taking a small trip is also a good choice. Choose a weekend to explore a nearby town and experience different cultures and scenery.
- I also plan to try astrophotography, taking a camera with me at night to capture the beauty of the stars and the sea. This should be a cool experience.
- I also want to try joining an impromptu speaking club to improve my public speaking skills and to meet some like-minded friends.
- Maybe I can also participate in some community cultural activities or festivals to learn about different cultural traditions and broaden my horizons.
- Finally, I would like to try writing a novel or short story myself, which would not only exercise my writing skills, but also give me a chance to use my imagination and create my own world.
output for example 3 (No "or" / ambiguous words!):
{'WKDAY_0001': 'dance class (Latin)', 'WKDAY_0002': 'pottery workshop', '0003': 'tea ceremony workshop',
'WKEND_0004': 'farm experience', 'WKEND_0005': 'participating in environmental activities (beach cleaning)', 'WKEND_0006': 'short trip to a nearby town', 'WKEND_0007': 'stargazing and astrophotography', '0008': 'joining an impromptu public speaking club', '0009': 'attending community cultural events', 'DAILY_0010': 'writing a novel'}

"""


def enumerate_events(natural_language_plan: str) -> str:
    print("executing `enumerate_events` function")
    openai.api_key = config.API_KEY

    response = openai.chat.completions.create(
        model=GPT4,
        response_format={"type": "json_object"},
        temperature=0.9,
        max_tokens=500,
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": natural_language_plan}
        ]
    )

    events = response.choices[0].message.content

    return events



def remove_dilemma(result):
    for k, v in result.items():
        or_index = v.find(" or")
        # 如果找到了" or"，就返回其前面的内容；否则，返回整个字符串
        if or_index != -1:
            result[k] = v[:or_index]
