from tp2.natscbs import connect as run_nats
from tp2.webserver import create_app

print("on init")


# can't be async
def main():
    print("hello")
    app = create_app(startup)  # pass the startup function here
    return app


# automatically called on uvicorn startup event
async def startup():
    print("on startup.")
    await run_nats()
    print("nats is running :D")
