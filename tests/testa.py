from testb import division


def make_division(a, b):
    try:
        print('START TEST A')
        division(a, b)
        print('END TEST A')
    except ZeroDivisionError as e:
        print(f'ZERO TEST A: {e}')
        raise
    except Exception as e:
        print(f'EXCEPTION TEST A: {e}')
        raise
