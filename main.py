from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from models import PackSizeEnum, CoffeeFlavorEnum, ModelEnum
from service import simulate_pod_search, simulate_machine_search


app = FastAPI(default_response_class=ORJSONResponse)


@app.get("/coffee_machine")
async def filter_coffee_machine(
    product_type: str = None,
    water_line_compatible: bool = None,
    model: ModelEnum = None,
):
    res = await simulate_machine_search(
        product_type=product_type,
        water_line_compatible=water_line_compatible,
        model=model,
    )
    return res


@app.get("/coffee_pod")
async def filter_coffee_pods(
    product_type: str = None,
    pack_size: PackSizeEnum = None,
    coffee_flavor: CoffeeFlavorEnum = None,
):
    res = await simulate_pod_search(
        product_type=product_type,
        pack_size=pack_size,
        coffee_flavor=coffee_flavor,
    )
    return res


@app.get("/health_check")
async def health_check():
    return {"status": "healthy"}
