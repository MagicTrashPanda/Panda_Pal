# HealthBar class to represent the health status of an entity
class HealthBar:
    # Define the symbols for the health bar
    symbol_remaining: str = ":green_square:"  # Symbol for remaining health
    symbol_lost: str = ":red_square:"  # Symbol for lost health
    barrier: str = ":black_small_square:"  # Symbol for the barrier of the health bar

    # Initialize the HealthBar with an entity and length of bar option
    def __init__(self,
                 entity,  # The entity whose health is represented
                 length: int = 20,  # The length of the health bar
                 ) -> None:
        self.entity = entity  # The entity whose health is represented
        self.length = length  # The length of the health bar
        self.max_value = entity.health_max  # The maximum health of the entity
        self.current_value = entity.health  # The current health of the entity

    # Update the current health value from the entity
    def update(self) -> None:
        self.current_value = self.entity.health

    # Draw the health bar and update the current health value
    def draw_update(self):
        self.update()  # Update the current health value
        remaining_bars = round(self.current_value / self.max_value * self.length)  # Calculate remaining health bars
        lost_bars = self.length - remaining_bars  # Calculate the number of lost health bars
        # Generate the health bar output
        health_bar_output = (f"**{self.entity.name}**'s HEALTH: {self.entity.health}/{self.entity.health_max}\n"
                             f'{self.barrier}'
                             f"{remaining_bars * self.symbol_remaining}"  # Draw the remaining health bars
                             f"{lost_bars * self.symbol_lost}"  # Draw the lost health bars
                             f"{self.barrier}")  # Draw the barrier
        return health_bar_output  # Return the health bar output
