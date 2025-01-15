def fight_soldiers(soldier_one, soldier_two):
    soldier_one_dps = soldier_one["damage"] * soldier_one["attacks_per_second"]
    soldier_two_dps = soldier_two["damage"] * soldier_two["attacks_per_second"]

    if soldier_one_dps > soldier_two_dps:
        return "soldier 1 wins"
    elif soldier_two_dps > soldier_one_dps:
        return "soldier 2 wins"
    else:
        return "both soldiers die"

get_soldier_