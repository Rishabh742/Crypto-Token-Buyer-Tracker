
3. AI-Powered Rewriting

To rewrite biased text into neutral language, we can use GPT models (OpenAI, T5, or BART). The AI rewrites articles using more 
factual and balanced language.

import openai

openai.api_key = "your-api-key"

def rewrite_text(text):

    response = openai.ChatCompletion.create(

        model="gpt-4",

        messages=[{"role": "system", "content": "Rewrite this article in a neutral tone:"}, 
                  {"role": "user", "content": text}]
    )
    return response["choices"][0]["message"]["content"]

biased_article = "The reckless leader ruined the economy."

print(rewrite_text(biased_article))
