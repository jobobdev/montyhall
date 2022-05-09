# 이제 몬티홀을 만들어 봅시다.
# 자료형: int
# 변수 명: 선택한 문 = 's_door', 자동차 문 = 'c_door', 사회자가 열어줄 문 = 'o_door'

import random

class montyHall():
  def __init__(self):
    self.c_door = random.randrange(1,4)
    self.s_door = random.randrange(1,4)
    self.o_door = 0

# 1st 개발(본인)은 
# 클래스 self.s_door에 참여자가 선택한 문 번호를 저장함(1~3 중의 1개의 임의 수)
# 클래스 self.c_door에 자동차가 들어 있는 문 번호를 저장함(1~3 중의 1개의 임의 수)
# 2nd 개발부분에서 사용할 < 객체명 = montyHall() >(으)로 인스턴스를 할당하여 
# 결정 된 수들(s_door, c_door, o_door)을 접근할 수 있습니다.

## 2nd step E.G. #######################################################  
#  def emcee(self): 
#    if self.s_door == self.c_door: 
       # s와 c를 제외하고 나머지 문 번호들 중에 임의 선택
#      pass 
#    else: # s와 c를 제외하고 나머지 문 번호를 선택
#      pass 
## Final step E.G. #####################################################  
#  def changeAndResult(self, WhetherChange): #WhetherChange dtype is bool
#   if WhetherChange:
      # 참여자가 문을 바꾸는 경우
      # 2nd step에서 사회가자 open한 문과 참여자가 처음 선택한 문을 제외한 문을 선택
#      pass
#    else:
      # 참여자가 문을 바꾸지 않는 경우
#      pass

    # 그렇게 참여자가 새롭게 선택한 문 또는 
    # 처음 선택한 그대로의 문과 
    # 자동차가 있는 문을 비교하고 같으면 당첨!으로 누적.
    # 아니면 꽝으로 누적.

# 해당 클래스의 인스턴스를 만들어 1000회 반복 하고, 당첨될 확률과 되지 않을 확률을 출력한다.

###########################################################################

##################################################
#### 1st step에 값을 확인하는 예는 아래와 같다. ##########
##################################################
FirstStepResult = montyHall()
print(FirstStepResult.c_door, FirstStepResult.s_door)

