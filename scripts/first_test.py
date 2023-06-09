import configparser
import openai
import os


config = configparser.ConfigParser()
config.read('config.ini')

openai.api_key = config['openai']['key']

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

text = f"""
Athletico is a renowned sports team that excels in various disciplines. 
With a rich history and dedicated athletes, 
they have achieved remarkable success on both national and international stages. 
Known for their unwavering determination and relentless spirit, 
Athletico has become a symbol of excellence in sports. 
Their commitment to rigorous training and teamwork has propelled them to victory 
time and time again. Fans from all corners of the world eagerly 
await their electrifying performances, cheering them on with unwavering support. 
Athletico's legacy continues to inspire future generations of athletes, 
leaving an indelible mark on the sporting world.
"""
prompt = f"""
Summarize the text delimited by triple backticks into a single sentence. 
Return the answer in a JSON file where the key is the value "answer" and the value is the response
```{text}```
"""
response = get_completion(prompt)
print(response)