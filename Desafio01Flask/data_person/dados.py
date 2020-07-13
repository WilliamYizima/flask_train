pessoa_01 = {
    'id': '01',
    'nome': 'Ian Caleb Aragão',
    'cpf': '053.482.228-28',
    'interesses': {
            'produtos': ['Moto G1', 'Motorola Rzr', 'Moto G8'],
            'lugares': ['Cancun', 'Boipeba']}
    }

pessoa_02 = {
    'id': '02',
    'nome': 'Carolina Aurora Stefany Mendes',
    'cpf': '856.858.348-29',
    'interesses': {
        'produtos': ['Motorola One', 'Motorola Rzr', 'Moto E6'],
        'lugares': ['Brusque', 'Acre']}
}

pessoa_03 = {
    'id': '03',
    'nome': 'Mariah Isis Dias',
    'cpf': '615.003.138-15',
    'interesses': {
        'produtos': ['Futebol', 'Praia', 'Política'],
        'lugares': ['Rio de Janeiro', 'Salvador']}
}

def data_person()->list:
    return [pessoa_01, pessoa_02, pessoa_03]

if __name__ == '__main__':
    data_person()