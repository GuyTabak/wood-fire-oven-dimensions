from math import hypot


class FireBrick:
    def __init__(self, length: float, width: float, height: float):
        self.length = length
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Fire brick dimensions: length: {self.length}, width: {self.width}, height: {self.height}."


class OvenOpening:
    def __init__(self, width: float):
        self.width = width

    def __repr__(self):
        return f"Oven Opening width is {self.width}."


class VentLanding:
    def __init__(self, length: float):
        self.length = length

    def __repr__(self):
        return f"Vent Landing length is {self.length}."


class Oven:
    concrete_insulation_width = 10
    fiber_blanket_insulation_width = 5

    def __init__(self, radius: float, fire_brick: FireBrick, oven_opening: OvenOpening, vent_landing: VentLanding):
        self.radius = radius
        self.fire_brick = fire_brick
        self.oven_opening = oven_opening
        self.vent_landing = vent_landing

    def oven_outer_opening_width(self) -> float:
        return self.oven_opening.width + self.fire_brick.width * 2

    def min_oven_width(self) -> float:
        return 2 * (self.radius + self.concrete_insulation_width +
                    self.fiber_blanket_insulation_width + self.fire_brick.length / 2)

    def _inner_opening_edge_dist(self) -> float:
        # calculates the distance from the center of the oven to the inner edge of the oven opening
        return hypot(self.oven_outer_opening_width() / 2, self.radius)

    def _outer_opening_edge_dist(self) -> float:
        return hypot(self.oven_outer_opening_width() / 2, self.radius + self.vent_landing.length)

    def _fire_brick_insulation_dist(self) -> float:
        return self.radius + self.fire_brick.length / 2

    def _fiber_blanket_insulation_dist(self) -> float:
        return self._fire_brick_insulation_dist() + self.fiber_blanket_insulation_width

    def _concrete_insulation_dist(self) -> float:
        return self._fiber_blanket_insulation_dist() + self.concrete_insulation_width

    def __repr__(self):
        return f"Oven dimensions:\n" + \
               f"{self.fire_brick}\n" + \
               f"{self.oven_opening}\n" + \
               f"{self.vent_landing}\n" + \
               f"Inner opening edge dist: {self._inner_opening_edge_dist()}, " + \
               f"outer opening edge dist: {self._outer_opening_edge_dist()}, \n" + \
               f"the min oven width is: {self.min_oven_width()}," \
               f" oven outer opening width is : {self.oven_outer_opening_width()}"


if __name__ == "__main__":
    fire_brick_ = FireBrick(23, 11.4, 6.4)
    oven_opening_ = OvenOpening(45)
    vent_landing_ = VentLanding(15.24)
    oven_ = Oven(40, fire_brick_, oven_opening_, vent_landing_)
    print(oven_)
