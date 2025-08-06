# if you dont use pipenv uncomment the following:
import os
from dotenv import load_dotenv
import base64
from groq import Groq
load_dotenv()


GROQ_API_KEY=os.environ.get("GROQ_API_KEY")



def encode_image(image_path):   
    image_file=open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode('utf-8')


model="meta-llama/llama-4-scout-17b-16e-instruct"
def analyze_image_with_query(query, model, encoded_image):
    client=Groq()  
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }]
    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content