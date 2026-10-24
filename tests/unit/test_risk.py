import pytest

from insoc.risk.scoring import RiskInput, risk_level, risk_score

LEVEL_CASES = [
    (0, "Low"),
    (30, "Low"),
    (31, "Medium"),
    (60, "Medium"),
    (61, "High"),
    (80, "High"),
    (81, "Critical"),
    (100, "Critical"),
]


def test_max_input_is_critical():
    score = risk_score(RiskInput(10, 1.0, 100, 5))
    assert score == 100
    assert risk_level(score)[0] == "Critical"


def test_min_input_is_low():
    score = risk_score(RiskInput(1, 0.0, 0, 1))
    assert risk_level(score)[0] == "Low"


@pytest.mark.parametrize(("score", "level"), LEVEL_CASES)
def test_level_boundaries(score, level):
    assert risk_level(score)[0] == level


def test_invalid_input_rejected():
    with pytest.raises(ValueError):
        risk_score(RiskInput(11, 0.5, 1, 3))
