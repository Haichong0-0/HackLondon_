import openai
import json



PROMPT="""
You are a chatbot that interprets user plans submitted in natural language.

output的要求: You must always answer in JSON. 每天都要重复的 event 的key要加上 DAILY_ 的前缀; 在周末的 event 要加上 WKEND_ 的前缀; 考试/deadline等不可抗力因素前要加 FIXED_ 前缀.
当用户说“画画、陶艺或摄影”“户外探险啊，比如攀岩或者划皮艇/远足/登山”之类有多种等价活动的选项时, 一定要为用户只选择其中的一项,
或者试图拆分成多个 events. 输出的结果一定不要出现“or”或类似需要让用户继续自己做选择的模糊字眼

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
"DAILY_0008":"lunch at",
"DAILY_0009":"dinner",
"DAILY_0010":"work",
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
'DAILY_0006': 'pottery session',
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
{'DAILY_0001': 'dance class (Latin)', 'DAILY_0002': 'pottery workshop', 'DAILY_0003': 'tea ceremony workshop', 'WKEND_0004': 'farm experience', 'WKEND_0005': 'participating in environmental activities (beach cleaning)', 'WKEND_0006': 'short trip to a nearby town', 'WKEND_0007': 'stargazing and astrophotography', '0008': 'joining an impromptu public speaking club', '0009': 'attending community cultural events', 'DAILY_0010': 'writing a novel'}

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

测试结果=enumerate_events("""
- 我挺想参加个摄影工作坊的，学学怎么拍出大片的感觉。或者我也可以试试手工艺课，比如学做手链或者小饰品，感觉挺有趣的。
- 我还想去听听现场音乐，不管是爵士乐还是摇滚，现场的气氛肯定迷人极了。
- 说到书，我可能会去图书馆找找看有没有什么新书发布的讲座，听听作者怎么说自己的书。
- 我也挺想尝试一下街头艺术，比如涂鸦。找个合法的地方，释放一下自己的创造力。
- 参加一次慈善跑或者环保活动也不错，既能锻炼身体，又能为好事出一份力。
- 我还挺想学习一下花艺，装饰自己的房间，让生活更有艺术感。
- 一个人的时候，我可能会选择一个安静的咖啡馆，写写日记或者计划一下未来，给自己一点时间思考和放松。
- 我也挺想去做一些社区服务，比如在动物收容所帮忙，和小动物们相处，感觉应该很治愈。
- 我也想尝试一下自己制作一部小短片，记录一下日常生活或者旅行的点点滴滴。
- 周末的时候，我打算去郊外野餐，带上一些美食，享受一下大自然的宁静。
""")

# for k in 测试结果:
#     print()
def remove_dilemma(result):
    for k,v in result.items():
        or_index = v.find(" or")
        # 如果找到了" or"，就返回其前面的内容；否则，返回整个字符串
        if or_index != -1:
            result[k]=v[:or_index]




remove_dilemma(测试结果)
print(type(测试结果))
print(测试结果)

