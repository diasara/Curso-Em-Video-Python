def is_number(s):
    try:
        float(s.replace(',', '.'))
    except ValueError:
        return False
    else:
        return True

def leiaDinheiro(msg):
    while True:       
        n = str(input(msg)).strip()

        if is_number(n):
            n = float(n.replace(',', '.'))
            break
        else:
            print('ERRO! DIGITE UM VALOR MONETÁRIO!')

    return float(n)
