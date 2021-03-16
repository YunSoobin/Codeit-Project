"""
로또는 주 1회씩 열립니다. 하지만 한 사람이 한 회차에 여러 번 참여할 수도 있습니다.
번호는 1부터 45까지 있는데요. 주최측에서는 매주 6개의 '일반 당첨 번호'와 1개의 '보너스 번호'를 뽑습니다. 그리고 참가자는 1번 참여할 때마다 서로 다른 번호 6개를 선택합니다.
당첨 액수는 아래 규칙에 따라 결정됩니다.
내가 뽑은 번호 6개와 일반 당첨 번호 6개 모두 일치 (10억 원)
내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치, 그리고 내 번호 1개와 보너스 번호 일치 (5천만 원)
내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치 (100만 원)
내가 뽑은 번호 4개와 일반 당첨 번호 4개 일치 (5만 원)
내가 뽑은 번호 3개와 일반 당첨 번호 3개 일치 (5천 원)
여러분의 임무는 로또 시뮬레이션을 위한 함수들을 작성하는 것입니다.
"""

from random import randint

# 번호 뽑기
def generate_numbers(n):
    numbers=[]

    while n:
        num=randint(1,45)
        # numbers 리스트에 중복값이 들어가면 안됨
        if num not in numbers:
            numbers.append(num)
        n-=1

    return numbers


# 당첨 번호 뽑기
def draw_winning_numbers():
    # 일반 당첨 번호 6개 + 보너스 번호 1개
    winning_numbers=sorted(generate_numbers(7))

    # 일반 당첨 번호 6개는 정렬되어 있어야 함
    return sorted(winning_numbers[:6])+winning_numbers[6:]


# 겹치는 번호 개수
def count_matching_numbers(numbers,winning_numbers):
    list_num=set(numbers+winning_numbers)
    count=len(numbers+winning_numbers)-len(list_num)

    return count


# 당첨금 확인
def check(numbers, winning_numbers):
    count=count_matching_numbers(numbers,winning_numbers[:6])
    bonus_count=count_matching_numbers(numbers,winning_numbers[6:])
    if count==6:
        return 1000000000
    elif count==5 and bonus_count==1:
        return 50000000
    elif count==5:
        return 1000000
    elif count==4:
        return 50000
    elif count==3:
        return 5000
    else:
        return 0


