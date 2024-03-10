import openai
import json

import config

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

example 1: 有这几件事情: 打游戏、钓鱼、打麻将、远足、约会、吃饭、工作、晨跑、音乐剧、电影 (但我周三早上10点有考试)

output for example 1 (不要出现 or 或模糊的用词!): 
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
- 我想试试去烹饪课。或者看喜剧或话剧怎么样？比起电影，现场的感觉更真实，笑声、掌声，气氛很棒的。
- 加入个书俱乐部呢？除了读书，还能遇到一些有意思的人，交流交流思想什么的。
- 我还想户外探险，比如攀岩或者划皮艇/远足/登山。和朋友一起，既刺激又好玩。
- 瑜伽或冥想课程也挺不错，对身心都好，换个方式放松一下。
- 画画、陶艺或摄影，搞搞艺术创作。这个特别能放松人，而且说不定你还有隐藏的艺术天分呢。
- 晚上找个时间去观星吧，选个视野开阔、光污染少的地方，看看宇宙的美，感觉特别棒。

output for example 2 (不要出现 or 或模糊的用词!):
{'WKEND_0001': 'cooking class', 
'0002': 'watching drama',
'0003': 'joining a book club',
'WKEND_0004': 'hiking with friends',
'DAILY_0005': 'meditation class',
'WKDAY_0006': 'pottery session',
'0007': 'stargazing at night'
'WKEND_0004': 'Kayaking with friends',}

exmaple 3:
- 我觉得去参加一个舞蹈课程也挺好的。学学拉丁舞或街舞，动感的音乐，跟着节奏舞动，感觉自己也年轻活力满满的。
- 或者我可以试试手工艺品制作课，比如学做皮革手工艺或是陶瓷，动手能力强了，做出来的东西还能送人，多有意义。
- 我还挺想学习一下茶艺或咖啡冲泡技术，这样不仅能享受过程，还能提升生活品质，邀请朋友来家里，展示一下自己的手艺。
- 体验一天的农场生活也不错，去郊外的农场体验一下收获果蔬的乐趣，接触大自然，感受一下农耕文化。
- 我想去参加一些环保活动，比如海滩清洁或是城市绿化项目。这样既能出力做好事，又能提高自己的环保意识。
- 做个小旅行也是个不错的选择，选择一个周末，去附近的小镇探险，体验不一样的文化和风景。
- 我还打算试试看天文摄影，晚上带着相机捕捉星辰大海的美景，这应该会是一个很酷的经历。
- 我也想试试参加一个即兴演讲俱乐部，提升一下自己的公众演讲能力，同时也能认识一些志同道合的朋友。
- 也许我还可以去参加一些社区的文化活动或节庆，了解不同的文化传统，拓宽视野。
- 最后，我想尝试自己写小说或短篇故事，这样不仅能锻炼我的写作能力，还能让我有个机会发挥想象力，创造自己的世界。
output for example 3:
{'WKDAY_0001': 'dance class (Latin)', 'WKDAY_0002': 'pottery workshop', '0003': 'tea ceremony workshop',
'WKEND_0004': 'farm experience', 'WKEND_0005': 'participating in environmental activities (beach cleaning)', 'WKEND_0006': 'short trip to a nearby town', 'WKEND_0007': 'stargazing and astrophotography', '0008': 'joining an impromptu public speaking club', '0009': 'attending community cultural events', 'DAILY_0010': 'writing a novel'}

"""


def enumerate_events(natural_language_plan: str) -> json:
    print("正在执行 enumerate_events 函数")
    openai.api_key = config.API_KEY

    response = openai.chat.completions.create(
        model="gpt-4-0125-preview",
        response_format={"type": "json_object"},

        max_tokens=500,
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": natural_language_plan}
        ]
    )

    events = response.choices[0].message.content
    events_json = json.loads(events)

    return events_json


# for k in 测试结果:
#     print()
def remove_dilemma(result):
    for k, v in result.items():
        or_index = v.find(" or")
        # 如果找到了" or"，就返回其前面的内容；否则，返回整个字符串
        if or_index != -1:
            result[k] = v[:or_index]
