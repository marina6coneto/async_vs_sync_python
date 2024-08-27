import time

def sync_tks(task_id):
    print(f'Começando a tarefa {task_id}')
    time.sleep(2)
    print(f'Terminando a tarefa {task_id}')
    
start_time = time.time()

sync_tks(1)
sync_tks(2)
sync_tks(3)

print(f'Tempo decorrido: {time.time() - start_time:.2f}s')