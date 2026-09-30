from game.data.buckets import BUCKETS
from game.inventory import *
from ui.style import *


def get_bucket_row_length(state):
    fish_inventory = state.inventory["fish"]

    if not fish_inventory:
        return 40

    return max(
        5
        + 30
        + 15
        + len(f"{fish['money']:,} (G)")
        for fish in fish_inventory
    )

def display_bucket_capacity(state):
    bucket_id = state.equipped["bucket"]
    bucket = BUCKETS[bucket_id]

    bucket_name = bucket["label"]
    capacity = bucket["capacity"]
    fish_count = len(state.inventory["fish"])

    capacity_ratio = f"{fish_count}/{capacity}"

    if is_bucket_full(state):
        return f"{bucket_name}: {RED}{capacity_ratio} (FULL){RESET}"

    return f"{bucket_name}: {capacity_ratio}"

def display_sellbucket_result(state):
    total_gold = sell_all_fish(state)

    if total_gold == 0:
        print("There are no fish to sell!")
        return

    print(f"You sold all your fish for {YELLOW}{total_gold:,} (G)!{RESET}")