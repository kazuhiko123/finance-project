import time


def log_function_call(func):

    def wrapper(*args, **kwargs):

        print(f"\n[LOG] Calling: {func.__name__}")

        result = func(*args, **kwargs)

        print(f"[LOG] Finished: {func.__name__}")

        return result

    return wrapper


def measure_time(func):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(
            f"[TIME] {func.__name__}: "
            f"{end - start:.4f} sec"
        )

        return result

    return wrapper