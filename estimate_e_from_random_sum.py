import random
import math

def generate_until_sum_exceeds_one():
    numbers = []
    total = 0.0

    while total <= 1.0:
        num = random.random()
        numbers.append(num)
        total += num

    return numbers, total, len(numbers)

def generate_multiple_rounds(n):
    result = []
    for _ in range(n):
        numbers, total, count = generate_until_sum_exceeds_one()
        result.append({
            "numbers": numbers,
            "sum": total,
            "count": count
        })
    return result

try:
    n = int(input("몇 번 실행하시겠습니까: "))
    if n <= 0:
        raise ValueError("양의 정수를 입력하세요.")

    rounds = generate_multiple_rounds(n)

    total_counts = 0
    for i, r in enumerate(rounds, 1):
        print(f"[{i}회차]")
        print("  뽑은 수들:", r["numbers"])
        print("  총합:", r["sum"])
        print("  뽑은 횟수:", r["count"])
        print()
        total_counts += r["count"]

    average_count = total_counts / n
    e = math.e
    absolute_error = abs(average_count - e)
    relative_error = (absolute_error / e) * 100

    print(f"총 {n}회 실행했으며, 평균 뽑은 횟수는 {average_count:.5f}회입니다.")
    print(f"자연상수 e = {e:.5f}")
    print(f"절대 오차: {absolute_error:.5f}")
    print(f"상대 오차: {relative_error:.3f}%")

except ValueError as e:
    print("입력이 잘못되었습니다:", e)
