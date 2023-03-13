import logging
import traceback

import nats
from nats.aio.client import Client
from nats.aio.msg import Msg

from tp2.config import config


async def err_cb(e: Exception):
    if e:
        logging.critical(f"nats: {type(e)}: {e}")
        print(traceback.format_exc())
    else:
        logging.warn("nats: attempting to reconnect")


async def reconnected_cb():
    logging.info("nats: reconnected")


async def connect():
    nc: Client = await nats.connect(
        config.nats_server,
        error_cb=err_cb,
        reconnected_cb=reconnected_cb,
        allow_reconnect=True,
        reconnect_time_wait=5,
        max_reconnect_attempts=9e6,
    )
    await nc.flush()
    print("subscribing")
    await nc.subscribe(config.nats_topic, cb=manage_message)
    print("subscribed")
    # now there is a task on the event loop which
    # is listening to nats messages and will call the callback
    # on a new one


async def manage_message(msg: Msg):
    print("got a message: ", msg)
