from typing import Optional, Annotated
from datetime import datetime, timezone

from fastapi import FastAPI, Request, Query, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.db import get_db_session, engine, Base
from src.models.click import Click

from src.schemas.click import ClickSchema

OFFER = {"ZipRecruiter": "https://www.ziprecruiter.ie/"}

app = FastAPI(
    title='Click Tracking API'
)

#
# @app.on_event("startup")
# async def startup():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await engine.dispose()

@app.get("/click")
async def click(
        request: Request,
        async_session: Annotated[AsyncSession, Depends(get_db_session)],
        offer: str = Query(..., min_length=1, max_length=255),
        sub1: Optional[str] = Query(
        default=None,
        max_length=1000)
):
    client_ip = request.client.host if request.client else None
    user_agent = request.headers.get("user-agent")
    click = Click(
        offer=offer,
        sub1=sub1,
        timestamp=datetime.now(timezone.utc),
        ip=client_ip,
        user_agent=user_agent
        )

    async_session.add(click)
    await async_session.commit()

    return RedirectResponse(
        url=OFFER.get(offer, ""),
        status_code=302
    )

@app.get("/clicks", response_model=list[ClickSchema])
async def clicks(
        async_session: Annotated[AsyncSession, Depends(get_db_session)]
):
    query = select(Click).order_by(Click.timestamp.desc())
    clicks = (await async_session.execute(query)).scalars().all()

    return clicks