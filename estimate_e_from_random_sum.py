import random
from decimal import Decimal, getcontext

# 소수점 정밀도 설정 (최대 52자리 이상)
getcontext().prec = 60

def generate_until_sum_exceeds_one():
    numbers = []
    total = Decimal("0")
    
    while total <= 1:
        num = Decimal(str(random.random()))
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

def format_decimal_with_spaces(d: Decimal, precision=50):
    s = f"{d:.{precision}f}"  # 고정소수점 문자열
    int_part, frac_part = s.split(".")

    # 소수부를 3자리 단위로 나눔
    frac_part_spaced = " ".join([frac_part[i:i+3] for i in range(0, len(frac_part), 3)])

    return f"{int_part}.{frac_part_spaced}"

try:
    n = int(input("몇 번 실행하시겠습니까: "))
    if n <= 0:
        raise ValueError("양의 정수를 입력하세요.")

    rounds = generate_multiple_rounds(n)

    total_counts = Decimal("0")
    for i, r in enumerate(rounds, 1):
        # print(f"[{i}회차]")
        # print("  뽑은 수들:", r["numbers"])
        # print("  총합:", r["sum"])
        # print("  뽑은 횟수:", r["count"])
        # print()
        total_counts += Decimal(r["count"])

    average_count = total_counts / Decimal(n)
    e = Decimal("2.71828182845904523536028747135266249775724709369995")  # 50자리 고정 e
    absolute_error = abs(average_count - e)
    relative_error = (absolute_error / e) * 100

    print(f"총 {n:,}회 실행했으며, 평균 뽑은 횟수는 {format_decimal_with_spaces(average_count)}회입니다.")
    print(f"자연상수 e = {format_decimal_with_spaces(e)}")
    print(f"절대 오차: {format_decimal_with_spaces(absolute_error)}")
    print(f"상대 오차: {relative_error:.5f}%")

except ValueError as e:
    print("입력이 잘못되었습니다:", e)
