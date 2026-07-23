from fastapi import FastAPI


def register_routers(app: FastAPI, routers: list):

    for router in routers:
        app.include_router(router)
