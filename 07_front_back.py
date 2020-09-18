"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""


def front_back_first_solution(a, b):
    a_half = int(len(a)/2) if len(a) % 2 == 0 else int(len(a)/2) + 1
    b_half = int(len(b)/2) if len(b) % 2 == 0 else int(len(b)/2) + 1
    a_front, b_front = a[0:a_half], b[0:b_half]
    a_back, b_back = a[a_half::], b[b_half::]

    return f'{a_front}{b_front}{a_back}{b_back}'


def front_back(a, b):
    a_half, b_half = half_string(a), half_string(b)
    a_front, a_back = cut_string(a, a_half)
    b_front, b_back = cut_string(b, b_half)

    return f'{a_front}{b_front}{a_back}{b_back}'

def half_string(s):
    return int(len(s)/2) if len(s) % 2 == 0 else int(len(s)/2) + 1

def cut_string(s, position):
    return s[0:position], s[position::]


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
