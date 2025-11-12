import re 

from hotel.victor_manuel.model.objetos_m import InventarioModel

SUS_KEY = [
    r"\bSELECT\b",
    r"\bHAVING\b",
    r"\bSLEEP\b",
    r"\bINSERT\s+INTO\b",
    r"\bRENAME\b",
    r"\bALTER\b",
    r"\bBAND\b"
]

patron = re.compile("|".join(SUS_KEY), re.IGNORECASE)

class InventarioController:
    def __init__(self, modelo: InventarioModel):
        self.modelo = modelo