from typing import Union, Dict, List

from pydantic import BaseModel

from typing import Union
import requests
import json


def get_token_from_code(url,dataobj):
    """
    It takes a url and a data object and returns a json object with the token or an error message

    :param url: The URL to the token endpoint
    :param dataobj: This is the data object that is sent to the server. It contains the client_id,
    client_secret, code, and redirect_uri
    :return: A dictionary with the key "access_token" and the value of the access token.
    """
    try:
        # Sending a post request to the url with the dataobj and a header.
        GetToken = requests.post(url,data=dataobj, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4146.4 Safari/537.36'})
    except:
        ret={"error":"unable to get token"}
    if GetToken.status_code==200:
        try:
            ret=json.loads(GetToken.text)
        except json.JSONDecodeError:
            ret = {"error":"200 with json decode error"}
    elif GetToken.status_code==400:
        ret={"error":"400 Unable to get token"}
    elif ret=={"error":"unable to get token"}:
        ret=ret
    else:
        ret={"error":"Unknown Error"}
    return ret        

class GlobalDateTime(BaseModel):
    dateTime:str # YYYY-MM-DDT00:00:00
    timeZone:str = 'China Standard Time'

class DefaultMsEvent(BaseModel):
    class EventBody(BaseModel):
        contentType: str = 'HTML'
        content:str = '' # str in raw or html. e.g."<html><head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"><meta name=\"Generator\" content=\"Microsoft Exchange Server\"><!-- converted from rtf --><style><!-- .EmailQuote { margin-left: 1pt; padding-left: 4pt; border-left: #800000 2px solid; } --></style></head><body><font face=\"Times New Roman\" size=\"3\"><span style=\"font-size:12pt;\"><a name=\"BM_BEGIN\"></a></span></font></body></html>"
    class loc(BaseModel):
        displayName:str
    class attendee(BaseModel):
        class emad(BaseModel):
            address:str
            name:str
        emailAddress:emad
        type:str = 'required'
    subject:str
    body:Union[EventBody,None] = None
    start:GlobalDateTime
    end:GlobalDateTime
    location:Union[None,loc] = None
    isReminderOn:Union[bool,None] = None # True default in Ms
    reminderMinutesBeforeStart:Union[int,None] = None # 15 minutes default in Ms; Minutes Ahead.
    attendees:Union[List[attendee],None] = None
    allowNewTimeProposals:Union[bool,None] = None
    isAllDay:bool = False
    transactionId:Union[None,str] = None # Maybe a UUID again, but not sure.
    def trans(self,a):
        self.transactionId = a

class DefaultMsToDo(BaseModel):
    class bodyDict(BaseModel):
        content:str=""
        contentType:str="text"
    title:str
    importance:str # low normal high
    isReminderOn:bool=True 
    status:str # notStarted, inProgress, completed, waitingOnOthers, deferred
    categories:list = [] # "红色类别",etc.
    body:bodyDict
    dueDateTime:GlobalDateTime
    startDateTime:GlobalDateTime
    reminderDataTime:GlobalDateTime

