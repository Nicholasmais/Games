import pygame
import sys

# Cores
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)
# Tamanho da janela
WIDTH = 800
HEIGHT = 400
HAS_COLIDED_YET = False

# Classe para representar um objeto em movimento
class Objeto:
    def __init__(self, massa, velocidade, cor, pos):
        self.massa = massa
        self.velocidade = velocidade
        self.cor = cor
        tamanho = 25*massa + 25
        self.rect = pygame.Rect(0, 0, tamanho, tamanho)
        self.rect.center = (pos + tamanho/2, HEIGHT // 2)
    
    def quantidade_movimento(self):
        return self.massa*self.velocidade

    def update(self):
        self.rect.x += self.velocidade

         # Verifica a colisão com as paredes
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.velocidade *= -1
            self.rect.x += self.velocidade

    def draw(self, screen):
        pygame.draw.rect(screen, self.cor, self.rect)

# Função para verificar a colisão entre dois objetos
def verificar_colisao(objeto1, objeto2):
    global HAS_COLIDED_YET
    if objeto1.rect.colliderect(objeto2.rect) and not HAS_COLIDED_YET:
        HAS_COLIDED_YET = True
        # Calcula a nova velocidade do objeto 1 usando a conservação da quantidade de movimento
        v1_final = (((objeto1.massa - objeto2.massa)/(objeto1.massa + objeto2.massa)) * objeto1.velocidade + 2 * objeto2.massa * objeto2.velocidade) / (objeto1.massa + objeto2.massa)
        
        # Calcula a nova velocidade do objeto 2 usando a conservação da quantidade de movimento
        v2_final = 2*objeto1.massa*objeto1.velocidade/(objeto1.massa + objeto2.massa) + (objeto2.massa - objeto1.massa)/(objeto1.massa + objeto2.massa)*objeto2.velocidade
        
        # Define as novas velocidades
        objeto1.velocidade = v1_final
        objeto2.velocidade = v2_final
        
        objeto1.update()
        objeto2.update()
    if HAS_COLIDED_YET:
        HAS_COLIDED_YET = False

# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Criação dos objetos
objeto1 = Objeto(1, 0, BLUE,  WIDTH // 6)
objeto2 = Objeto(2, -5, RED, WIDTH // 3)

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualiza a posição dos objetos
    objeto1.update()
    objeto2.update()

    # Verifica a colisão entre os objetos
    verificar_colisao(objeto1, objeto2)

    # Limpa a tela
    screen.fill(BLACK)

    # Desenha os objetos na tela
    objeto1.draw(screen)
    objeto2.draw(screen)

    # Atualiza a tela
    pygame.display.flip()
    clock.tick(60)
