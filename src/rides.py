# Takeoff/kick-out logic and ride objects with censoring
from dataclasses import dataclass, field
from typing import List, Optional, Dict

@dataclass
class Ride:
    track_id: int
    t0: float
    t1: Optional[float] = None
    duration_s: Optional[float] = None
    censored: bool = False
    direction: Optional[str] = None
    length_m: Optional[float] = None
    turns: List[float] = field(default_factory=list)

def compute_rides(tracks_iter, cfg):
    # tracks_iter yields (t, [ {id,bbox,speed,heading}, ... ])
    # TODO: implement planing detection, takeoff/kickout, stitching, censoring
    rides = []
    return rides
