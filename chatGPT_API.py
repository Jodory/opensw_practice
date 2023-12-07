from openai import OpenAI

OPEN_API_KEY = "OPEN_API_KEY 입력"

OpenAI.api_key = OPEN_API_KEY

client = OpenAI(api_key = OPEN_API_KEY)

query = "opensw 실습 공부법 알려주세요."

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": query}
  ]
)


print(completion.choices[0].message)

