from models import (
    ModelEnum,
    PackSizeEnum,
    CoffeeFlavorEnum,
)
from sku_db import sku


async def simulate_machine_search(
    product_type: str = None,
    water_line_compatible: bool = None,
    model: ModelEnum = None,
):
    result = []
    for product in sku:
        match_filters = all(
            [
                not product_type or product.product_type == product_type,
                not water_line_compatible
                or getattr(product, "water_line_compatible", None)
                == water_line_compatible,
                not model or getattr(product, "model", None) == model,
            ]
        )
        if match_filters:
            result.append(product)
    return result


async def simulate_pod_search(
    product_type: str = None,
    pack_size: PackSizeEnum = None,
    coffee_flavor: CoffeeFlavorEnum = None,
):
    result = []
    for product in sku:
        match_filters = all(
            [
                not product_type or product.product_type == product_type,
                not pack_size or getattr(product, "pack_size", None) == pack_size,
                not coffee_flavor
                or getattr(product, "coffee_flavor", None) == coffee_flavor,
            ]
        )
        if match_filters:
            result.append(product)

    return result
