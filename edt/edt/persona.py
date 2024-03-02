class Persona:
    def __init__(self,nombre:str,peso:int,estatura:float) -> None:
        self.nombre = nombre
        self.peso = peso
        self.estatura = estatura
    def __repr__(self) -> str:
        return f"({self.nombre},{self.peso},{self.estatura})"

    def __eq__(self, __value: object) -> bool:
        return isinstance(__value,Persona) and self.nombre == __value.nombre and self.peso == __value.peso and self.estatura == __value.estatura

    def __hash__(self) -> int:
        return hash((self.nombre,self.peso,self.estatura))
