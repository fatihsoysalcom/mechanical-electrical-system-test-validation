import unittest

# --- Mock System Components ---

class MechanicalComponent:
    def __init__(self, pressure_limit, temperature_limit):
        self.pressure_limit = pressure_limit
        self.temperature_limit = temperature_limit
        self.current_pressure = 0
        self.current_temperature = 0

    def set_pressure(self, pressure):
        if pressure > self.pressure_limit:
            raise ValueError("Pressure exceeds limit")
        self.current_pressure = pressure

    def set_temperature(self, temperature):
        if temperature > self.temperature_limit:
            raise ValueError("Temperature exceeds limit")
        self.current_temperature = temperature

    def get_status(self):
        return {
            "pressure": self.current_pressure,
            "temperature": self.current_temperature
        }

class ElectricalComponent:
    def __init__(self, voltage_limit, current_limit):
        self.voltage_limit = voltage_limit
        self.current_limit = current_limit
        self.current_voltage = 0
        self.current_current = 0

    def set_voltage(self, voltage):
        if voltage > self.voltage_limit:
            raise ValueError("Voltage exceeds limit")
        self.current_voltage = voltage

    def set_current(self, current):
        if current > self.current_limit:
            raise ValueError("Current exceeds limit")
        self.current_current = current

    def get_status(self):
        return {
            "voltage": self.current_voltage,
            "current": self.current_current
        }

# --- System Integration and Testing ---

class IntegratedSystem:
    def __init__(self, mech_comp, elec_comp):
        self.mech = mech_comp
        self.elec = elec_comp

    def run_scenario(self, pressure, temperature, voltage, current):
        # Test: Mechanical component under load
        self.mech.set_pressure(pressure)
        self.mech.set_temperature(temperature)

        # Test: Electrical component under load
        self.elec.set_voltage(voltage)
        self.elec.set_current(current)

        # Validation: Check if system operates within defined parameters
        # In a real system, this would involve more complex checks and interdependencies.
        print("System scenario executed successfully.")
        return True

    def get_system_status(self):
        return {
            "mechanical": self.mech.get_status(),
            "electrical": self.elec.get_status()
        }

# --- Unit Tests for Validation ---

class TestSystemValidation(unittest.TestCase):

    def setUp(self):
        # Setup for each test: Create components with defined limits
        self.mech_comp = MechanicalComponent(pressure_limit=100, temperature_limit=80)
        self.elec_comp = ElectricalComponent(voltage_limit=240, current_limit=10)
        self.system = IntegratedSystem(self.mech_comp, self.elec_comp)

    def test_normal_operation(self):
        # Test case 1: Expected normal operating conditions
        self.assertTrue(self.system.run_scenario(pressure=50, temperature=30, voltage=120, current=5))
        status = self.system.get_system_status()
        self.assertEqual(status["mechanical"]["pressure"], 50)
        self.assertEqual(status["electrical"]["voltage"], 120)

    def test_pressure_overload(self):
        # Test case 2: Validate error handling for mechanical pressure overload
        with self.assertRaises(ValueError):
            self.system.run_scenario(pressure=150, temperature=30, voltage=120, current=5)

    def test_temperature_overload(self):
        # Test case 3: Validate error handling for mechanical temperature overload
        with self.assertRaises(ValueError):
            self.system.run_scenario(pressure=50, temperature=90, voltage=120, current=5)

    def test_voltage_overload(self):
        # Test case 4: Validate error handling for electrical voltage overload
        with self.assertRaises(ValueError):
            self.system.run_scenario(pressure=50, temperature=30, voltage=300, current=5)

    def test_current_overload(self):
        # Test case 5: Validate error handling for electrical current overload
        with self.assertRaises(ValueError):
            self.system.run_scenario(pressure=50, temperature=30, voltage=120, current=15)

if __name__ == '__main__':
    print("--- Running System Tests ---")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    print("--- System Tests Completed ---")
