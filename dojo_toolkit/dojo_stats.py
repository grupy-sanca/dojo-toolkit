"""
Statistics during Dojo run.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class DojoStats:
    start_time: datetime
    rounds: int = 0


def display_stats(stats: DojoStats) -> None:
    now = datetime.now()
    print(f"\n{stats.rounds} rounds played and took {now - stats.start_time}")
