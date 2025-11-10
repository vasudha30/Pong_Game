# game_utils.py - pure python helpers used by game and tests

def clamp(val, low, high):
    """Clamp val into [low, high]."""
    return max(low, min(high, val))

def reflect_velocity(vx, vy, offset=0.0):
    """Reflect horizontal velocity and tweak vertical velocity by offset."
    return -vx, vy + offset
