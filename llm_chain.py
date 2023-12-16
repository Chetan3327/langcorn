from langchain.chains import LLMChain
from langchain.llms import GooglePalm
from langchain.prompts import PromptTemplate

import os
from dotenv import load_dotenv
load_dotenv()


llm = GooglePalm(google_api_key=os.environ['GOOGLE_API_KEY'], temperature=0.2)


prompt = PromptTemplate(
    input_variables=['file_name', 'code'],
    template="Update the code in the file named {file_name}. Implement or complete the code based on the provided {code}. Do not use any markdown-like code blocks (e.g., ```python) in your response. Provide the entire modified code for the file."
)

# prompt = PromptTemplate(
#     input_variables=['chapter_name', 'course_name', 'user_prompt'],
#     template='Create a short compelling description for a chapter {chapter_name} of course named {course_name}.  {user_prompt}.'
# )

chain = LLMChain(llm=llm, prompt=prompt)

if __name__ == '__main__':
    input_data = {
        "file_name": "test.py",
        "code": "const factorial = (n) => {    // inplement code for factorial of n }"
    }

    # input_data = {
    #     "chapter_name": "sql for begginers",
    #     "course_name": "sql",
    #     "user_prompt": ""
    # }
    print(chain.run(**input_data))