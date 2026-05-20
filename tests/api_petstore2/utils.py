# retry logic 
from time import time


def retry(function, max_retry=3, delays=1):
    for attempt in range(max_retry): # meaning for each attemp with length of max_retry
        try:
            return function;
        except Exception as e:
            print(f"Attempt {attempt + 1} failed with error: {e}")
            if attempt < max_retry - 1: # meaning if the attempt is less than max_retry - 1, 
                #then we will wait for the delay before retrying
                time.sleep(delays)
    raise Exception(f"All {max_retry} attempts failed.")    



def test_retry():
    def flaky_function():
        import random
        if random.random() < 0.5:  # 50% chance to fail
            raise Exception("Flaky error!")
        return "Success!"
    
    try:
        result = retry(flaky_function, max_retry=5, delays=2)
        print(result)
    except Exception as e:
        print(e)