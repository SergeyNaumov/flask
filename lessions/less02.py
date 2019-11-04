# -*- coding: utf-8 -*- 
import json
import sys
import copy # для копирования структур
'''
    чтение файла, eval, работа с json
    копирование структур данных, указатели
'''
def struct_test():
    a={"a":1,"b":2}
    b=copy.deepcopy(a)
    a['c']=5
    print(a,b)

struct_test();

sys.exit();

def to_json(data):
    return json.dumps(data,ensure_ascii=False);

def from_json(str):
    return json.loads(str)


# запуск событий
def run_event(event):
    for e in event:
        e()

f = open('./conf/user.py', 'r')
form='';
exec(f.read())
f.close()

# FROM JSON
#data2=from_json('{"a":"Всем привет","b":[1,2,3]}')
#print data2['a'];

# TO_JSON
data={"name": "John Smith", "hometown": {"name": "New York", "id": "123"}}
#print( dataTojson(data) )
print( to_json(from_json(to_json(form))) )




#run_event(form['events']['permissions'])
#run_event(form['events']['after_insert'])


