MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'studyful'
RENDERERS = [
    'eve.render.JSONRenderer'
]

RESOURCE_METHODS = ['GET','POST']
ITEM_METHODS = ['GET','PATCH','PUT']
X_HEADERS = ['Authorization', 'Content-type', 'Cache-Control',
             'If-Match']
X_DOMAINS = '*'

aluno_schema = {
    'firstname':{
        'type':'string', 
        'required':True
    },
    'aluno_email': {
        'type':'string',
        'required': True,
        'unique': True
    },
    'lastname': {'type':'string'},
    'nickname': {
        'type':'string', 
        'required': False
    },
    'ranking':{
        'type':'integer',
        'required': False
    },
    'skills':{
        'type':'list',
        'schema':{
            'type':'dict',
            'schema':{
                'subject':{'type':'string'},
                'topic': {'type':'string'},
                'score':{'type':'float'}
            }
        }
    }
}


historico_schema = {
    'aluno_email': {
        'type':'string',
        'required': True
    },
    'question_id':{
        'type': 'number',
        'required': True
    }
}

DOMAIN = {
    'aluno': {
        'schema':aluno_schema
    },
    'historico': {
        'schema':historico_schema,
        'additional_lookup': {
            'field': 'aluno_email',
            'url': 'regex("[\w]+")'
        }
    }
}