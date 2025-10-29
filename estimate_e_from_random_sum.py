import random
import sys
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
    """메모리 효율적으로 라운드별 count만 수집"""
    counts = []
    for _ in range(n):
        _, _, count = generate_until_sum_exceeds_one()
        counts.append(count)
    return counts

def calculate_average_count(n, show_progress=True):
    """메모리 최적화: count 리스트를 저장하지 않고 바로 합산"""
    total_counts = Decimal("0")
    
    # 진행률 표시를 위한 설정
    update_interval = max(1, n // 100) if n > 100 else 1  # 최대 100번 업데이트
    
    for i in range(n):
        _, _, count = generate_until_sum_exceeds_one()
        total_counts += Decimal(count)
        
        # 진행률 표시
        if show_progress and (i + 1) % update_interval == 0 or i + 1 == n:
            progress = ((i + 1) / n) * 100
            completed = i + 1
            bar_length = 40
            filled_length = int(bar_length * (completed / n))
            bar = '█' * filled_length + ' ' * (bar_length - filled_length)
            
            # 두 줄을 업데이트: 이전 줄로 돌아가서 덮어쓰기
            sys.stdout.write(f'\r\033[1A' if i > 0 else '')  # 이전 줄로 이동 (두 번째부터)
            sys.stdout.write(f'({completed:,}/{n:,}회 완료)\n진행률: [{bar}] {progress:.1f}%')
            sys.stdout.flush()
    
    if show_progress:
        print()  # 진행률 표시 후 줄바꿈
    
    return total_counts / Decimal(n)

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

    # 메모리 최적화: count 리스트를 저장하지 않고 바로 합산
    average_count = calculate_average_count(n)
    e = Decimal("2.71828182845904523536028747135266249775724709369995")  # 50자리 고정 e
    absolute_error = abs(average_count - e)
    relative_error = (absolute_error / e) * 100

    print(f"총 {n:,}회 실행했으며, 평균 뽑은 횟수는 {format_decimal_with_spaces(average_count)}회입니다.")
    print(f"자연상수 e = {format_decimal_with_spaces(e)}")
    print(f"절대 오차: {format_decimal_with_spaces(absolute_error)}")
    print(f"상대 오차: {relative_error:.5f}%")

except ValueError as e:
    print("입력이 잘못되었습니다:", e)
