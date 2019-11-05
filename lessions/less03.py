# -*- coding: utf-8 -*- 

'''
    циклы
'''
def loop_for():
#    for number in range(5,15): 
#        print(number) # 5...14

    for number in [1,3,4,7,9]:
        print(number)

def loop_while():
    i=1
    while i<10:
        print(i,' => ',i*i)
        i=i+1
        if i==5: break


#loop_for()
loop_while()