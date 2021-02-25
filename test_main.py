from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health_check")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_all_large_machines():
    response = client.get("/coffee_machine?product_type=COFFEE_MACHINE_LARGE")
    assert response.status_code == 200
    print(response.json())
    assert response.json() == [
        {
            "id": "CM101",
            "product_type": "COFFEE_MACHINE_LARGE",
            "water_line_compatible": False,
            "model": "BASE_MODEL",
        },
        {
            "id": "CM102",
            "product_type": "COFFEE_MACHINE_LARGE",
            "water_line_compatible": True,
            "model": "PREMIUM_MODEL",
        },
        {
            "id": "CM103",
            "product_type": "COFFEE_MACHINE_LARGE",
            "water_line_compatible": True,
            "model": "DELUX_MODEL",
        },
    ]


def test_all_large_pods():
    response = client.get("/coffee_pod?product_type=COFFEE_POD_LARGE")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": "CP101",
            "product_type": "COFFEE_POD_LARGE",
            "coffee_flavor": "COFFEE_FLAVOR_VANILLA",
            "pack_size": "12",
        },
        {
            "id": "CP103",
            "product_type": "COFFEE_POD_LARGE",
            "coffee_flavor": "COFFEE_FLAVOR_VANILLA",
            "pack_size": "36",
        },
        {
            "id": "CP111",
            "product_type": "COFFEE_POD_LARGE",
            "coffee_flavor": "COFFEE_FLAVOR_CARAMEL",
            "pack_size": "12",
        },
        {
            "id": "CP113",
            "product_type": "COFFEE_POD_LARGE",
            "coffee_flavor": "COFFEE_FLAVOR_CARAMEL",
            "pack_size": "36",
        },
        {
            "id": "CP121",
            "product_type": "COFFEE_POD_LARGE",
            "coffee_flavor": "COFFEE_FLAVOR_PSL",
            "pack_size": "12",
        },
        {
            "id": "CP123",
            "product_type": "COFFEE_POD_LARGE",
            "coffee_flavor": "COFFEE_FLAVOR_PSL",
            "pack_size": "36",
        },
        {
            "id": "CP131",
            "product_type": "COFFEE_POD_LARGE",
            "coffee_flavor": "COFFEE_FLAVOR_MOCHA",
            "pack_size": "12",
        },
        {
            "id": "CP133",
            "product_type": "COFFEE_POD_LARGE",
            "coffee_flavor": "COFFEE_FLAVOR_MOCHA",
            "pack_size": "36",
        },
        {
            "id": "CP141",
            "product_type": "COFFEE_POD_LARGE",
            "coffee_flavor": "COFFEE_FLAVOR_HAZELNUT",
            "pack_size": "12",
        },
        {
            "id": "CP143",
            "product_type": "COFFEE_POD_LARGE",
            "coffee_flavor": "COFFEE_FLAVOR_HAZELNUT",
            "pack_size": "36",
        },
    ]


def test_all_esspresso_vanilla_pods():
    response = client.get(
        "/coffee_pod?product_type=ESPRESSO_POD&coffee_flavor=COFFEE_FLAVOR_VANILLA"
    )
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": "EP003",
            "product_type": "ESPRESSO_POD",
            "coffee_flavor": "COFFEE_FLAVOR_VANILLA",
            "pack_size": "36",
        },
        {
            "id": "EP005",
            "product_type": "ESPRESSO_POD",
            "coffee_flavor": "COFFEE_FLAVOR_VANILLA",
            "pack_size": "60",
        },
        {
            "id": "EP007",
            "product_type": "ESPRESSO_POD",
            "coffee_flavor": "COFFEE_FLAVOR_VANILLA",
            "pack_size": "84",
        },
    ]


def test_all_espresso_machines():
    response = client.get("/coffee_machine?product_type=ESPRESSO_POD")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": "EP003",
            "product_type": "ESPRESSO_POD",
            "coffee_flavor": "COFFEE_FLAVOR_VANILLA",
            "pack_size": "36",
        },
        {
            "id": "EP005",
            "product_type": "ESPRESSO_POD",
            "coffee_flavor": "COFFEE_FLAVOR_VANILLA",
            "pack_size": "60",
        },
        {
            "id": "EP007",
            "product_type": "ESPRESSO_POD",
            "coffee_flavor": "COFFEE_FLAVOR_VANILLA",
            "pack_size": "84",
        },
        {
            "id": "EP013",
            "product_type": "ESPRESSO_POD",
            "coffee_flavor": "COFFEE_FLAVOR_CARAMEL",
            "pack_size": "36",
        },
        {
            "id": "EP015",
            "product_type": "ESPRESSO_POD",
            "coffee_flavor": "COFFEE_FLAVOR_CARAMEL",
            "pack_size": "60",
        },
        {
            "id": "EP017",
            "product_type": "ESPRESSO_POD",
            "coffee_flavor": "COFFEE_FLAVOR_CARAMEL",
            "pack_size": "84",
        },
    ]


def test_all_small_pods():
    response = client.get("/coffee_pod?product_type=COFFEE_POD_SMALL")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": "CP001",
            "product_type": "COFFEE_POD_SMALL",
            "coffee_flavor": "COFFEE_FLAVOR_VANILLA",
            "pack_size": "12",
        },
        {
            "id": "CP003",
            "product_type": "COFFEE_POD_SMALL",
            "coffee_flavor": "COFFEE_FLAVOR_VANILLA",
            "pack_size": "36",
        },
        {
            "id": "CP011",
            "product_type": "COFFEE_POD_SMALL",
            "coffee_flavor": "COFFEE_FLAVOR_CARAMEL",
            "pack_size": "12",
        },
        {
            "id": "CP013",
            "product_type": "COFFEE_POD_SMALL",
            "coffee_flavor": "COFFEE_FLAVOR_CARAMEL",
            "pack_size": "36",
        },
        {
            "id": "CP021",
            "product_type": "COFFEE_POD_SMALL",
            "coffee_flavor": "COFFEE_FLAVOR_PSL",
            "pack_size": "12",
        },
        {
            "id": "CP023",
            "product_type": "COFFEE_POD_SMALL",
            "coffee_flavor": "COFFEE_FLAVOR_PSL",
            "pack_size": "36",
        },
        {
            "id": "CP031",
            "product_type": "COFFEE_POD_SMALL",
            "coffee_flavor": "COFFEE_FLAVOR_MOCHA",
            "pack_size": "12",
        },
        {
            "id": "CP033",
            "product_type": "COFFEE_POD_SMALL",
            "coffee_flavor": "COFFEE_FLAVOR_MOCHA",
            "pack_size": "36",
        },
        {
            "id": "CP041",
            "product_type": "COFFEE_POD_SMALL",
            "coffee_flavor": "COFFEE_FLAVOR_HAZELNUT",
            "pack_size": "12",
        },
        {
            "id": "CP043",
            "product_type": "COFFEE_POD_SMALL",
            "coffee_flavor": "COFFEE_FLAVOR_HAZELNUT",
            "pack_size": "36",
        },
    ]


def test_all_pods_sold_in_7_dozen_packs():
    response = client.get("/coffee_pod?pack_size=84")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": "EP007",
            "product_type": "ESPRESSO_POD",
            "coffee_flavor": "COFFEE_FLAVOR_VANILLA",
            "pack_size": "84",
        },
        {
            "id": "EP017",
            "product_type": "ESPRESSO_POD",
            "coffee_flavor": "COFFEE_FLAVOR_CARAMEL",
            "pack_size": "84",
        },
    ]
