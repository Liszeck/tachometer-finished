
import os
import sys
import logging
import time

LOG_FORMAT = '%(asctime)s | %(process)d | %(levelname)s | %(message)s'
logging.basicConfig(filename='signals.log',
                    filemode='w',
                    format=LOG_FORMAT,
                    level=logging.DEBUG)
LOG = logging.getLogger()

def sleep_and_count(max_count: int = 1, sleep_inerval: int = 1) -> None:
    for i in range(max_count):
        LOG.info(f'Iteration: {i}')
        time.sleep(sleep_inerval)



if __name__ == '__main__':
    
    print('Hello World')
    print(f'Operating System: {os.name}')
    print(f'Uname: {os.uname()}')
    print(f'Platform: {sys.platform}')

    LOG.error('Hello')
    child_pid = os.fork()
    if child_pid == 0:
        LOG.info(f'Child Process! PID: {os.getpid()} PPID: {os.getppid()}')
        sleep_and_count(10)
        LOG.info(f'Child Process! PID: {os.getpid()} Counting is finished!')
        LOG.info(f'Child Process! PID: {os.getpid()} Terminate')
        exit(0)
    else:
        LOG.info(f'Parent Process! PID: {os.getpid()} PPID: {os.getppid()}')
        os.wait()
        LOG.info(f'Parent Process! Child Process has terminated!')
        exit(0)
