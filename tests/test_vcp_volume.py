import pandas as pd

from app.patterns.vcp_volume import VCPVolumeAnalyzer


def test_volume_dry_up():

    data = pd.DataFrame(
        {
            "volume": [
                1000,
                980,
                950,
                900,
                870,
                820,
                790,
                760,
                730,
                700,
                680,
                650,
                620,
                600,
                580,
                560,
                540,
                520,
                500,
                480,
            ]
        }
    )

    analyzer = VCPVolumeAnalyzer()

    result = analyzer.analyze(data)

    assert result.is_drying_up
    assert result.contraction_percent > 20