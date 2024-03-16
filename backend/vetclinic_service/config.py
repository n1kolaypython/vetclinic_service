from dataclasses import dataclass, field
from functools import partial
import os


@dataclass(slots=True)
class DatabaseConfig:

    user: str = field(default_factory=partial(os.environ.get, "DB_USER_NAME"))
    password: str = field(default_factory=partial(os.environ.get, "DB_USER_PASSWORD"))
    name: str = field(
        default_factory=partial(os.environ.get, "DB_NAME", "vetclinic_service")
    )
    port: str = field(default_factory=partial(os.environ.get, "DB_PORT", "5432"))
    host: str = field(default_factory=partial(os.environ.get, "DB_HOST", "0.0.0.0"))
