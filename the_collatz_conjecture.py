def the_collatz_conjecture(until):
    for numero in range(1, until+1):
        print(numero, end='')
        while True:
            if numero == 1:
                break
            else:
                print(' -> ', end='')
            numero = int(3 * numero + 1) if numero % 2 else int(numero / 2)
            print(numero, end='')
        print('')

the_collatz_conjecture(10)
