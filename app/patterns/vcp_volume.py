"""
===============================================================================
VCP Volume Analysis
===============================================================================

Volume contraction analysis for the
Volatility Contraction Pattern (VCP).

This module measures whether volume progressively dries up
during the construction of the base.
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


@dataclass(slots=True)
class VolumeAnalysis:
    """
    Volume contraction statistics.
    """

    average_volume: float

    first_half_volume: float

    second_half_volume: float

    contraction_percent: float

    is_drying_up: bool


class VCPVolumeAnalyzer:
    """
    Analyze whether volume contracts across a base.
    """

    def analyze(
        self,
        data: pd.DataFrame,
    ) -> VolumeAnalysis:

        if len(data) < 20:
            return VolumeAnalysis(
                average_volume=0.0,
                first_half_volume=0.0,
                second_half_volume=0.0,
                contraction_percent=0.0,
                is_drying_up=False,
            )

        volume = data["volume"].astype(float)

        midpoint = len(volume) // 2

        first = volume.iloc[:midpoint].mean()

        second = volume.iloc[midpoint:].mean()

        average = volume.mean()

        contraction = 0.0

        if first > 0:
            contraction = (first - second) / first * 100

        return VolumeAnalysis(
            average_volume=average,
            first_half_volume=first,
            second_half_volume=second,
            contraction_percent=contraction,
            is_drying_up=contraction >= 20,
        )