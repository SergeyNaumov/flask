# -*- coding: utf-8 -*- 

'''
    чтение файла, eval, работа с json
'''
f = open('./conf/user.py', 'r')
form='';
exec(f.read())
f.close()


def run_event(event):
    for e in event:
        e()

run_event(form['events']['permissions'])
run_event(form['events']['after_insert'])


