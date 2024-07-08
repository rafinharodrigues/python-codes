# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os
import json

jobs = []
last_job_deleted = []

def list_add(job):
    jobs.append(job)
    return

def list_undo(jobs):
    last_job_deleted.append(jobs.pop())
    list_show()
    return 

def list_redo():
    try:
        jobs.append(last_job_deleted[-1])
        last_job_deleted.pop()
    except:
        list_show()
    finally:
        list_show()

    return

def list_show():
    print()
    print('TAREFAS:\n')
    print(*jobs, sep='\n')
    print()
    return

def list_save():

    with open('lista.json', 'w', encoding='utf8') as list:
        json.dump(jobs, list, indent=True)

    print("Lista salva no arquivo lista.json")

def list_load():
    try:
        with open('lista.json', 'r', encoding='utf8') as list:
            jobs = json.load(list)
            return jobs
    except:
        return jobs



while True:
    print('Comandos: listar, desfazer, refazer, salvar, clear')
    comand = input('Digite uma tarefa ou comando: ')

    if comand == 'listar':
        jobs = list_load()
        list_show()
    elif comand == 'desfazer':
        list_undo(jobs)
    elif comand == 'refazer':
        list_redo()
    elif comand == 'clear':
        os.system('cls')
    elif comand == 'salvar':
        list_save()
    else:
        list_add(comand)
        list_show()
        
