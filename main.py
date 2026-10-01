from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import json
path='data.json'
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
        with open(path,'w') as file:
            json.dump(dict_,file,indent=4)
        return {'detail':'update successfull'}
    return {'detail':'key already exist'}
@app.get('/abc/{id}',response_class=RedirectResponse)
def redirect(id:int)->RedirectResponse :
    with open(path,'r') as file:
        dict_.update(json.load(file))
    if id in [int(i) for i in dict_.keys()]:
        return dict_[str(id)]
    return {'detail':'id not found'}

