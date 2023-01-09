from fastapi import FastAPI


datastore = {
    1001: {"name": "Jordan Bruno", "teacher_rank": 7},
    1002: {"name": "Liping Zheng", "teacher_rank": 2}, 
    1003: {"name": "Michael Mortenson", "teacher_rank": 5}
            }

app = FastAPI()

@app.get("/all")
async def get_all():
    return datastore


@app.get("/ids/{id}")
async def get_by_id(id: int):
    try:
        return datastore[id]
    except:
        return "No records found"

    
@app.get("/names/{name}")
async def get_by_name(name):
    output = "No records found" 
    for sid in datastore:
        if datastore[sid]['name'] == name:
            output = datastore[sid]
    return output