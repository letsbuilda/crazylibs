"""Story definition."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Story:
    title: str
    template: str
    questions: dict[int, str]
