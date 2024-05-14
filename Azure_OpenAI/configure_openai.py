import os
from langchain_core.messages import HumanMessage
from langchain_openai import AzureChatOpenAI
from ServiceNow import catalog_item


model = AzureChatOpenAI(
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
    azure_deployment=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"],
)

def get_sentiment(text):
  text = f"Sentiment analysis: {text} return only positive or negative"
  sentiment = model.invoke(text)
  return sentiment

def openAIFunction(question):
    similar_catalog_items = catalog_item.get_similar_catalog_item(question)
    # message = HumanMessage(
    #     content=question
    # )
    # answer=model.invoke([message])
    return similar_catalog_items


def task_decider():
    print("Hello")
