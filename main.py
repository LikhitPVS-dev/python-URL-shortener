from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
dict_={}
class data(BaseModel):
    id:int
    url:str
@app.post('/url_/')
def postings(data_:data):
    data_dict=data_.model_dump()
    if data_.id not in dict_.keys():
        dict_[data_.id]=data_dict['url']
        return {'detail':'update successfull'}
    return {'detail':'key already exist'}
    
@app.get('/url_/{id}')
def getting_data(id:int):
    if id in dict_.keys():
        return dict_[id]
    return {'detail':'id not found'}

