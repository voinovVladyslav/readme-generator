from dataclasses import dataclass


@dataclass
class Options:
    project_name: str
    celery: bool = False
    storage: bool = False
    pytest: bool = False
