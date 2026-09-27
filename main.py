from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
dict_={}
paths={}
class data(BaseModel):
    id:int
    url:str
@app.post('/post')
def postings(id :int):
    if dict_[id]:
        paths.update({dict_[id]:f'abc/{id}'})
        return paths[dict_[id]]
    raise HTTPException (status_code=404,detail='id not found')
@app.get('/get_data/{id}')
def getting_data(id:int,url:str):
    if id not in dict_.keys():
        dict_.update({id:url})
        return {'detail':'update successful'}
    return {'detail':'id already exist'}
@app.get('/abc/{id}')
def new_url(id:int):
    return dict_[id]
