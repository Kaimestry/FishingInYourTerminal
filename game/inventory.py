#game/inventory.py

from game.data.buckets import BUCKETS


def add_caught_fish(state, fish):
    # *Add caught fish into the inventory*
    fish_item = fish.copy()

    fish_item.pop("caught", None)
    fish_item["origin"] = "caught"

    state.inventory["fish"].append(fish_item)

def is_bucket_full(state):
    bucket_id = state.equipped["bucket"]
    bucket = BUCKETS[bucket_id]

    capacity = bucket["capacity"]
    fish_count = len(state.inventory["fish"])

    return fish_count >= capacity