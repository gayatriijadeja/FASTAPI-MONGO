from pydantic import BaseModel

class PRL_db (BaseModel):   
    
    filename: str
    sender: str
    subject: str
    time: str
    body: str
    ips: list[str]
    emails: list[str]
    domains:list[str]
    urls: list[str]
    headers_footers: list[str]

    