import multiprocessing
import time


def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f'Square: {i*i}')

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f'Cube: {i*i*i}')

if __name__ == '__main__':

    #### Create 2 processes:
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)
    
    #### Start the process
    t = time.time()
    
    
    p1.start()
    p2.start()
    
    #### we will wait for process finish
    p1.join()
    p2.join()
    
    finished_time = time.time()-t
    print(f'Finished time is: {finished_time} sec')

# got best result in this .py file than jupyter notebook file. this one is best for this 
# multiprocesing.

