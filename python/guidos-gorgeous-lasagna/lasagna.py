"""
Lasagna module
"""

EXPECTED_BAKE_TIME = 40

PREPARATION_TIME = 2

def bake_time_remaining(minutes: int):
    """
    Return bake remaining time.

    """
    return EXPECTED_BAKE_TIME - minutes

def preparation_time_in_minutes(layers: int):
    """
    Return preparation time.
    """
    return PREPARATION_TIME * layers

def elapsed_time_in_minutes(layers: int, elapsed_bake_time: int):
    """
    Return elapsed cooking time.
    This function takes two numbers representing the number of layers & the time already spent
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return PREPARATION_TIME * layers + elapsed_bake_time