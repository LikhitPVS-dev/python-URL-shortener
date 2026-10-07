from fastapi import FastAPI,Response,HTTPException
from fastapi.responses import RedirectResponse,JSONResponse
from pydantic import BaseModel,HttpUrl
import datetime
import json
path='data.txt'
app=FastAPI()

class data(BaseModel):
    id:str
    url:HttpUrl
    
@app.post('/links/')
def postings(data_:data):
        
        data_pass={'id':data_.id,'url':str(data_.url),'click':0,'date':str(datetime.date.today())}        
        with open (path,'r') as file:
            try:
                dict_=json.load(file)
                dict_.append(data_pass)
            except json.decoder.JSONDecodeError:
                dict_=[]
                dict_.append(data_pass)
        
        with open(path,'w') as file:
            json.dump(dict_,file,indent=4)
            short_url=f'http://127.0.0.1:8000/code/{data_.id}'
            return {'short-url':short_url}
        #raise HTTPException(status_code=422,detail='invalid url')
        
    
@app.get('/code/{id}',response_class=RedirectResponse,status_code=307)
def redirect(id:str)->Response:
        try:
            with open(path,'r') as file:
                dic=(json.load(file))
            for i in dic:
                if i['id']==id:
                    i['click']+=1
                    with open (path,'w') as file:
                        json.dump(dic,file,indent=4)
                    return i[('url')]
            raise HTTPException(status_code=404,detail='{id} not found') 
        except json.decoder.JSONDecodeError:
            return JSONResponse(content='no data added')
@app.get('/links/code/stats/{id}')
def stats(id : str):
    with open(path,'r') as file:
        dic=json.load(file)
    for i in dic:
        if i['id']==id:
            return {'original url':i['url'],'date added':i['date']}
    raise HTTPException(status_code=404,detail=f'id {id} not found') 
@app.post('/links/code/{id}')
def delete(id : str):
    with open(path,'r') as file :
        dic=json.load(file)
    for i in dic:
        if i['id']==id:
            del dic[dic.index(i)]
            with open(path,'w') as file:
                json.dump(dic,file,indent=4)
            return {'detail':'data deletion sucessful'}

    raise HTTPException(status_code=404,detail=f'id {id} not found')
         
     