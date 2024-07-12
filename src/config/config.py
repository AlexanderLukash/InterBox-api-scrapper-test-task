from dataclasses import dataclass

from environs import Env


@dataclass
class Config:
    BASE_URL: str


def load_config(path: str) -> Config:
    env = Env()
    env.read_env(path)

    return Config(
        BASE_URL=env.str("BASE_URL"),
    )
