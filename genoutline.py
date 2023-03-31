
import sys
import os
import openai
import json

#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key_path =  '../openai.key'
max_tokens = 2000

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a software engineer. You like giving simple well thought out examples of programming concepts. You are an excellet technical writer."},
        {"role": "user", "content": "Please give me the chapter outline of a 10 chapter book on python programming. Cover the basics in one chapter. The last chapter should be a introduction ot large language models"},
          {"role": "user", "content": "Generate the output in markdown format. Don't add an extraneous helpful comments"},
        ] 
        max_tokens=max_tokens,
        temperature=0.8,
)


try:
    f = open('Chapters.md','w')
    f.write(str(completion.choices[0].message.content))
    f.close()
except Exception as ex:
    print(ex)
    pass

print('finished')