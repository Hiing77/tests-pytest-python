def verifier_temperature(temp):

    if not isinstance(temp, (int,float)):
            return "TYPE_INVALIDE"
    
    elif temp < -50 or temp > 100:
        return "TEMPERATURE_INVALIDE"
    
    elif temp >= 38:
         return "FIEVRE"
    
    else:
         return "NORMALE"

def test_TYPE_INVALIDE():
        assert verifier_temperature("OK") == "TYPE_INVALIDE"

def test_TEMPERATURE_INVALIDE():
        assert verifier_temperature(101) == "TEMPERATURE_INVALIDE"

def test_FIEVRE():
         assert verifier_temperature(38) == "FIEVRE"

def test_NORMALE():
         assert verifier_temperature(12) == "NORMALE" 

