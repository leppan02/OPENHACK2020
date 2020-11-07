def get_weapon(id): 
    mp = {
        "1": "Aircraft",
        "2": "Artillery",
        "3": "Armoured vehicles",
        "4": "Engines", 
        "5": "Sensors",
        "6": "Missiles",
        "7": "Ships",
        "11": "Other",
        "12": "Naval weapons",
        "13": "Satellites",
        "14": "Air defence systems"
    }
    return mp[str(id)]