def permission1():
    print("RUN permission 1")

def permission2():
    print("RUN permission 2")

def after_insert1():
    print("RUN after_insert1")

def after_insert2():
    print("RUN after_insert2")


form={
    'title':'Конфиг компаний',
    'work_table':'user',
    'work_table_id':'id',
    'events':{
        'permissions':[
            #permission1,
            #permission2
        ],
        
        'after_insert':[
            #after_insert1,
            #after_insert2,
        ]
    },
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




