
import sys
import os
import openai
import json

#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key_path =  '../openai.key'

def completion():
    try:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt="You are a funny software engineer . \nGive me a list of chapters of a book on python programming. Make the chapter titles funny. Produce the ",
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        print (response)
        try:
            
            os.mkdir('output')
        except:
            pass

        f = open("./output/chapteroutline.txt","w")
        f.write(response.choices[0].message)
        f.close()

        print(response)
    except Exception as ex:
        print(ex)

    import openai

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a software engineer. You like giving simple well thought out examples of programming concepts. You are an excellet technical writer."},
        {"role": "user", "content": "Please give me the chapter outline of a 10 chapter book on python programming. Cover the basics in one chapter. The last chapter should be a introduction ot large language models"},
          {"role": "user", "content": "Generate the output in markdown format. Don't add an extraneous helpful comments"},
    ]
)


try:
    f = open('chapters.md','w')
    f.write(str(completion.choices[0].message.content))
    f.close()
except Exception as ex:
    print(ex)
    pass

print('finished')