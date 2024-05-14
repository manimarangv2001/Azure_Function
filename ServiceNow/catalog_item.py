import requests
import os
from langchain.docstore.document import Document
from langchain_openai import AzureOpenAIEmbeddings
from langchain_chroma import Chroma


def get_catalog_item():
    url = 'https://hexawaretechnologiesincdemo8.service-now.com/api/now/table/sc_cat_item?sysparm_query=active%3Dtrue&sysparm_limit=500'

    user = 'pankajj@hexaware.com'
    pwd = 'Pankaj@123'

    headers = {"Content-Type":"application/json","Accept":"application/json"}
    response = requests.get(url, auth=(user, pwd), headers=headers )
    if response.status_code != 200: 
        data = {'Status': response.status_code, 'Headers': response.headers, 'Error Response':response.json()}
  
    data = response.json()
    return data



def loadJSONFile(data):
    docs=[]
    for catalog_item in data['result']:
        metadata = {"sys_id":catalog_item['sys_id'], "sys_name":catalog_item['sys_name']}
        content = catalog_item['sys_name'] \
            +", "+catalog_item['short_description'] \
            +", "+catalog_item['description']
        docs.append(Document(page_content=content, metadata=metadata))
    return docs 



def get_similar_catalog_item(query):
    response = {}
    embedding_function = AzureOpenAIEmbeddings(model="Text-embedding")
    main_docs = loadJSONFile(data=get_catalog_item())
    db = Chroma.from_documents(main_docs, embedding_function)
    answer = db.similarity_search(query, k=4)
    detailedList = []
    response = {}
    for value in answer:
        answerlist = {}
        answerlist['content'] = value.page_content
        answerlist['sys_id'] = value.metadata['sys_id']
        answerlist['sys_name'] = value.metadata['sys_name']
        detailedList.append(answerlist)
    response = {'result': detailedList, 'response_detail':'similar_catalog_items'}
    return response

#[{'content':'sysname+shortdescription_description', 'sys_id'='234567890', 'sys_name'='name of the catalog item'}]
