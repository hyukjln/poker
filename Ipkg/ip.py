import random as rd
from time import sleep


class Not_CD_Error(Exception) :
    def __init__(self):
        super().__init__('call , die 중에 고르세요')

class Not_RCD_Error(Exception) :
    def __init__(self):
        super().__init__('raise, call , die 중에 고르세요')


class Indian_poker :
    deck = [i for i in range(1,11)]*2
    def __init__(self):

        self.player = 25 # 플레이어 칩 갯수
        self.com = 25 # 컴퓨터 칩 개수

        self.c_card = 0 # 컴퓨터가 받을 카드가 될 예정
        self.p_card = 0 # 플레이어가 받을 카드가 될 예정


    def com_judge(self):
        if self.p_card in range(1,4):
            return 'raise'
            #self.c_bet += rd.choice(range(self.com + 1))
        elif self.p_card in range(4,7):
            return 'call'
        else : # 7~10
            return 'die'
            
    def who_win(self):
        if self.com_judge() != 'die' : # 둘다 살아있을때   컴퓨터 판단이 살아있다 라고 말한다면 
            if self.c_card > self.p_card : # 컴퓨터가 이겼을 때
                self.player -= self.p_bet
                self.com += self.p_bet
                print("Computer's card : {} , Player's card : {}. Computer won this turn".format(self.c_card,self.p_card))
            elif self.c_card < self.p_card : # 플레이어가 이겼을 때 
                self.player += self.c_bet
                self.com -= self.c_bet
                print("Computer's card : {} , Player's card : {}. Player won this turn".format(self.c_card,self.p_card))
            elif self.c_card == self.p_card :
                print("Computer's card : {} , Player's card : {}. It was a tie".format(self.c_card,self.p_card))
        elif self.com_judge() == 'die' : # 컴퓨터 die, 플레이어 이김
            self.player += self.c_bet
            self.com -= self.c_bet
            print("Computer's card : {} , Player's card : {}. Player won this turn".format(self.c_card,self.p_card))
        elif self.pd == 'die' : # 플레이어 die
            self.player -= self.p_bet
            self.com += self.p_bet
            print("Computer's card : {} , Player's card : {}. Computer won this turn".format(self.c_card,self.p_card))

    @staticmethod
    def get_cd(ans) : 
        if ans not in ['call','die'] : # ans 가 콜,다이 가 아닌 경우
            raise Not_CD_Error

    @staticmethod
    def get_rcd(ans) :
        if ans not in ['raise','call','die'] : # ans 가 콜,다이 가 아닌 경우
            raise Not_RCD_Error


    def play(self):
        i = 0 # 카드 한 장씩 줄 때 필요한 인덱스 넘버
        rd.shuffle(Indian_poker.deck)
        while i < 20 :
            self.c_card = Indian_poker.deck[i]
            self.p_card = Indian_poker.deck[i+1]

            self.p_bet = 1 # 플레이어가 거는 칩 갯수가 될 예정
            self.c_bet = 1 # 컴퓨터가 거는 칩 갯수가 될 예정

            print("Computer's card : {}.".format(self.c_card))

            while True :

                if self.com_judge() == 'raise' : # 컴퓨터가 레이즈할때

                    if self.p_bet != self.player : # 플레이어가 올인하지 않는 경우
                        if self.p_bet > 1 : # n번째 반복중인거임
                            self.c_bet += rd.choice(range(self.com + 1)) + self.p_bet
                        else : # 1번째 시도
                            self.c_bet += rd.choice(range(self.com + 1))

                        if self.c_bet > self.com : # 위 계산하는 과정에서 컴퓨터 베팅하는게 컴퓨터가 가진 칩 갯수보다 많게 될 때
                            self.c_bet = self.com # 그땐 컴퓨터가 올인하는 걸로 처리. (올인하면 상대는 콜이나 다이 둘 중 하나만 할 수 있다.)
  
                            while True :
                              try:   
                                self.pd = input('Com decided to all-in. What do you want to do? (call or die) : ') # 콜이나 다이 둘 중 하나 
                                Indian_poker.get_cd(self.pd)
                                break

                              except Exception as e:
                                print('Error raised : ',e)
                            
                            if self.pd == 'call' :
                                if self.c_bet > self.player : # 플레이어가 가진 칩 개수보다 컴퓨터가 올인한 칩의 개수가 많을 때
                                    self.p_bet = self.player # 플레이어는 올인을 할 수 밖에 없다.
                                else : # 컴퓨터의 올인한 칩 개수 이상을 플레이어가 가질 때 (여유가 있다)
                                    self.p_bet = self.c_bet # 플레이어는 컴퓨터의 올인을 받아칠 수 있다. (그만큼 베팅하게 된다.)
                                break
                            elif self.pd == 'die' : # 플레이어 die
                                break 
                                  
                        while True :
                            try:   
                                self.pd = input('Com decided to raise {}. What do you want to do? (raise, call or die) : '.format(self.c_bet)) # 레이즈, 콜, 다이 중 하나 
                                Indian_poker.get_rcd(self.pd)
                                break
                            
                            except Exception as e:
                                print('Error raised : ',e)

                        if self.pd == 'raise' :
                            self.p_bet += int(input('How much would you like to raise? : '))
                            continue # 컴퓨터가 다시 레이즈 하는 부분으로 돌아간다. 판이 점점 커지는 거지.
                        elif self.pd == 'call' :
                            if self.c_bet <= self.player : # 컴퓨터가 레이즈한 양을 플레이어가 그 양으로 콜할 여유가 있는 상황
                                self.p_bet = self.c_bet # 플레이어는 컴퓨터만큼 베팅한다.
                            else : 
                                self.p_bet = self.player # 플레이어는 콜하는데 자신의 전재산이 상대가 레이즈한 것보다 적은 상황임. 그래서 콜하는게 올인하는 거랑 다를게 없는 상황.
                            break
                        elif self.pd == 'die' : # 플레이어 die
                            break            

                    else : # 플레이어가 올인하면
                        self.c_bet = self.p_bet
                        break

                elif self.com_judge() == 'call' : # 컴퓨터가 콜할때
                    if self.p_bet <= self.com : # 컴퓨터가 플레이어가 베팅한만큼 콜할 여유가 있다
                        self.c_bet = self.p_bet
                    else : # 컴퓨터가 콜하는게 플레이어가 베팅한 것보다 부족한 경우 (컴퓨터 입장에선 올인임)
                        self.c_bet = self.com
                    
                    if self.p_bet != 1 : # 컴퓨터 콜 > 플레이어 레이즈 > 컴퓨터 콜하는 상황
                        self.c_bet = self.p_bet
                        break
                    else : # 처음인 상황
                        while True :
                            try:   
                                self.pd = input('Com decided to call. What do you want to do? (raise, call or die) : ') # 레이즈, 콜, 다이 중 하나 
                                Indian_poker.get_rcd(self.pd)
                                break
                            
                            except Exception as e:
                                print('Error raised : ',e)
                        
                    if self.pd == 'raise' :
                        self.p_bet += int(input('How much would you like to raise?  : '))
                        if self.player <= self.p_bet : # 플레이어가 올인하게 되는 경우
                            self.p_bet = self.player

                        continue # 컴퓨터가 다시 콜하는 부분으로 돌아간다. 
                    elif self.pd == 'call' :
                        if self.c_bet <= self.player :
                            self.p_bet = self.c_bet
                        else : 
                            self.p_bet = self.player # 플레이어는 콜하는데 자기가 가진 칩이 컴퓨터가 레이즈한 것보다 적은 상황임. 그래서 콜하는게 올인하는 거랑 다를게 없는 상황.
                        break
                    elif self.pd == 'die' : # 플레이어 die
                        break
                                
                elif self.com_judge() == 'die' : # 컴퓨터 die
                    print('Com decided to die')
                    break
                                                
            self.who_win() # 판단해준다.

            print('{}번째 턴, 컴퓨터칩 갯수 : {}, 플레이어칩 갯수 : {} \n'.format(int((i/2)+1),self.com,self.player))
            sleep(1.5) # 시간차 출력해준다
            i += 2 # 카드를 갱신해주기 위한 밑작업

            if self.player == 50 :# 플레이어가 최종적으로 이김
                print('Congratulations! You won!')
                break
            elif self.com == 50 :
                print('Too bad. You lost!')
                break

            continue

        # 카드가 다 떨어진 경우 (첫번째 while에서 빠져 나왔다.)
        if self.player > self.com :
            print('Congratulations! You won!')
            
        elif self.player == self.com :
            print('It was a tie.')
            
        else : # self.player < self.com
            print('Too bad. You lost!')
               
