def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
def floor(real):
    """ Bepaal het grootste gehele getal (int), dat kleiner dan of gelijk is aan real (float). """
    cheat = str(real).split(".") # import math en math.floor() doen is veel makkelijker maar ja.
    if cheat[1] != "0":
        if real < 0:
            return int(cheat[0]) - 1
        else:
            return int(cheat[0])
    else:
        return int(real)

def ceil(real):
    """ Bepaal het kleinste gehele getal (int), groter dan of gelijk aan real (float). """
    cheat = str(real).split(".") # import math en math.ceil() doen is veel makkelijker maar ja.
    if cheat[1] != "0":
        if real < 0:
            return int(cheat[0])
        else:
            return int(cheat[0]) + 1
    else:
        return int(real)
    return
def div(n):
    """
    Bepaal alle delers van een geheel getal.
    Het positieve gehele getal a is een deler van n, als er een positief geheel getal b is, zodat a × b = n.
    Args:
        n (int): Een geheel getal.
    Returns:
        list: Een gesorteerde lijst met alle delers van `n`.
    """
    divisors = []
    for x in range(1, (n + 1)): # range fuctie stopt voor het nummer wat wordt neergezet dus hij stop VOOR n en niet BIJ n dus vandaar de (n + 1).
        if n % x == 0: # Bij het getal 1 zou hij daarom niks moeten neerzetten want hij start bij 1 en stopt VOOR 1 dus zou hij gelijk stoppen, niks in de lijst zetten en een lege lijst returnen.
            divisors.append(x)
    return sorted(divisors)


def is_prime(n):
    """
    Bepaal of gegeven getal een priemgetal is.
    Hint: maak gebruik van de functie `div()`.
    Optioneel: bedenk een efficiënter alternatief.
    Args:
        n (int): Een geheel getal.
    Returns:
        bool: True als het getal een priemgetal is, anders False.
    """
    if len(div(n)) == 2:
        return True
    else:
        return False


def primes(num):
    """
    Bepaal alle priemgetallen kleiner dan een bepaald geheel getal.
    Hint: Maak gebruik van de functie `is_prime()`.
    Args:
        num (int): Een geheel getal.
    Returns:
        list: Een gesorteerde lijst met alle priemgetallen kleiner dan `num`.
    """
    primelist = []
    for x in range(1, num): # Dit keer alle priemgetallen die kleiner zijn dan num dus als num een priemgetal is wil je die niet mee laten tellen.
        if is_prime(x):
            primelist.append(x)
    return sorted(primelist)


def primefactors(n):
    """
    Bepaal de verzameling van priemfactoren van n.
    Args:
        n (int): Een geheel getal.
    Returns:
        list: Een gesorteerde lijst met alle priemfactoren van n. Als n kleiner
            dan 2, retourneer dan een lege lijst `[]`.
    """
    factors = []
    return sorted(factors)