def confidence_colour(score: float) -> str:
    if score > 85:
        return "GREEN"
    if score >= 70:
        return "AMBER"
    return "RED"
