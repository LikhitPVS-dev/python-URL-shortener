from fastapi import FastAPI,HTTPException
from fastapi.responses import RedirectResponse,JSONResponse
from pydantic import BaseModel
import json
path='data.txt'
app=FastAPI()

class data(BaseModel):
    id:str
    url:str
@app.post('/url_/')
def postings(data_:data):
    data_pass={data_.id:data_.url,'click':0}
    with open (path,'r') as file:
        try:
            dict_=json.load(file)
            dict_.append(data_pass)
            
        except json.decoder.JSONDecodeError:
            dict_=[]
            dict_.append(data_pass)
    with open(path,'w') as file:
        json.dump(dict_,file,indent=4)
    
@app.get('/abc/{id}',response_class=RedirectResponse,status_code=307)
def redirect(id:str):
    try:
        with open(path,'r') as file:
            dic=(json.load(file))
        flag=False
        for i in dic:
            if (id) in i.keys():
                i['click']=+1
                flag=True
                return i[(id)]
        if not flag:
            return {'detail':'id not found'}
    except json.decoder.JSONDecodeError:
        return {'detail':'no data yet'}