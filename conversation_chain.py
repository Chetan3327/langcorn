from langchain.chains import ConversationChain
from langchain.chat_models import ChatGooglePalm
from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder, SystemMessagePromptTemplate


import os
from dotenv import load_dotenv
load_dotenv()


prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template('The following is a friendly conversation between a human and an AI(name of AI is Luna). AI is good at Coding and provides good solutions to the questions.'),
        MessagesPlaceholder(variable_name='history'),
        HumanMessagePromptTemplate.from_template('{input}')
    ]
)

llm = ChatGooglePalm(google_api_key=os.environ['GOOGLE_API_KEY'], temperature=0.2)
memory = ConversationBufferWindowMemory(k=3, return_messages=True)
conversation = ConversationChain(memory=memory, prompt=prompt, llm=llm)

if __name__ == '__main__':
    print(conversation.run(input='what is 2 + 2 ?'))