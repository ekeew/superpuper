import asyncio
import logging

import nats
from aiogram import Bot

from awesome.application.mailing import Mailing
from awesome.infrastructure.config import ApplicationSettings
from awesome.infrastructure.nats.adapter import MailAdapter


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)-8s [%(asctime)s] :: %(name)s : %(message)s"
    )
    logger = logging.getLogger(__name__)

    config = ApplicationSettings()

    bot = Bot(config.bot.token.get_secret_value())
    client = await nats.connect([config.nats.dsn])
    mail_adapter = MailAdapter(client)
    mailing = Mailing(bot, mail_adapter)

    try:
        logger.warning("Services started")
        await asyncio.gather(
            mailing.send_mails()
        )
    finally:
        await bot.session.close()
        await client.drain()
        logger.warning("Services stopped")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
