from fastapi import HTTPException


class ContentPilotException(Exception):

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


def raise_not_found(message="Resource not found"):
    raise HTTPException(
        status_code=404,
        detail=message,
    )


def raise_bad_request(message="Bad request"):
    raise HTTPException(
        status_code=400,
        detail=message,
    )


def raise_server_error(message="Internal server error"):
    raise HTTPException(
        status_code=500,
        detail=message,
    )
