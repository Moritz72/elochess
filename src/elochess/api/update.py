from fastapi import APIRouter, status

from elochess.api.models.requests import UpdateDwzRequest, UpdateEloRequest
from elochess.api.models.responses import UpdateResponse
from elochess.dwz import DwzCalculator
from elochess.elo import EloCalculator

update_router = APIRouter(prefix="/update", tags=["Update"])


@update_router.post(
    path="/elo",
    status_code=status.HTTP_200_OK,
    summary="Update Elo Rating",
    description="Calculates updated Elo ratings for given current ratings and results.",
    response_description="Elo Rating",
)
def update_elo_request(request: UpdateEloRequest) -> UpdateResponse:
    """Return the updated Elo rating."""
    rating = EloCalculator.update_rating(
        current_rating=request.current_rating,
        opponent_ratings=request.opponent_ratings,
        score=request.score,
        birth_year=request.birth_year,
        evaluation_year=request.evaluation_year,
        games_played=request.games_played,
        reached_2400=request.reached_2400,
    )
    return UpdateResponse(rating=rating)


@update_router.post(
    path="/dwz",
    status_code=status.HTTP_200_OK,
    summary="Update DWZ Rating",
    description="Calculates updated DWZ ratings for given current ratings and results.",
    response_description="DWZ Rating",
)
def update_dwz_request(request: UpdateDwzRequest) -> UpdateResponse:
    """Return the updated DWZ rating."""
    rating = DwzCalculator.update_rating(
        current_rating=request.current_rating,
        opponent_ratings=request.opponent_ratings,
        score=request.score,
        age=request.age,
        index=request.index,
    )
    return UpdateResponse(rating=rating)
