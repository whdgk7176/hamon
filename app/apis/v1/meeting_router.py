from fastapi import APIRouter

from app.dtos.create_meetin_response import CreateMeetingResponse

edgedb_router = APIRouter(prefix="/v1/edgedb/meetings", tags=["meeting"])

@edgedb_router.post(
    "",description="meeting을 생성합니다."
)
async def api_create_meeting_edgedb() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc ")

