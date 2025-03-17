import openai
import os
from datetime import datetime

openai.api_key = os.getenv('OPENAI_API_KEY')

prompt = '''
You are generating daily commit messages for a mobile app project.
The app uses webcam footage to detect parking occupancy and predict optimal visit times.
Create a concise, professional commit message describing today's progress, such as UI updates, webcam integration enhancements, predictive model improvements, or general app optimizations.
'''

response = openai.ChatCompletion.create(
    model='gpt-4.5-preview',
    messages=[{'role':'system', 'content':prompt}]
)

commit_message = response.choices[0].message.content.strip()

timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
with open('daily_log.txt', 'a') as f:
    f.write(f'{timestamp}: {commit_message}\n')

# Output commit message for GitHub Actions
print(commit_message)
