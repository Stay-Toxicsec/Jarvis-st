
import os
import openai
from myapi import apikey

openai.api_key = apikey

a= input("enter command")

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": a}])
print(completion.choices[0].message.content)
