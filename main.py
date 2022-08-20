from db.pokedex import Pokedex
#from helper.WriteAJson import writeAJson

pokedex = Pokedex()
"""Buscar Pokemon por fraqueza:
weak='Water'
pokemons=pokedex.getPokemonNotWeaknesses(weak)"""

"""Buscar pokemon por ID
pokemons=pokedex.getPokemonssByID(2)"""

"""Buscar Pokemon por regex, que comeca com a letra :
letter = '^A.*$'
pokemons=pokedex.getPodemonsByregex(letter)"""

"""Buscar Pokemon por altura:
height = '0,71'
pokemons=pokedex.getPokemonsHeight(height)"""

"""Buscar Pokemon por CandyCount:
pokemons=pokedex.getPokemonsCandyCount()"""
"""Buscar Pokemon por SpawTime
time = '11:30'
pokemons=pokedex.getPokemonSpawTime(time)"""
print(pokemons)

#writeAJson(pokemons,'Bulbasaur')"""

