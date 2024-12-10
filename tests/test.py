from testa import make_division


def do_action(a, b):
    try:
        print('START TEST')
        make_division(a, b)
        print('END TEST\n')
    except ZeroDivisionError as e:
        print(f'ZERO TEST: {e}')
    except Exception as e:
        print(f'EXCEPTION TEST: {e}')


do_action(10, 2)
do_action(10, 0)
