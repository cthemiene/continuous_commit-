from openai import OpenAI
import os
from datetime import datetime

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

prompt = '''
Write a concise, professional daily commit message summarizing today's update.
'''

response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[{'role': 'system', 'content': prompt}],
    temperature=1,
    max_completion_tokens=4000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

commit_message = response.choices[0].message.content.strip()

timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
with open('daily_log.txt', 'a') as f:
    f.write(f'{timestamp}: {commit_message}\n')

print(commit_message)
