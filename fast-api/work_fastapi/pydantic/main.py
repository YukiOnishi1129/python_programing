from datetime  import datetime
from pydantic import BaseModel

class Event(BaseModel):
    name: str = "未定"
    start_datetime: datetime
    participants: list[str] = []
    
external_data = {
	"name": "FastAPI勉強会",
	"start_datetime": "2021-09-01T12:00:00",
	"participants": ["Alice", "Bob"]
}

event = Event(**external_data)
print("イベント名:", event.name, type(event.name))
print("開始日時:", event.start_datetime, type(event.start_datetime))
print("参加者:", event.participants, type(event.participants))