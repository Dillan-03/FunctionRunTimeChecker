# Timer

import time

def timeThis(function):
    def wrapperFunction(*args):
        old_time =  time.time()

        values = function(*args)

        new_time = time.time()

        print("[timeThis] The time taken for this function was", round(new_time - old_time,5), "secs.")

        return values

    return wrapperFunction