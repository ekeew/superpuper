from aiogram import Router


def get_main_router() -> Router:
    from .common import get_common_router
    from .admin import get_admin_router

    router = Router()
    router.include_router(get_common_router())
    router.include_router(get_admin_router())

    return router
