# 이제 몬티홀을 만들어 봅시다.
# 자료형: int
# 변수 명: 선택한 문 = 's_door', 자동차 문 = 'c_door', 사회자가 열어줄 문 = 'o_door'
# host_door = 게임 도중 진행자가 열어주는 문을 선택할 때 사용한 변수
# runs 은 게임을 돌린 횟수
# hits는 당첨


import random


class Montyhall:
    def __init__(self):
        self.c_door = random.randint(1, 3)
        self.s_door = 0
        self.o_door = 0

    def select_door(self):
        self.s_door = random.randint(1, 3)
        return s_door

    def host_door(self):
        host_door = random.randint(1, 3)
        while host_door == self.s_door or host_door == self.c_door:
            host_door = random.randint(1, 3)
        o_door = host_door
        return o_door

    def switch_door(self):
        # 문 값의 합 = 1 + 2 + 3 = 6
        self.s_door = 6 - self.s_door - self.o_door
        return s_door

    def hit(self):
        if s_door == c_door:
            return True

    def run(self, switch=True):
        self.select_door()  # s_door 값을 뽑아냄
        self.host_door()  # o_door 값을 뽑아냄
        if switch:
            self.switch_door()  # switch한다면 s_door가 변경됨.
        return self.hit()  # s_door와 c_door 값을 비교 후 같으면 True반환.


# Swtich Door
runs = 1000
monty = Montyhall()
hits = 0
for i in range(runs):
    if monty.run(switch=True) == True:
        hits += 1
print("%.1f%%" % (game / 100))

# Do not Switch Door
hits = 0
for i in range(runs):
    if monty.run(switch=False):
        hits += 1
print("%.1f%%" % (game / 100))
