from Sistema.TorreHanoi import TorreHanoi

class Juego:
    def __init__(self, n):
        self.hanoi = TorreHanoi(n)

    def jugar(self):
        """Controla el flujo del juego."""
        # Mostrar estado inicial
        self.hanoi.mostrar_torres()

        while True:
            try:
                origen = int(input("Selecciona la torre de origen (1, 2, 3): ")) - 1
                destino = int(input("Selecciona la torre de destino (1, 2, 3): ")) - 1

                if origen < 0 or origen > 2 or destino < 0 or destino > 2:
                    print("Movimiento inválido: selecciona torres entre 1 y 3.")
                    continue

                self.hanoi.mover_disco(origen, destino)
                self.hanoi.mostrar_torres()

            except ValueError as e:
                print(e)