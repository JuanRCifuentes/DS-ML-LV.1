countries = {
    'Iceland': 35,
    'Ireland': 32,
    'Canada': 50
}

def busca_pais(paises, pais):
    """
    Paises es un diccionario. Pais es la llave.
    Codigo con el principio EAFP.
    """
    
    try:
        return paises[pais]
    except KeyError:
        return None

def busca_pais_notcool(paises, pais):
    if(paises.get(pais, 'none') == 'none'):
        return None
    else:
        return paises.get(pais)

country = 'Colombia'
print(busca_pais(countries, country))
print(busca_pais_notcool(countries, country))

country = 'Canada'
print(busca_pais(countries, country))
print(busca_pais_notcool(countries, country))
