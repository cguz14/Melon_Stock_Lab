############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []
        self.name = name
        self.code = code
        self.color = color
        self.first_harvest = first_harvest
        self.is_seedeless = is_seedless
        self.is_bestseller = is_bestseller

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)
        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
    muskmelon = MelonType("musk", 1998, "Green", True, True, "Muskmelon")
    muskmelon.add_pairing("mint")

    casaba = MelonType("cas", 2003, "Orange", False, False, "Casaba")
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")
    # print(casaba.pairings)

    crenshaw = MelonType("cren", 1996, "Green", False, False, "Crenshaw")
    crenshaw.add_pairing("prosciutto")

    yellow_watermelon = MelonType("yw", 2013, "Yellow", False, True, "Yellow Watermelon")
    yellow_watermelon.add_pairing("ice cream")

    all_melon_types = [muskmelon, casaba, crenshaw, yellow_watermelon]

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        pairs = ""
        pairs = ' and '.join(melon.pairings)
        print(f'{melon.name} pairs with {pairs}.')


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melonDictionary = {}

    for melon in melon_types:
        melonDictionary[melon.code] = melon

    return melonDictionary

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    def __init__(
            self, harvestNumber, type, shapeRating, colorRating, field, harvester
    ):
        
        self.type = type
        self.harvestNumber = harvestNumber
        self.shapeRating = shapeRating
        self.colorRating = colorRating
        self.field = field
        self.harvester = harvester

    # Fill in the rest
    # Needs __init__ and is_sellable methods

    def is_sellable(self):
        
        if self.shapeRating > 5 and self.colorRating > 5 and self.field != 3:
            return True
        else:
            return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons_by_id = make_melon_type_lookup(melon_types)

    melon1 = Melon(1, melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon2 = Melon(2, melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon3 = Melon(3, melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon4 = Melon(4, melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon5 = Melon(5, melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon6 = Melon(6, melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon7 = Melon(7, melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon8 = Melon(8, melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon9 = Melon(9, melons_by_id['yw'], 7, 10, 3, 'Sheila')

    return [melon1, melon2, melon3, melon4, melon5, melon6, melon7, melon8, melon9]

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        melonNum = f"Melon {melon.harvestNumber}"
        harvestedBy = f"harvested by {melon.harvester}"
        field = f"from Field {melon.field}"
        sellable = f"-- CAN BE SOLD" if melon.is_sellable() else f"-- NOT SELLABLE"

        print(f"{melonNum} {harvestedBy} {field} {sellable}")
        # if melon.is_sellable():
        #     print(f"Melon {melon.harvestNumber} harvested by {melon.harvester}",
        #         f"from Field {melon.field} -> CAN BE SOLD. MMMMMMelon!")
        # else:
        #     print(f"Melon {melon.harvestNumber} harvested by {melon.harvester}",
        #         f"from Field {melon.field} -> CAN NOT BE SOLD. Don't Sell!")
