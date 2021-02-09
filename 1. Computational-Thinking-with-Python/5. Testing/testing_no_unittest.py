def sum(num_1, num_2):
    return abs(num_1) + num_2

def test_sum():
    num_1 = 5
    num_2 = 10
    
    resultado = sum(num_1, num_2)
    if resultado == 15:
        print('Test sum is ok')
    else:
        print('Test sum dió ' + resultado + ' y debió dar 15')

test_sum()