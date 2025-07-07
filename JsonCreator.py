import json
import os

armor_items = [
    "copper_chestplate",
    "copper_leggings",
    "copper_boots",
    "waxed_copper_helmet",
    "waxed_copper_chestplate",
    "waxed_copper_leggings",
    "waxed_copper_boots"
]

trim_materials = [
    ("quartz", 0.1),
    ("iron", 0.2),
    ("netherite", 0.3),
    ("redstone", 0.4),
    ("copper", 0.5),
    ("gold", 0.6),
    ("emerald", 0.7),
    ("diamond", 0.8),
    ("lapis", 0.9),
    ("amethyst", 1.0)
]

dir_path = "assets/copperequipment/models/item/"
os.makedirs(dir_path, exist_ok=True)

for armor_item in armor_items:
    armor_type = armor_item.split("_")[-1]
    base_file_name = f"{armor_item}.json"
    base_file_path = os.path.join(dir_path, base_file_name)
    overrides = [
        {
            "model": f"copperequipment:item/{armor_item}_{material}_trim",
            "predicate": {"trim_type": trim_type}
        } for material, trim_type in trim_materials
    ]
    base_json = {
        "parent": "minecraft:item/generated",
        "overrides": overrides,
        "textures": {"layer0": f"copperequipment:item/{armor_item}"}
    }
    with open(base_file_path, "w") as f:
        json.dump(base_json, f, indent=4)
    for material, _ in trim_materials:
        trim_file_name = f"{armor_item}_{material}_trim.json"
        trim_file_path = os.path.join(dir_path, trim_file_name)
        trim_json = {
            "parent": "minecraft:item/generated",
            "textures": {
                "layer0": f"copperequipment:item/{armor_item}",
                "layer1": f"minecraft:trims/items/{armor_type}_trim_{material}"
            }
        }
        with open(trim_file_path, "w") as f:
            json.dump(trim_json, f, indent=4)
