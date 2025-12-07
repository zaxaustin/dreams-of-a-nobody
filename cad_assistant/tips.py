
TIPS = {
    "General": [
        "Always design with the orientation of printing in mind. This affects strength (layer adhesion) and support requirements.",
        "Fillets reduce stress concentrations, but chamfers are often easier to print, especially on bottom edges.",
        "Consider the layer height. A design with fine vertical details needs a lower layer height."
    ],
    "Wall Thickness": [
        "For a standard 0.4mm nozzle, a wall thickness of 0.8mm (2 perimeters) is a good minimum for structural parts.",
        "1.2mm - 1.6mm (3-4 perimeters) provides significant strength increase.",
        "Avoid thin walls that aren't multiples of your nozzle width to ensure clean slicing."
    ],
    "Holes & Tolerances": [
        "Vertical holes (printed with axis vertical) tend to print slightly undersized due to plastic shrinking inwards. Design them 0.1-0.2mm larger.",
        "Horizontal holes (axis horizontal) may droop at the top. Use a teardrop shape if precision is key without supports.",
        "Clearance for parts: 0.1-0.15mm for a press fit / tight fit.",
        "Clearance for parts: 0.2-0.3mm for a sliding fit / loose fit.",
        "Clearance for parts: >0.4mm for completely free movement."
    ],
    "Overhangs & Bridges": [
        "The 45-degree rule: Angles steeper than 45 degrees from the build plate usually don't need supports.",
        "Bridges (horizontal spans) can be printed without support if the cooling is good and the span isn't too long (e.g., < 20mm).",
        "Use chamfers instead of fillets on the bottom face to avoid overhangs that curl up."
    ]
}

def get_tips_by_category(category):
    """Returns tips for a specific category."""
    return TIPS.get(category, [])

def get_all_categories():
    """Returns a list of tip categories."""
    return list(TIPS.keys())

def get_random_tip():
    """Returns a random tip from any category."""
    import random
    category = random.choice(list(TIPS.keys()))
    tip = random.choice(TIPS[category])
    return f"[{category}] {tip}"
