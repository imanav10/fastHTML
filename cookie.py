from fastapi import FastAPI, Request
from fastapi.responses import Response
from datetime import datetime

app = FastAPI()
# from starlette.responses import Response was not working


@app.get('/settimestamp')
async def get(request: Request):
    now = datetime.now()
    res = Response(f'Set to {now}')
    res.set_cookie('timestamp', str(now))
    return res

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)