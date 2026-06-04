"""
Statistics during Dojo run.
"""

from dataclasses import dataclass
from datetime import datetime

@dataclass
class DojoStats:
    start_time: datetime


def display_stats(stats: DojoStats) -> None:
    now = datetime.now()
    print(f"Dojo play took {now - stats.start_time}")