import pytest
import random

random.seed(42)

from DP_grasshopper import hopper_alg

NUM_TESTS = 10_000
@pytest.mark.parametrize("hopper_length_list",
                         [random.randint(4, 10_000) for _ in range(NUM_TESTS)])
def test_grasshopper_sum(hopper_length_list: int) -> None:
    "Generates obstacles to overcome and asserts hopper algorithm returns correct sum"
    values_list = [float("-inf"), 1.0]
    obstacles_to_overcome = [random.choice(values_list)]
    for _ in range(hopper_length_list):
        new_obstacle = random.choice(values_list)
        if obstacles_to_overcome[-1] == float("-inf"):
            obstacles_to_overcome.append(1.0)
        else:
            obstacles_to_overcome.append(new_obstacle)
    alg_answer = hopper_alg(obstacles_to_overcome)
    assert alg_answer == sum(filter(lambda num: num != float("-inf"), obstacles_to_overcome))