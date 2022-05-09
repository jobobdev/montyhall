# 이제 몬티홀을 만들어 봅시다.
# 자료형: int
# 변수 명: 선택한 문 = 's_door', 자동차 문 = 'c_door', 사회자가 열어줄 문 = 'o_door'

#import random
#class Montyhall :
#    def __init__(self):
#        self.c_door = random.randint(1, 3)
#        self.s_door = 0
#        self.o_door = 0
#        
#    def select_door(self) :
#        self.s_door = random.randint(1, 3)
#        
#    def host_door(self) :
#        host_door = random.randint(1, 3)
#        while host_door == self.s_door or host_door == self.c_door :
#            host_door = random.randint(1, 3)
#            self.o_door = host_door
#        
    def switch_door(self) :
        self.s_door = 6 - self.c_door - self.o_door

    def hit_door(self) :
        if self.s_door == self.c_door :
            return True
        
    def run(self, switch=True) :
        #1번 문 선택함수를 넣어주세요
        #1번 호스트 문 선택함수를 넣어주세요
        if switch :
            self.switch_door()
        return self.hit()
#    
# if switch door
#
#RUNS = 10000
#for i in range(RUNS) :
#    hits = 0
#    monty = Montyhall()
#    if monty.run(switch=True) :
#        hits += 1
#        
#print(hits/RUNS)
#
# Not switch door