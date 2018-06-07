def servico(self, vel=(4, 0)):
    # Posiciona a bola no centro da tela
    self.bola.center = self.center

    # Seta a velocidade da bola
    self.bola.velocidade = vel
