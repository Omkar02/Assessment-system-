set_of_question = []
from Data import training_data as ques
import random
from Network import classify
print('Be Ready')
for iy in ques:
    set_of_question.append(iy['class'])
o = 0
score = 0
wrong_ans = []
random.seed(5)
while True :
    cn = random.randint(0,len(set_of_question)-1)
   # ab = set_of_question[cn]
    print(o+1,'.',set_of_question[cn])
    #ac = classify(ab)
    # af = ac[0]
    # ag = af[0]
    ad = input("Your answer : ")
    ac = classify(ad)
    if ac != []:
        ae = ac[0]
        af = ae[1]
        ak = ae[0]

        print(af)
    else:
        ae = 0
        af = 0
        ak = ''
    if set_of_question[cn] == ak:
        score = score + af
        #print('Score ==',score)
    elif set_of_question[cn] != ak:
       # print('Wrong')
        #print('Score ==',score)
        wrong_ans.append(set_of_question[cn])
    o+=1
    if o == 5:
        break
print('Wrong Ans: ')
for at in wrong_ans:
    print('---->',at)
print('---------------------------')
print('Score: ' , ((score/5)*10))
print('---------------------------')




