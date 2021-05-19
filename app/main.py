from fastapi import FastAPI, Request, Response

app = FastAPI(docs_url=None, redoc_url=None)


@app.post("/")
async def echo_body(request: Request):
    content = await request.body()
    return Response(content=content, media_type="text/plain")
