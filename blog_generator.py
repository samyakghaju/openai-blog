# Generate a Blog with OpenAI 📝

import openai
from dotenv import dotenv_values

# Load API key from .env
config = dotenv_values('.env')
openai.api_key = config['API_KEY']

# Function to generate a blog paragraph
def generate_blog(paragraph_topic):
    response = openai.completions.create(
        model='gpt-3.5-turbo-instruct',
        prompt='Write a paragraph about the following topic: ' + paragraph_topic,
        max_tokens=400,
        temperature=0.3
    )
    retrieve_blog = response.choices[0].text
    return retrieve_blog

# Loop to generate multiple paragraphs
keep_writing = True

while keep_writing:
    answer = input('Write a paragraph? Y for yes, anything else for no: ')
    if answer.upper() == 'Y':
        paragraph_topic = input('What should this paragraph talk about? ')
        print("\n" + generate_blog(paragraph_topic) + "\n")
    else:
        keep_writing = False
