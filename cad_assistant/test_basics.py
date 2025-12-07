
import unittest
from cad_assistant import materials
from cad_assistant import tips
from cad_assistant import calculator

class TestCadAssistant(unittest.TestCase):
    def test_materials_list(self):
        mats = materials.list_materials()
        self.assertIn("PLA", mats)
        self.assertIn("ABS", mats)
        self.assertIn("NYLON", mats)
        self.assertIn("ASA", mats)

    def test_material_info(self):
        info = materials.get_material_info("PLA")
        self.assertIsNotNone(info)
        self.assertEqual(info["description"], "Polylactic Acid. Easy to print, biodegradable, rigid but brittle.")

        info_asa = materials.get_material_info("ASA")
        self.assertIsNotNone(info_asa)
        self.assertTrue("UV resistant" in info_asa["pros"][0])

    def test_tips_categories(self):
        cats = tips.get_all_categories()
        self.assertIn("General", cats)

    def test_random_tip(self):
        tip = tips.get_random_tip()
        self.assertIsInstance(tip, str)

    def test_calculator_cost(self):
        # 100g at $20/kg = $2
        cost = calculator.calculate_cost(100, 20)
        self.assertAlmostEqual(cost, 2.0)

        # 0 weight = 0 cost
        cost = calculator.calculate_cost(0, 50)
        self.assertEqual(cost, 0.0)

    def test_calculator_total(self):
        # Material: 100g @ $20/kg = $2.00
        # Energy: 100W for 10 hours = 1000Wh = 1 kWh
        # Energy Cost: 1 kWh @ $0.15 = $0.15
        # Total: $2.15

        cost = calculator.calculate_total_cost(
            weight_g=100,
            cost_per_kg=20,
            print_time_hours=10,
            power_watts=100,
            electricity_cost_kwh=0.15
        )
        self.assertAlmostEqual(cost, 2.15)

if __name__ == '__main__':
    unittest.main()
