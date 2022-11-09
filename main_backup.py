from os import system
from datetime import date

d = date.today()

name_arq_backup = f'dumpall_{d.month}-{d.day}.sql'

system(f'mysqldump -u <usuário> --password=<senha> --all-databases > <diretório>/{name_arq_backup}')
