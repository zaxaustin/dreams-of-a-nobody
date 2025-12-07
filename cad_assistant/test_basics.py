
import unittest
from cad_assistant import materials, tips, calculator, cad_basics

class TestCadAssistant(unittest.TestCase):
    def test_materials_list(self):
        mats = materials.list_materials()
        self.assertIn("PLA", mats)
        self.assertIn("ABS", mats)
        self.assertIn("NYLON", mats)

    def test_tips_categories(self):
        cats = tips.get_all_categories()
        self.assertIn("General", cats)

    def test_calculator_cost(self):
        cost = calculator.calculate_cost(100, 20)
        self.assertAlmostEqual(cost, 2.0)

    def test_cad_basics_tools(self):
        tools = cad_basics.list_tools()
        self.assertIn("Extrude", tools)
        self.assertIn("Revolve", tools)

        expl = cad_basics.get_tool_explanation("Extrude")
        self.assertTrue(len(expl) > 10)

    def test_cad_basics_shortcuts(self):
        softwares = cad_basics.list_software()
        self.assertIn("Fusion 360", softwares)

        sc = cad_basics.get_shortcuts_for_software("Fusion 360")
        self.assertEqual(sc.get("E"), "Extrude")

if __name__ == '__main__':
    unittest.main()
