class Flowers:
    in_stock = True
    country = 'Netherlands'

    def __init__(self, title, colour, price, stem_length, avg_lifespan):
        self.title = title
        self.colour = colour
        self.price = price
        self.stem_length = stem_length
        self.avg_lifespan = avg_lifespan

    def __str__(self):
        return f'{self.title}: цена {self.price}, цвет {self.colour}'


class Rose(Flowers):
    def __init__(self, title, colour, price, stem_length, avg_lifespan, has_thorns):
        super().__init__(title, colour, price, stem_length, avg_lifespan)
        self.has_thorns = has_thorns


class Tulip(Flowers):
    def __init__(self, title, colour, price, stem_length, avg_lifespan, has_closed_bud):
        super().__init__(title, colour, price, stem_length, avg_lifespan)
        self.has_closed_bud = has_closed_bud


class Gerbera(Flowers):
    def __init__(self, title, colour, price, stem_length, avg_lifespan):
        super().__init__(title, colour, price, stem_length, avg_lifespan)


rose1 = Rose('rose', 'red', 100, 70, 7, True)
tulip1 = Tulip('tulip', 'yellow', 70, 40, 5, True)
gerbera1 = Gerbera('gerbera', 'pink', 50, 45, 10)
print(rose1.has_thorns)
print(tulip1.has_closed_bud)
print(gerbera1.stem_length)


class Bouquet:
    def __init__(self):
        self.bouquet = []

    def add_flower(self, flower):
        self.bouquet.append(flower)

    def count_price(self):
        price_of_the_bouquet = 0
        for flower in self.bouquet:
            price_of_the_bouquet = price_of_the_bouquet + flower.price
        return price_of_the_bouquet

    def when_withers(self):
        average_lifespan = 0
        for flower in self.bouquet:
            average_lifespan = average_lifespan + flower.avg_lifespan
        return round(average_lifespan / len(self.bouquet))

    def sort_by_price(self):
        self.bouquet.sort(key=lambda flower: flower.price)
        return self.bouquet

    def sort_by_colour(self):
        self.bouquet.sort(key=lambda flower: flower.colour)
        return self.bouquet

    def search_by_colour(self, colour):
        flower_list = []
        for flower in self.bouquet:
            if flower.colour == colour:
                flower_list.append(flower)
        return flower_list

    def __str__(self):
        lines = []
        for flower in self.bouquet:
            lines.append(str(flower))
        return "\n".join(lines)


bouquet1 = Bouquet()

bouquet1.add_flower(rose1)
bouquet1.add_flower(rose1)
bouquet1.add_flower(tulip1)
bouquet1.add_flower(gerbera1)

print(bouquet1.count_price())
print(bouquet1.when_withers())
# bouquet1.sort_by_price()
bouquet1.sort_by_colour()
print(bouquet1)

filtered = Bouquet()
filtered.bouquet = bouquet1.search_by_colour("red")
print(filtered)
