# kitchen.py
class Converter:
    RATES = {
        ("oz", "g"): 28.3495,
    }

    def reduce(self, quantity_or_sum, unit):
        return quantity_or_sum.reduce(unit, self)

    def convert(self, amount, from_unit, to_unit):
        if from_unit == to_unit:
            return amount
        rate = self.RATES[(from_unit, to_unit)]
        return amount * rate


class Quantity:
    def __init__(self, amount, unit):
        self.amount = amount
        self.unit = unit

    def times(self, multiplier):
        return Quantity(self.amount * multiplier, self.unit)

    def plus(self, other):
        return Sum(self, other)

    def reduce(self, unit, converter):
        converted = converter.convert(self.amount, self.unit, unit)
        return Quantity(converted, unit)

    def __eq__(self, other):
        return self.amount == other.amount and self.unit == other.unit

    def __repr__(self):
        return f"Quantity({self.amount}, {self.unit!r})"


class Sum:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def times(self, multiplier):
        return Sum(self.left.times(multiplier), self.right.times(multiplier))

    def reduce(self, unit, converter):
        left_amount = converter.convert(self.left.amount, self.left.unit, unit)
        right_amount = converter.convert(self.right.amount, self.right.unit, unit)
        return Quantity(left_amount + right_amount, unit)