def prime_factors(number):
    if is_prime(number):
        print(str(number) + " is al een priemgetal")
        return

    factors = []
    updated_number = number

    for i in range(number):
        if is_prime(updated_number): # als het restant een priemgetal is hebben we de laatste factor gevonden
            factors.append(int(updated_number))
            print("Alle priemfactors gevonden: ")
            print(factors)
            return
        if is_prime(i) and is_factor(i, updated_number):
                factors.append(i)
                updated_number = updated_number / i

def is_factor(possible_factor, number):
    # als de modulo 1 van de deling 0 is gaat het om een heel getal
    # en dus hebben we een factor te pakken
    if (number / possible_factor) % 1 == 0:
        return True

def is_prime(number):
    if number <= 1:
        return False

    # loop door alle getallen van 2 t/m de helft van het gegeven getal
    # als modulo i nooit 0 oplevert is het getal alleen deelbaar door 1 en door zichzelf
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            return False
    return True

prime_factors(600851475143)
