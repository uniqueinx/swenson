port=$1

# All large machines
curl -s --location --request GET "localhost:$port/coffee_machine?product_type=COFFEE_MACHINE_LARGE" | jq
echo "-----------------"
# All large pods
curl -s --location --request GET "localhost:$port/coffee_pod?product_type=COFFEE_POD_LARGE" | jq
echo "-----------------"
# All espresso vanilla pods
curl -s --location --request GET "localhost:$port/coffee_pod?product_type=ESPRESSO_POD&coffee_flavor=COFFEE_FLAVOR_VANILLA" | jq 
echo "-----------------"
# All espresso machines
curl -s --location --request GET "localhost:$port/coffee_machine?product_type=ESPRESSO_POD" | jq 
echo "-----------------"
# All small pods
curl -s --location --request GET "localhost:$port/coffee_pod?product_type=COFFEE_POD_SMALL" | jq 
echo "-----------------"
# All pods sold in 7 dozen packs
curl -s --location --request GET "localhost:$port/coffee_pod?pack_size=84" | jq 
echo "-----------------"