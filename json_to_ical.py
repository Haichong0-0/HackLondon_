def events_to_ics(events, output_file_name):
    """
    将包含多个事件的列表转换为单一的含有多个事件的 iCalendar (.ics) 文件。

    参数:
    - events: 包含事件字典的列表。
    - output_file_name: 输出的 .ics 文件名。
    """
    ics_content = "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//Your Company//Your Product//EN\n"


    for e in events:
        ics_content += f"""BEGIN:VEVENT
SUMMARY:{e["summary"]}
DTSTART:{e["start"]}
DTEND:{e["end"]}
"""
        if "location" in e:
            ics_content += "LOCATION:"+e["location"]+"\n"
        if "description" in e:
            ics_content += "DESCRIPTION:"+e["description"]+"\n"

        ics_content += "END:VEVENT\n"


    ics_content += "\nEND:VCALENDAR"
    print(ics_content)
    with open(output_file_name, "w") as file:
        file.write(ics_content)


# 示例事件列表
events_list = [{
    "summary": "Team meeting",

    "start": "20240311T100000",
    "end": "20240311T110000",

}, {
    "summary": "Lunch",
    "location": "Chinatown",
    "start": "20240311T120000",
    "end": "20240311T130000",

}, {
    "summary": "Nap",

    "start": "20240311T133000",
    "end": "20240311T140000",
    "description": "Re-energize"
}]
test_list=[]
# 调用函数，将事件列表转换为 .ics 文件
events_to_ics(events_list, "my_events.ics")
