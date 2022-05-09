# 이제 몬티홀을 만들어 봅시다.
# 자료형: int
# 변수 명: 선택한 문 = 's_door', 자동차 문 = 'c_door', 사회자가 열어줄 문 = 'o_door'

import random

class montyHall():
  def __init__(self):
    self.c_door = random.randrange(1, 4)
    self.s_door = random.randrange(1, 4)
    self.o_door = 0

# 1st 개발(본인)은 
# 클래스 self.s_door에 참여자가 선택한 문 번호를 저장함(1~3 중의 1개의 임의 수)
# 클래스 self.c_door에 자동차가 들어 있는 문 번호를 저장함(1~3 중의 1개의 임의 수)
# 2nd 개발부분에서 사용할 < 객체명 = montyHall() >(으)로 인스턴스를 할당하여 
# 결정 된 수들(s_door, c_door, o_door)을 접근할 수 있습니다.

# 사용예는 아래와 같다.

FirstStepResult = montyHall()
print(FirstStepResult.c_door, FirstStepResult.s_door)

