import json

def scrap_punctuations(timestamp: str) -> str:
    # Purpose: combat Generative AI delusion
    cleaned_string = timestamp.replace("-", "").replace(":", "").replace(" ", "")
    return cleaned_string


def events_to_ics(events, output_file_name: str):
    print("executing `events_to_ics` function")

    """
    Convert a list of multiple events into a single iCalendar (.ics) file of multiple events.
    :param events: List containing event dictionaries.
    :param output_file_name: output .ics file name.
    """

    ics_content = "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//TimeManagers/TimeWise//EN\nCALSCALE:GREGORIAN\n"
    i = 0

    for event in events:
        e=json.loads(event)
        start_timestamp = scrap_punctuations(e["start"])
        end_timestamp = scrap_punctuations(e["end"])
        i += 1
        print(i)

        ics_content += f"""BEGIN:VEVENT
SUMMARY:{e["summary"]}
DTSTART:{start_timestamp}
DTEND:{end_timestamp}
"""
        if ("location" in e) and e["location"] != "":
            ics_content += "LOCATION:" + e["location"] + "\n"
        if ("description" in e) and e["description"] != "":
            ics_content += "DESCRIPTION:" + e["description"] + "\n"

        ics_content += "END:VEVENT\n"

    ics_content += "END:VCALENDAR"
    # print(ics_content)
    with open(output_file_name, "w") as file:
        file.write(ics_content)

    print("Done")


test_events_list = [{
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
