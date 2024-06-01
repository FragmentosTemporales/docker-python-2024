import os


class Welcome:
    """Welcome user"""
    def __init__(self):

        self.first_name = os.environ.get('FIRST_NAME')
        self.last_name = os.environ.get('LAST_NAME')

        precio = 50
        max_resultado = 0

        while precio <= 200:
            resultado = 1000 * precio - 5 * (precio * precio)
            if resultado > max_resultado:
                max_resultado = resultado
                precio_final = precio
            precio += 1

        print(f'Bienvenido/a {self.first_name} {self.last_name}')
        print(f"Valor final de precio: {precio_final}")
        print(f"Valor final de resultado: {max_resultado}")
