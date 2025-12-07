
CAD_TOOLS = {
    "Extrude": "Takes a 2D sketch and pulls it into 3D space linearly. This is the most common way to create a 3D body.",
    "Revolve": "Rotates a 2D profile around a central axis (centerline) to create a cylindrical or spherical shape.",
    "Sweep": "Moves a 2D profile along a specified path (curve) to create complex shapes like pipes or handles.",
    "Loft": "Creates a 3D shape by transitioning between two or more different 2D profiles on different planes.",
    "Fillet": "Rounds off the sharp internal or external edges of a part to reduce stress concentrations and improve aesthetics.",
    "Chamfer": "Cuts a straight angled slope (usually 45 degrees) on the edge of a part.",
    "Shell": "Hollows out a solid part, leaving walls of a specified thickness.",
    "Boolean (Combine/Cut)": "Operations that join (Union), subtract (Cut), or find the intersection of two solid bodies."
}

SHORTCUTS = {
    "Fusion 360": {
        "L": "Line tool",
        "R": "2-point Rectangle",
        "C": "Center Diameter Circle",
        "E": "Extrude",
        "Q": "Press Pull (dynamic extrude/offset)",
        "D": "Dimension",
        "S": "Search Toolbox",
        "F": "Fillet"
    },
    "SolidWorks": {
        "L": "Line",
        "D": "Smart Dimension",
        "Ctrl+8": "Normal To (view flat on face)",
        "S": "Shortcut Bar",
        "F": "Zoom to Fit",
        "Enter": "Repeat Last Command"
    },
    "Onshape": {
        "Shift+S": "Sketch",
        "Shift+E": "Extrude",
        "N": "View Normal To",
        "P": "Hide/Show Planes",
        "L": "Line",
        "D": "Dimension"
    },
    "Blender (CAD-like)": {
        "G": "Grab (Move)",
        "R": "Rotate",
        "S": "Scale",
        "E": "Extrude",
        "Tab": "Toggle Edit/Object Mode",
        "Numpad 1/3/7": "Front/Right/Top View"
    }
}

def get_tool_explanation(tool_name):
    """Returns the explanation for a specific CAD tool."""
    return CAD_TOOLS.get(tool_name, "Tool definition not found.")

def list_tools():
    """Returns a list of available CAD tool definitions."""
    return list(CAD_TOOLS.keys())

def get_shortcuts_for_software(software_name):
    """Returns the shortcut dictionary for a specific software."""
    return SHORTCUTS.get(software_name, {})

def list_software():
    """Returns a list of software with available shortcuts."""
    return list(SHORTCUTS.keys())
