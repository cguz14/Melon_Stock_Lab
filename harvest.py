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
        

    ## ' '.join(list)
    # Fill in the rest


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
