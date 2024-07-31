import openai
API_BASE = "https://aigptx.top/v1"
API_KEY = ''
openai.api_base = API_BASE # Useful for ohmygpt API
openai.api_key = API_KEY
response = openai.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)
print(response.choices[0].message.content)