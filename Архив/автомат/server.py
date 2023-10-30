from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
def index_page(data: str = Query(None)):
    print(data)
