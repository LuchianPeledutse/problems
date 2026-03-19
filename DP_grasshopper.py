# Grasshopper problem solution
# ----------------------------



def hopper_alg(obstacles: List[float]) -> float:
    N = len(obstacles)
    dp = [obstacles[0], obstacles[1] if obstacles[0] < 0 else obstacles[1] + obstacles[0]]
    for idx in range(2, N):
        idx_optimal_value = max(obstacles[idx] + dp[idx-1], obstacles[idx] + dp[idx-2])
        dp.append(idx_optimal_value)
    return dp[-1] if obstacles[-1] > 0 else dp[-2]

