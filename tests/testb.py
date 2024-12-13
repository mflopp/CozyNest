def division(a, b):
    try:
        print('START TEST B')
        print(a / b)
        print('END TEST B')
    except ZeroDivisionError as e:
        print(f'ZERO TEST B: {e}')
        raise
    except Exception as e:
        print(f'EXCEPTION TEST B: {e}')
        raise
