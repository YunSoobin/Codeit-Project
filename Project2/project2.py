"""
컴퓨터는 0과 9 사이의 서로 다른 숫자 3개를 무작위로 뽑습니다. 예를 들어서 컴퓨터가 5, 2, 3을 뽑을 수도 있고 6, 7, 4를 뽑을 수도 있는 거죠.
사용자는 컴퓨터가 뽑은 숫자의 값과 위치를 맞추어야 합니다.
컴퓨터는 사용자가 입력한 숫자 3개에 대해서, 아래의 규칙대로 스트라이크(S)와 볼(B)의 개수를 알려줍니다.
숫자의 값과 위치가 모두 일치하면 S입니다.
숫자의 값은 일치하지만 위치가 틀렸으면 B입니다.
예를 들어 컴퓨터가 1, 2, 3을 뽑았다고 가정합시다. 사용자가 1, 3, 5를 입력하면, 1S(1의 값과 위치가 일치) 1B(3의 값만 일치)입니다.
기회는 무제한입니다. 하지만 몇 번의 시도 끝에 맞췄는지 기록됩니다.
3S(숫자 3개의 값과 위치를 모두 맞춘 경우)가 나오면 게임이 끝납니다.
진행 방식
1. "0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다."가 출력됩니다.
2. "숫자 3개를 하나씩 차례대로 입력하세요."가 출력됩니다.
3. "1번째 숫자를 입력하세요: "가 출력되고, 사용자로부터 입력을 받습니다. 마찬가지로 "2번째 숫자를 입력하세요: "와 "3번째 숫자를 입력하세요: "가 출력되고, 사용자로부터 각각 입력을 받습니다. 만약 사용자가 중복되는 숫자를 입력하거나 범위에서 벗어나는 숫자를 입력하면, 사용자로부터 입력을 다시 받습니다.
4. 사용자가 올바르게 숫자 3개를 입력하면, 규칙에 따라 "*S *B"가 출력됩니다.
5. 3S가 아닌 경우, 2번부터 다시 진행합니다.
6. 사용자가 3S를 달성하면, "축하합니다. *번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다."가 출력됩니다. 그리고 게임은 종료됩니다.
"""

from random import randint

# 숫자 3개 뽑기
def generate_numbers():
    numbers = []

    while len(numbers)<3:
        new_numbers=randint(0,9)
        if new_numbers not in numbers:
            numbers.append(new_numbers)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


# 숫자 예측하기
def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []

    while len(new_guess)<3:
        num=int(input(("{}번째 숫자를 입력하세요: ".format(len(new_guess)+1))))
        # 유저가 범위에서 벗어나는 숫자를 입력한 경우
        if num<0 or num>9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        # 유저가 이미 입력한 숫자를 다시 입력한 경우
        elif num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(num)

    return new_guess


# 점수 계산
def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for i in range(3):
        if guess[i]==solution[i]:
            strike_count+=1
        elif guess[i] in solution:
            ball_count+=1

    return strike_count, ball_count


ANSWER = generate_numbers()
tries = 0

while 1:
    tries += 1
    GUESS = take_guess()
    strike, ball = get_score(GUESS, ANSWER)
    print("{}S {}B".format(strike, ball))
    if strike==3:
        break

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))