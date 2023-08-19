from fastapi import FastAPI

from core.configs import settings
from api.v1.api import api_router


app = FastAPI(title='Curso API - Segurança')
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level='info', reload=True)


"""
{
	"access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNjkyOTI5MTEzLCJpYXQiOjE2OTIzMjQzMTMsInN1YiI6IjYifQ.zIHr6G6OVA_Ti8oD5wf9T7CPunq5rDCX0Rzd1lzC3II",
	"token_type": "bearer"
}
"""