class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f"{self._nome} | {self.categoria}"
    
    @classmethod
    def listar_restaurantes(cls):
        print(f"{"Nome do restaurante:".ljust(25)} | {"Categoria:".ljust(25)} | {"Status:"}")
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}")

    @property
    def ativo(self):
        return "Verdadeiro" if self._ativo else "Falso"
    
    def alternar_estado(self):
        self._ativo = not self._ativo
    

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante("Pizza Express", "Italiana")

Restaurante.listar_restaurantes()
