from langchain.chains import LLMChain
from langchain.llms import GooglePalm
from langchain.prompts import PromptTemplate

import os
from dotenv import load_dotenv
load_dotenv()


llm = GooglePalm(google_api_key=os.environ['GOOGLE_API_KEY'], temperature=0.2)

prompt = PromptTemplate(
    input_variables=['product'],
    template='What is good name for a company name that makes {product} ?'
)

chain = LLMChain(llm=llm, prompt=prompt)

if __name__ == '__main__':
    print(chain.run('websites'))