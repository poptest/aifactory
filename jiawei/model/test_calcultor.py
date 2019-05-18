# encoding:utf-8


from jiawei.db.calcultor import Calcultor

a=2
b=4
act_ret=Calcultor.plus(a,b)
exp_ret=7

if exp_ret==act_ret:
    print("真")

else:
    print("假")
