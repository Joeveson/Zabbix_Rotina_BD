from MySQLdb import _mysql

tabelas = [
    'history',
    'history_log',
    'history_str',
    'history_uint',
    'history_text',
    'trends',
    'trends_uint',
    'alerts'
]

db = _mysql.connect("localhost","<usuário>","<senha>","<banco>")

for table in tabelas:
    
    db.query(f"truncate table <banco>.{table};")
