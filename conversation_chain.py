from langchain.chains import ConversationChain
from langchain.chat_models import ChatGooglePalm
from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder, SystemMessagePromptTemplate


import os
from dotenv import load_dotenv
load_dotenv()


prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template('Following is a formal conversation between a human and an AI. AI knows about building the layout of a basic catalogue and the norms it should follow. Chatbot can answer the routes each button might redirect to, example, a scoring catalogue option, option to become a seller, option to buy subscriptions for the site according to the user. The site also offers free two reviews for the catalogue.'),
        MessagesPlaceholder(variable_name='history'),
        HumanMessagePromptTemplate.from_template('{input}')
    ]
)

llm = ChatGooglePalm(google_api_key=os.environ['GOOGLE_API_KEY'], temperature=0.2)
memory = ConversationBufferWindowMemory(k=3, return_messages=True)
conversation = ConversationChain(memory=memory, prompt=prompt, llm=llm)

if __name__ == '__main__':
    print(conversation.run(input='what is 2 + 2 ?'))
