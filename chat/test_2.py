from openai import OpenAI
import json
import os


client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

def chat():


    file = open("response.json", "w")

    try:

        history = []
        flag = True
        json_reminder = {"role" : "system", "content" : "return the response in JSON format"}
        history.append(json_reminder)
        check = 0
        while (flag == True):

            user_input = input("<<< ")
            if (user_input == "end"):
                flag == False
                file.close()
                for x in history:
                    print(f"{x["role"]} : {x["content"]}")

                file.close()
                file = open("response.json", "r")
                string = file.read()
                file.close()
                file = open("response.json", "w")
                file.write(' {"message_history" : [')
                file.write(string)
                file.write("]}")
                file.close()


                break
            if (check == 1):
                file.write(",")

            history.append({"role" : "user", "content" : user_input})

            chat_completion = client.chat.completions.create(
            model= "gpt-3.5-turbo-1106",
            response_format= {"type" : "json_object"},
            messages=history,
            max_tokens=200,
        )

            try:

                string = chat_completion.choices[0].message.content
                data = json.loads(string)
                keys = dict(data).keys()
                keys = list(keys)
                print(data[keys[0]])

                history.append({"role" : "assistant", "content" : data[keys[0]]})
                json.dump(data, file, indent=2)
                check = 1
            except Exception as e:
                print(f"This happened: {e}")
    except Exception as e:
            file.close()
            file = open("response.json", "r")
            string = file.read()
            file.close()
            file = open("response.json", "w")
            file.write(' {"message_history" : [')
            file.write(string)
            file.write("]}")
            file.close()


if __name__ == "__main__":

    chat()