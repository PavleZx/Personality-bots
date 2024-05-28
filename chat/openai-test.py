import os
import json
from openai import OpenAI


client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)
flag = True
while (flag == True):
  x = input(">>> ")
  if (x == "end"):
        break
  chat_completion = client.chat.completions.create(
      model="gpt-3.5-turbo-1106",
      messages=[
          {
              "role": "user",
              "content": x,
          }, {
              "role" : "system", 
              "content" : "return response in JSON text format."
          }
      ],
      max_tokens = 300,

  )

  try:
        file= open("response.json", "w")
        string = chat_completion.choices[0].message.content
        data = json.loads(string)
        json.dump(data, file, indent=2)
        file.close()
  except Exception as e:
      print(f"This occured: {e}")  
  
