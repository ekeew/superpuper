from aiogram import Router


def get_main_router() -> Router:
    from .common import get_common_router

    router = Router()

    router.include_router(get_common_router())

    return router
