class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight

class BaseRobot:
    def __init__(self, weight: int, name: str, coords: list) -> None:
        self.weight = weight
        self.name = name
        self.coords = coords


    def go_forward(self, coords: list, step: int = 1) -> None:
        coords[1] += step


    def go_back(self, coords: list, step: int = 1) -> None:
        coords[1] -= step


    def go_right(self, coords: list, step: int = 1) -> None:
        coords[0] += step


    def go_left(self, coords: list, step: int = 1) -> None:
        coords[0] -= step

    def get_info(self) -> dict:
        return {"Robot": {self.name}, "Weight": {self.weight}}


class FlyingRobot(BaseRobot):
    def __init__(self, weight: int, name: str, coords: list) -> None:
        super().__init__(weight, name, coords)
        if coords is None:
            coords = [0, 0, 0]
        elif len(coords) == 2:
            coords.append(0)
        self.coords = coords

    @staticmethod
    def go_up(coords: list, step: int = 1) -> None:
        coords[2] += step

    @staticmethod
    def go_down(coords: list, step: int = 1) -> None:
        coords[2] -= step

class DeliveryDrone(FlyingRobot):
    def __init__(self, name: int, weight: str, max_load_weight: int, coords=None, current_load: Cargo = None) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = None
        if current_load:
            self.hook_load(current_load)


    def hook_load(self, cargo: Cargo) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None










