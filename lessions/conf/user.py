# -*- coding: utf-8 -*- 

def zz(a):
    return a*2
    
form={
    'title':'Конфиг компаний',
    'work_table':'user',
    'work_table_id':'id',
    'fields':[
        # {
        #     'sort':1,
        #     'description':'ю',
        #     'name':'status',
        #     'type':'select_values'
        # },
        {
            'sort':3,
            'description':'Наименование компании',
            'name':'firm',
            'type':'text'
        },
        {
            'sort':1,
            'description':'Я',
            'name':'status',
            'type':'select_values'
        },
        {
            'sort':5,
            'description':'Менеджер',
            'name':'manager_id',
            'type':'select_from_table'
        },
        {
            'sort':1,
            'description':'Статус',
            'name':'status',
            'type':'select_values'
        },
        {
            'sort':1,
            'description':'Б',
            'name':'status',
            'type':'select_values'
        },
        {
            'sort':1,
            'description':'А',
            'name':'status',
            'type':'select_values'
        },
    ]
}
