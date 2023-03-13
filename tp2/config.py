from dynaconf import LazySettings, Validator

config = LazySettings(
    dotenv_override=True,
    encoding="utf-8",
    environments=False,
    envvar_prefix=False,
    load_dotenv=True,
    root_path="./conf/",
    validators=[
        Validator("NATS_SERVER", is_type_of=str, required=True),
        Validator("NATS_TOPIC", is_type_of=str, required=True),
        Validator("HOST", is_type_of=str, default="127.0.0.1"),
        Validator("PORT", is_type_of=int, default=8000),
    ],
)
