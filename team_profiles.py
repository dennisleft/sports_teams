# classes for Team, Manager, Player
# Team - name, sport, colour, manager, stadium, league
# Manager - name, country, age
# Player - name, squad number, position, age, nationality

class Manager:

    def __init__(self, name, country, birth_year):
        self.name = name
        self.country = country
        self.birth_year = birth_year

    def age(self):
        from datetime import datetime
        return datetime.now().year - self.birth_year

    def profile(self):
        return f'\nName: {self.name}\nNationality: {self.country}\nAge: {self.age()}\n'


class Team(Manager):

    def __init__(self, name, sport, country, league, colours, manager, stadium, aka, town, birth_year):
        super().__init__(name, country, birth_year)
        self.sport = sport
        self.league = league
        self.colours = colours
        self.manager = manager
        self.stadium = stadium
        self.aka = aka
        self.town = town

    def profile(self):
        return f'\nTEAM PROFILE\nName: {self.name}\nSport: {self.sport}\nCountry: {self.country}\n' \
               f'Founded: {self.birth_year}\nLeague: {self.league}\nStadium: {self.stadium}\n' \
               f'Town: {self.town}\nAKA: {self.aka}\nCurrent Manager-> {self.manager}'


class Player(Manager):
    pass


# Manager
sarri = Manager('Maurizio Sarri', 'Italian', 1959)
valverde = Manager('Ernesto Valverde', 'Spanish', 1964)
kerr = Manager('Steve Kerr', 'American', 1965)
brown = Manager('Brett Brown', 'American', 1961)
print(valverde.profile(), brown.profile())

# Team
chelsea = Team('Chelsea', 'Football', 'England', 'English Premier League',
               'Blue', sarri.profile(), 'Stamford Bridge', 'The Blues',
               'London', 1905)
barca = Team('Barcelona', 'Football', 'Spain', 'La Liga', 'Blue and Red',
             valverde.profile(), 'Camp Nou', 'Barca', 'Barcelona', 1899)
sixers = Team('Philadelphia 76ers', 'Basketball', 'USA', 'NBA', 'Blue, White and Red',
              brown.profile(), 'Wells Fargo Center', 'Sixers', 'Philadelphia', 1946)

print(chelsea.profile(), barca.profile(), sixers.profile())
