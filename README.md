## Rotina de Backup/Delete do ZABBIX

Este repositório tem como objetivo auxiliar na limpeza e Backup dos dados do banco de dados ZABBIX [MySQL].

Criado script <strong>main_backup.py<strong\> para Rotina de backup mensal onde será armazenado 12 backups, referente aos meses do ano, após periodo será subscrito toda a rotina alterando os meses consecutivos, exemplo:

  mês 01_01_2022<br>
  mês 01_02_2022<br>
  mês 01_03_2022<br>
  mês 01_04_2022<br>
  mês 01_05_2022<br>
  mês 01_06_2022<br>
  mês 01_07_2022<br>
  mês 01_08_2022<br>
  mês 01_09_2022<br>
  mês 01_10_2022<br>
  mês 01_11_2022<br>
  mês 01_12_2022<br>

Após o prazo de 12 meses será subscrito os backups por ordem crescente, exemplo:

  (mês 01_01_2023) - Backup Atualizado, assim por diante.<br>
  mês 01_02_2022<br>
  mês 01_03_2022<br>
  mês 01_04_2022<br>
  mês 01_05_2022<br>
  mês 01_06_2022<br>
  mês 01_07_2022<br>
  mês 01_08_2022<br>
  mês 01_09_2022<br>
  mês 01_10_2022<br>
  mês 01_11_2022<br>
  mês 01_12_2022<br>


Criado script main_delete.py para rotina de Limpeza dos dados aonde será declarado um dia "x" do mês para limpar o banco mysql ZABBIX. 

OBS:
Para agendamento da tarefa foi utilizado o Crontab (agendador de tarefas tipo Unix)
Script desenvolvido na Liguagem Python.

