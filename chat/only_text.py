from openai import OpenAI
import json
import os


client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

def chat():

        history = []
        while (True):

            user_input = input("<<< ")
            if (user_input == "end"):
                for x in history:
                    print(f"{x["role"]} : {x["content"]}")
                    print()
                break
   
            history.append({"role" : "user", "content" : user_input})

            chat_completion = client.chat.completions.create(
            model= "gpt-3.5-turbo-1106",
            messages=history,
            max_tokens=200,
        )

            try:
                                # create vrati objekt klase shat.shat_completion.ChatCompletion
                print(chat_completion.usage.completion_tokens)
                print(chat_completion.usage.prompt_tokens)
                print(chat_completion.usage.total_tokens)
                print(type(chat_completion))
                string = chat_completion.choices[0].message.content
                print(">>> ", string)
                print(type(string))

                history.append({"role" : "assistant", "content" : string})
                check = 1
            except Exception as e:
                print(f"This happened: {e}")
    

if __name__ == "__main__":

    chat()