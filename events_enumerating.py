import openai
import json



PROMPT="""
You are a chatbot that interprets user plans submitted in natural language.
for example: 有这几件事情: 打游戏、钓鱼、打麻将、远足、约会、吃饭、工作、晨跑、音乐剧、电影
output的要求: You must always answer in JSON. 每天都要重复的 event 要加上 DAILY_ 的前缀; 在周末的 event 要加上 WEEKEND_ 的前缀
output example: 
{
"0001":"DAILY_jogging in the morning",
"0002":"DAILY_breakfast",
"0003":"dating",
"0004":"fishing",
"0005":"gaming",
"0006":"WEEKEND_hiking",
"0007":"Mahjong",
"0008":"DAILY_lunch",
"0009":"DAILY_dinner",
"0010":"DAILY_work",
"0011":"WEEKEND_watching musical",
"0012":"watching film",
}
"""
API_KEY='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'
def enumerate_events(generic_plan):
    openai.api_key = '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'

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={"type": "json_object"},

        max_tokens=500,
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": generic_plan}
        ]
    )

    events = response.choices[0].message.content
    events_json = json.loads(events)

    return events_json

测试结果=enumerate_events("我这一周要 打游戏、钓鱼、打麻将、远足、约会、吃饭、工作、晨跑、音乐剧、电影")
print(测试结果)