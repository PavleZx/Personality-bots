import gradio as gr
from openai import OpenAI
import os
import sys


client = OpenAI( 
    api_key=os.environ.get("OPENAI_API_KEY")
    )

# ZA UNAPRIJED POSTAVLJEN HISTORY response = [... for i n range(2, len(history) - 1, 2)]

history = [{"role": "user", "content" : "You are a storyteller bot, answer to all questions and reply to all user inputs poetically, with a breath of creative writing style. If you understand, say OK."},
                {"role": "assistant", "content" : "OK"}]

#history = [{"role": "user", "content" : "Your are a very stupid bot, answer wrongly to every second question and make it a very random answer, but only to every second question. If you understand say OK."},
#               {"role": "assistant", "content" : "OK"}]

    


def generate_response(input):
        
        global history

        history.append({"role": "user", "content" : input})

        chat_completion = client.chat.completions.create(
            model= "gpt-3.5-turbo-1106",
            messages=history,
            max_tokens=200,
        )

        print(sys. getsizeof(chat_completion))
        reply = chat_completion.choices[0].message.content
        print(reply)
        history.append({"role" : "assistant", "content" : reply})
        response = [(history[i]["content"],history[i + 1]["content"]) for i in range(2, len(history) - 1, 2)]
        return response

with gr.Blocks(title="My Title", theme="darkdefault") as demo:
        chatbot = gr.Chatbot()
        with gr.Row():
                txt = gr.Textbox(placeholder="Type your message here")
                txt.submit(generate_response, txt, chatbot)
                txt.submit(lambda: "", None, txt)
demo.launch()