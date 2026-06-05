# stats.py
# 점수 통계를 계산하는 모듈

import math


def calculate_variance(scores):
    """분산을 계산한다."""
    avg = sum(scores.values()) / len(scores)
    return sum((s - avg) ** 2 for s in scores.values()) / len(scores)


def calculate_stddev(scores):
    """표준편차를 계산한다."""
    return math.sqrt(calculate_variance(scores))


def print_stats(scores):
    """통계 정보를 출력한다."""
    print("\n" + "=" * 30)
    print("       통계 정보")
    print("=" * 30)
    print(f"  분산:     {calculate_variance(scores):>8.2f}")
    print(f"  표준편차: {calculate_stddev(scores):>8.2f}")
    print("=" * 30)