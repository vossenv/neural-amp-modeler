# File: metadata.py
# Created Date: Sunday May 19th 2024
# Author: Steven Atkinson (steven@atkinson.mn)

"""
Information from the simplified trainers that is good to know about.
"""

# This isn't part of ../metadata because it's not necessarily worth knowning about--only
# if you're using the simplified trainers!

from typing import List, Optional

from pydantic import BaseModel

__all__ = [
    "Data",
    "DataChecks",
    "Latency",
    "LatencyCalibration",
    "LatencyCalibrationWarnings",
    "Settings",
    "TrainingMetadata",
    "TRAINING_KEY",
]

# The key under which the metadata are saved in the .nam:
TRAINING_KEY = "training"


class Settings(BaseModel):
    """
    User-provided settings
    """

    fit_cab: bool
    ignore_checks: bool


class LatencyCalibrationWarnings(BaseModel):
    """
    Things that aren't necessarily wrong with the latency calibration but are
    worth looking into.

    :param matches_lookahead: The calibrated latency is as far forward as
        possible, i.e. the very first sample we looked at tripped the trigger.
        That's probably not a coincidence but the trigger is too sensitive.
    :param max_disagreement: The max disagreement between latency estimates. If
        it's too large, then there's a risk that something was wrong.
    """

    matches_lookahead: bool
    disagreement_too_high: bool


class LatencyCalibration(BaseModel):
    algorithm_version: int
    delays: List[int]
    safety_factor: int
    recommended: int
    warnings: LatencyCalibrationWarnings


class Latency(BaseModel):
    """
    Information about the latency
    """

    manual: Optional[int]
    calibration: LatencyCalibration


class DataChecks(BaseModel):
    version: int
    passed: bool


class Data(BaseModel):
    latency: Latency
    checks: DataChecks


class TrainingMetadata(BaseModel):
    settings: Settings
    data: Data
    validation_esr: Optional[float]
