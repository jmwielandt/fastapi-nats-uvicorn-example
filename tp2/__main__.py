import uvicorn

from tp2.config import config


def main():
    print("pre-run")
    uvicorn.run(
        "tp2:main", host=config.host, port=config.port, log_level="info", factory=True
    )


if __name__ == "__main__":
    print("on main!")
    main()
