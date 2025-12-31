from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from app.apis.v1.meeting_router import edgedb_router as meeting__edgedb_router
app = FastAPI(
    default_response_class=ORJSONResponse
)

app.include_router(meeting__edgedb_router)

