def sum(a,b):
    total = a + b
    return total

print(sum(2, 3))

def full_name(first_name, last_name, inv=False):
    if inv:
        return f'{last_name} {first_name}'
    else:
        return f'{first_name} {last_name}'

print(full_name('Juan R.', 'Cifuentes'))