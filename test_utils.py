from pong_game.game_utils import clamp, reflect_velocity

def test_clamp_inside():
    assert clamp(5, 0, 10) == 5

def test_clamp_below():
    assert clamp(-1, 0, 10) == 0

def test_clamp_above():
    assert clamp(20, 0, 10) == 10

def test_reflect_velocity():
    vx, vy = reflect_velocity(5, 2, 1.5)
    assert vx == -5
    assert vy == 3.5
