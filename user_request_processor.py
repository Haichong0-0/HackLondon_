import json
import events_enumerating
import events_timing
import events_formatting
import json_to_ical

User_input="""
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
"""

generic_plan=events_enumerating.enumerate_events(User_input)
specific_events=events_timing.timing(str(generic_plan))
# specific_events_dict = json.loads(specific_events)
specific_events_list = [f"{key}: {value}" for key, value in specific_events.items()]

formatted_events_list=[]
for e in specific_events_list:
    formatted_events_list.append(events_formatting.format_timed_event(e))

json_to_ical.events_to_ics(formatted_events_list, "my_events.ics")