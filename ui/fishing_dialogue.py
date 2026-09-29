import random
import time

from game.data.dialogues import FISH_WAITING_DIALOGUES
def fishing_dialogue(state, debug):
    if state.debug_mode and debug.skip_dialogue:
        return

    total_wait = random.uniform(1, 4)
    dialogue_interval = 1.6

    dialogue_count = int(total_wait / dialogue_interval)

    for _ in range(dialogue_count):
        # Random dialogue
        print(random.choice(FISH_WAITING_DIALOGUES))

        # Filler until the next dialogue
        filler_time = dialogue_interval
        filler_count = int(filler_time / 0.5)

        for _ in range(filler_count):
            print(".")
            time.sleep(1)

    # Any remaining time before the fish bites
    remaining_time = total_wait - (dialogue_count * dialogue_interval)

    if remaining_time > 0:
        filler_count = int(remaining_time / 0.5)

        for _ in range(filler_count):
            print(".")
            time.sleep(1)