import os

os.system("")


class HealthBar:
    symbol_remaining: str = ":green_square:"
    symbol_lost: str = ":red_square:"
    barrier: str = ":black_small_square:"

    def __init__(self,
                 entity,
                 length: int = 20,
                 is_colored: bool = True,
                 ) -> None:
        self.entity = entity
        self.length = length
        self.max_value = entity.health_max
        self.current_value = entity.health

        self.is_colored = is_colored

    def update(self) -> None:
        self.current_value = self.entity.health

    def draw_update(self):
        self.update()
        remaining_bars = round(self.current_value / self.max_value * self.length)
        lost_bars = self.length - remaining_bars
        health_bar_output = (f"**{self.entity.name}**'s HEALTH: {self.entity.health}/{self.entity.health_max}\n"
                             f'{self.barrier}'
                             f"{remaining_bars * self.symbol_remaining}"
                             f"{lost_bars * self.symbol_lost}"
                             f"{self.barrier}")
        return health_bar_output
