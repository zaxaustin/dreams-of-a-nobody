
MATERIALS = {
    "PLA": {
        "description": "Polylactic Acid. Easy to print, biodegradable, rigid but brittle.",
        "nozzle_temp": "190-220°C",
        "bed_temp": "45-60°C",
        "shrinkage": "Low (~0.2-0.3%)",
        "pros": ["Easy to print", "Good dimensional accuracy", "Wide color variety"],
        "cons": ["Low heat resistance", "Brittle", "Not suitable for outdoors (UV degrades it)"]
    },
    "PETG": {
        "description": "Polyethylene Terephthalate Glycol. Good balance of strength and ease of use.",
        "nozzle_temp": "230-250°C",
        "bed_temp": "70-90°C",
        "shrinkage": "Low (< 0.5%)",
        "pros": ["Stronger than PLA", "More flexible", "Heat resistant", "Water resistant"],
        "cons": ["Stringing", "Can stick too well to bed"]
    },
    "ABS": {
        "description": "Acrylonitrile Butadiene Styrene. Strong, durable, heat resistant.",
        "nozzle_temp": "220-250°C",
        "bed_temp": "95-110°C",
        "shrinkage": "High (0.4-0.7%)",
        "pros": ["Very strong", "Heat resistant", "Can be smoothed with acetone"],
        "cons": ["Warps easily", "Produces fumes when printing", "Needs enclosure"]
    },
    "TPU": {
        "description": "Thermoplastic Polyurethane. Flexible and rubber-like.",
        "nozzle_temp": "210-230°C",
        "bed_temp": "30-60°C",
        "shrinkage": "Low",
        "pros": ["Flexible", "Abrasion resistant", "Impact resistant"],
        "cons": ["Hard to print", "Slow print speeds", "Stringing"]
    },
    "NYLON": {
        "description": "Polyamide. Extremely strong, durable, and impact resistant.",
        "nozzle_temp": "240-260°C",
        "bed_temp": "70-100°C",
        "shrinkage": "High",
        "pros": ["High strength", "High impact resistance", "Low friction"],
        "cons": ["Absorbs moisture (hygroscopic)", "Warps easily", "Hard to print"]
    },
    "ASA": {
        "description": "Acrylonitrile Styrene Acrylate. Similar to ABS but UV stable.",
        "nozzle_temp": "230-250°C",
        "bed_temp": "90-110°C",
        "shrinkage": "Moderate",
        "pros": ["UV resistant (outdoor use)", "Strong like ABS", "Less warping than ABS"],
        "cons": ["Needs enclosure (fumes)", "Higher bed temp required"]
    },
    "PC": {
        "description": "Polycarbonate. One of the strongest engineering filaments.",
        "nozzle_temp": "250-300°C",
        "bed_temp": "100-115°C",
        "shrinkage": "High",
        "pros": ["Extremely heat resistant", "Very strong", "Impact resistant"],
        "cons": ["Very high print temps", "Warps significantly", "Expensive"]
    }
}

def get_material_info(material_name):
    """Returns information about a specific material."""
    return MATERIALS.get(material_name.upper())

def list_materials():
    """Returns a list of available materials."""
    return list(MATERIALS.keys())
