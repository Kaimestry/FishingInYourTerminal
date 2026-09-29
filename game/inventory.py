#game/inventory.py

def add_caught_fish(state, fish):
    # *Add caught fish into the inventory*
    fish_item = fish.copy()

    fish_item.pop("caught", None)
    fish_item["origin"] = "caught"

    state.inventory["fish"].append(fish_item)

