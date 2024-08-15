
def fizz_buzz(num: int) -> list[str]:
    if not isinstance(num, int):
        raise Exception('Valor recebido noo e um numero')
    elif num <= 0:
        raise Exception('Valor recebido e negativo ou zero')

    ret_list = []
    for n in range(1, num + 1):
        if n % 3 == 0 and n % 5 == 0:
            ret_list.append('FizzBuzz')
        elif n % 3 == 0:
            ret_list.append('Fizz')
        elif n % 5 == 0:
            ret_list.append('Buzz')
        else:
            ret_list.append(str(n))

    return ret_list
