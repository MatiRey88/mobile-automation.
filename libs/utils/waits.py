import time
def retry(fn, attempts=3, delay=0.5):
    last_err = None
    for _ in range(attempts):
        try:
            return fn()
        except Exception as e:
            last_err = e; time.sleep(delay)
    raise last_err
