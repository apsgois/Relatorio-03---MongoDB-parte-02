from db.database import Database


class Pokedex:
    def __init__(self):
        self.db = Database(database="pokedex", collection="pokemons")
        self.db.resetDatabase()
        self.collection = self.db.collection

    def find(self, filters: dict):
        response = self.collection.find(filters)
        pokemons = []
        for pokemon in response:
            pokemons.append(pokemon)
        return pokemons

    def getAllPokemons(self):
        response = self.collection.find({}, {"name": 1, "_id": 0})
        pokemons = []
        for pokemon in response:
            pokemons.append(pokemon)
        return pokemons

    def getPokemonByName(self, name: str):
        response = self.collection.find({"name": name},
                                        {"_id": 0, "name": 1,
                                         "next_evolution": 1, "prev_evolution": 1,
                                         "type": 1, "weaknesses": 1})
        result = {}
        for pokemon in response:
            result = pokemon
        return result

    def getPokemonsByType(self, type: list):
        response = self.collection.find({"type": {"$all": type}}, {
            "_id": 0, "name": 1, "type": 1})
        result = []
        for pokemon in response:
            result.append(pokemon)
        return result
    def getPokemonssByID(self, id: int):
        response = self.collection.find({"id": id}, {
            "_id": 0, "name": 1, "type": 1})
        result = []
        for pokemon in response:
            result.append(pokemon)
        return result
    def getPokemonNotWeaknesses(self, weak: str):
        response = self.collection.find({"weaknesses":{"$ne":weak}},{
            "_id": 0, "name": 1, "type": 1})
        result = []
        for pokemon in response:
            result.append(pokemon)
        return result
    def getPokemonsCandyCount(self):
        response = self.collection.find({"candy_count":{"$gte":25, "$lte":50}},
        { "_id": 0, "name": 1, "type": 1})
        result = []
        for pokemon in response:
            result.append(pokemon)
        return result
    def getPokemonsHeight(self, height: str):
        response = self.collection.find({"height":{"$gt": height}}, {
            "_id": 0, "name": 1, "type": 1})
        result = []
        for pokemon in response:
            result.append(pokemon)
        return result
    def getPodemonsByregex(self, letter:str):
        response = self.collection.find({"name":{"$regex":letter}},{
            "name": 1, "type": 1})
        result = []
        for pokemon in response:
            result.append(pokemon)
        return result
    def getPokemonSpawTime(self, time:str):
        response = self.collection.find({"spawn_time":{"$eq":time}},{
            "name": 1, "type": 1})
        result = []
        for pokemon in response:
            result.append(pokemon)
        return result
    def getPokemonEvolutionsByName(self, name: str):
        pokemon = self.getPokemonByName(name)

        evolutions = [pokemon['name']]
        hasNextEvolutions = ('next_evolution' in pokemon)
        hasPrevEvolutions = ('prev_evolution' in pokemon)

        if hasNextEvolutions:
            nextEvolutions = list(pokemon['next_evolution'])
            for evolution in nextEvolutions:
                evolution = self.getPokemonByName(evolution['name'])
                evolutions.append(evolution['name'])

        if hasPrevEvolutions:
            previousEvolutions = list(pokemon['prev_evolution'])
            for evolution in previousEvolutions:
                evolution = self.getPokemonByName(evolution['name'])
                evolutions.append(evolution['name'])

        return evolutions
