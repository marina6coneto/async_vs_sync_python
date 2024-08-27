import time
import asyncio

async def async_tsk(task_id):
    print(f'Começando a tarefa {task_id}')
    await asyncio.sleep(2)
    print(f'Terminando a tarefa {task_id}')
    
async def main():
    start_time = time.time()
    tasks = [async_tsk(1), async_tsk(2), async_tsk(3)]
    await asyncio.gather(*tasks)
    print(f'O tempo decorrido: {time.time() - start_time:.2f}s')


asyncio.run(main())
