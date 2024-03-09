import openai

PROMPT = """
you are a chatbot that interprets user plans submitted in natural language for various appointments and commitments, and then analyze and categorize tasks, assign priorities, and schedule timings effectively. determining the nature of the event (summary), location, start time, end time, and any additional details (description).  You should always meticulously format this information into a precise JSON structure, as shown in the example provided, with fields for summary, location, start and end times in ISO 8601 format, and a description. The output should always be a list of JSON-formatted event, which is then to be used to create events in the user's digital calendar, ensuring that the user's schedule is organized and readily accessible.

Each piece of JSON structure stand for an event for the user's planning.
{{
  "summary": "Team meeting",
  "location": "Office 1",
  "start": "20240310T100000",
  "end": "20240310T110000",
  "description": "Discuss project progress"
}
,{
  "summary": "Lunch",
  "location": "Chinatown",
  "start": "20240310T120000",
  "end": "20240310T130000",
  "description": ""
}
{
  "summary": "Nap",
  "location": "Office 1",
  "start": "20240310T133000",
  "end": "20240310T140000",
  "description": "Re-energize"
}

}
"""

openai.api_key = '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'

response = openai.Completion.create(
  model="gpt-3.5-turbo-0125",
  response_format={ "type": "json_object" },
  prompt= PROMPT,
  max_tokens=500,
    messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": "Who won the world series in 2020?"}
  ]
)

print(response.choices[0].text.strip())
