"""Risk score = f(severity, confidence, frequency, asset criticality) -> 0..100."""

from dataclasses import dataclass

W_SEVERITY = 0.35
W_CONFIDENCE = 0.25
W_FREQUENCY = 0.20
W_CRITICALITY = 0.20
# Number of events per correlation window at which frequency saturates.
FREQUENCY_CAP = 50


@dataclass(frozen=True)
class RiskInput:
    """Inputs of the risk model."""

    # 1..10
    severity: int
    # 0..1
    confidence: float
    # events in the correlation window
    frequency: int
    # 1..5
    asset_criticality: int


def risk_score(r: RiskInput) -> int:
    """Return an integer risk score between 0 and 100."""
    if not 1 <= r.severity <= 10:
        raise ValueError("severity must be between 1 and 10")
    if not 0 <= r.confidence <= 1:
        raise ValueError("confidence must be between 0 and 1")
    if r.frequency < 0:
        raise ValueError("frequency must be >= 0")
    if not 1 <= r.asset_criticality <= 5:
        raise ValueError("asset_criticality must be between 1 and 5")

    sev = r.severity / 10
    conf = r.confidence
    freq = min(r.frequency / FREQUENCY_CAP, 1)
    crit = r.asset_criticality / 5
    value = W_SEVERITY * sev + W_CONFIDENCE * conf + W_FREQUENCY * freq + W_CRITICALITY * crit
    return round(100 * value)


def risk_level(score: int) -> tuple[str, str]:
    """Map a score to (level, action)."""
    if score <= 30:
        return "Low", "log"
    if score <= 60:
        return "Medium", "alert"
    if score <= 80:
        return "High", "alert+temporary_block"
    return "Critical", "automated_response"
