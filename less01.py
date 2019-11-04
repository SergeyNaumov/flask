# -*- coding: utf-8 -*- 
import dumper
dumper.max_depth = 10

import sys
import importlib

sys.path.insert(1, './conf') #1

#name='ВаСя'
#print unicode(name,"utf-8").lower()
#sys.exit()

def load_config(name):
    mod=importlib.import_module(name)
    return mod.form


form=load_config('user');

#print form['title']

#from user import form

#print dumper.dump(form)


#import locale
#locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')






def out_fields(fields):
    for f in fields:
        print 'тип: ',f['type'],'\t;\tdesc: ',f['description']

def out_fields_sort(form):
    fields=sorted(form['fields'], key=lambda fld: unicode(fld['description'],"utf-8").lower())
    for f in fields:
        print f['description']

out_fields_sort(form)
#out_fields(form['fields'])


#print(dumper.dump(ab['Larry']))
#print(form['fields'][0]['description'])