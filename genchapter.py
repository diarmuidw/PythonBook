
import sys
import os
import openai
import json
import time

from datetime import datetime

current_time = datetime.now()
time_string = current_time.strftime("%H%M%S")

print("Current time is:", time_string)

max_tokens = 2000
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key_path =  '../../openai.key'

def run(version, chaptertitle, chapternumber, sections, sectionoutline):
    for section in sections:
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a professional software engineer. You like giving simple well thought out examples of programming concepts. You are an excellet technical writer."},
                {"role": "user", "content": "This is the outline of a chapter titled - %s: %s"%(chaptertitle, sectionoutline)},
                {"role": "user", "content": "Write the text of the section titled '%s', adding examples as needed"%section},
                {"role": "user", "content": "Generate the output in markdown format. Don't add an extraneous helpful comments"},
            ],
        max_tokens=max_tokens,
        temperature=0.8,
        )

        print(completion)

        try:
            f = open('Chapter%s.md'%(chapternumber),'a')
            f.write('# %s\n'%(chaptertitle))
            f.write(str(completion.choices[0].message.content))

            f.close()
        except Exception as ex:
            print(ex)
            pass