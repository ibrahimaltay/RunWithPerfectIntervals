import time

def helloworld():
    print("HelloWorld!")

def run_method_with_perfect_intervals(method, interval_seconds):

    while True:
        timer_start = time.perf_counter_ns()
        method()
        timer_stop = time.perf_counter_ns()
        
        print('It took', (timer_stop - timer_start)/1000000, 'miliseconds to run this piece of code.')
        time.sleep(interval_seconds - (timer_stop - timer_start) / 1000000000)
        print("Execution time was subtracted from the sleeping time to ensure perfect timing!")
