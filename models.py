from pydantic import BaseModel
from enum import Enum
from pydantic import BaseModel


class CoffeeMachineEnum(str, Enum):
    COFFEE_MACHINE_LARGE = "COFFEE_MACHINE_LARGE"
    COFFEE_MACHINE_SMALL = "COFFEE_MACHINE_SMALL"
    ESPRESSO_MACHINE = "ESPRESSO_MACHINE"


class CoffeePodEnum(str, Enum):
    COFFEE_POD_LARGE = "COFFEE_POD_LARGE"
    COFFEE_POD_SMALL = "COFFEE_POD_SMALL"
    ESPRESSO_POD = "ESPRESSO_POD"


class CoffeeFlavorEnum(str, Enum):
    COFFEE_FLAVOR_VANILLA = "COFFEE_FLAVOR_VANILLA"
    COFFEE_FLAVOR_CARAMEL = "COFFEE_FLAVOR_CARAMEL"
    COFFEE_FLAVOR_PSL = "COFFEE_FLAVOR_PSL"
    COFFEE_FLAVOR_MOCHA = "COFFEE_FLAVOR_MOCHA"
    COFFEE_FLAVOR_HAZELNUT = "COFFEE_FLAVOR_HAZELNUT"


class ModelEnum(str, Enum):
    BASE_MODEL = "BASE_MODEL"
    PREMIUM_MODEL = "PREMIUM_MODEL"
    DELUX_MODEL = "DELUX_MODEL"


class PackSizeEnum(str, Enum):
    DOZEN_1 = "12"
    DOZEN_3 = "36"
    DOZEN_5 = "60"
    DOZEN_7 = "84"


class Product(BaseModel):
    id: str
    product_type: str


class CoffeeMachine(Product):
    product_type: CoffeeMachineEnum
    water_line_compatible: bool = False
    model: ModelEnum


class CoffeePod(Product):
    product_type: CoffeePodEnum
    coffee_flavor: CoffeeFlavorEnum
    pack_size: PackSizeEnum
