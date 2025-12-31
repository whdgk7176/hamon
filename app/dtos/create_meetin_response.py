from typing import Annotated

from pydantic import BaseModel

from app.dtos.frozen_config import FROZEN_CONFIG


class CreateMeetingResponse(BaseModel):
    model_config = FROZEN_CONFIG

    url_code: Annotated[str,Field(description="ㅁㅣ팅url입니다")]

