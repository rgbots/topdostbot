from dataclasses import dataclass, field

import yaml


@dataclass
class Bot:
    token: str
    admins: list[int]


@dataclass
class DB:
    host: str
    user: str
    password: str
    db_name: str
    url: str = field(init=False)

    # this method will be called after initialization of the class
    def __post_init__(self):
        self.url = f"postgres://{self.user}:{self.password}@{self.host}/{self.db_name}"


@dataclass
class TgServices:
    flyerapi_token: str = None
    hi_views_token: str = None


@dataclass
class Config:
    bot: Bot
    db: DB
    tg_services: TgServices


def load_config(path: str):
    with open(path) as file:
        config_file: dict = yaml.safe_load(file)

    return Config(
        bot=Bot(**config_file['bot']),
        db=DB(**config_file['db']),
        tg_services=TgServices(**config_file['tg_services']),
    )


config = load_config('config.yaml')
