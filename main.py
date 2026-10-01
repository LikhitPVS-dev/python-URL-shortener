from fastapi import FastAPI
from fastapi.responses import RedirectResponse
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
    


@app.get('/abc/{id}:',response_class=RedirectResponse)
def redirect(id:int)->RedirectResponse:
    if id in dict_.keys():
        return dict_[id]
    return {'detail':'id not found'}

