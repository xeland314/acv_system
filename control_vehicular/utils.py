from enum import Enum

class TipoDeVehiculo(Enum):
    CAMION = "Camión"
    CAMIONETA = "Camioneta"
    AUTOMOVIL = "Automóvil"
    MOTOCICLETA = "Motocicleta"
    BUS = "Bus"
    TRACTOR = "Tractor"

class Combustible(Enum):
    GASOLINA = "Gasolina"
    DIESEL = "Diésel"
    GAS = "Gas"
    ELECTRICO = "Eléctrico"

class CondicionVehicular(Enum):
    NUEVO = "Nuevo"
    USADO = "Usado"

class PosicionLlanta(Enum):
    IZQUIERDA = "Izquierda"
    DERECHA = "Derecha"
    DELANTERA = "Delantera"
    TRASERA = "Trasera"

class TipoLicencia(Enum):
    A = 'A'
    B = 'B'
    F = 'F'
    A1 = 'A1'
    C = 'C'
    C1 = 'C1'
    D = 'D'
    D1 = 'D1'
    E = 'E'
    E1 = 'E1'
