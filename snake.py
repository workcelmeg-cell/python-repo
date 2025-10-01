import pygame
import random
import sys

# -----------------------------
# 1. Global Config & Constants
# -----------------------------
NERGUI_KOSHIG = 20  # CELL_SIZE (koshig = cell/square)
NERGUI_URD = 30     # GRID_WIDTH (urd = width)
NERGUI_URGUN = 20   # GRID_HEIGHT (urgun = height)
NERGUI_DELGETSIIN_URD = NERGUI_KOSHIG * NERGUI_URD  # SCREEN_WIDTH
NERGUI_DELGETSIIN_URGUN = NERGUI_KOSHIG * NERGUI_URGUN  # SCREEN_HEIGHT
NERGUI_EHELSEN_KHURD = 8  # FPS_START (khurd = speed)
NERGUI_KHURD_URGED = 0.5  # FPS_GROWTH (urged = growth)

# Colors
TSAGAAN = (255, 255, 255)  # WHITE (tsagaan = white)
KHAR = (0, 0, 0)          # BLACK (khar = black)
NOGOON = (0, 200, 0)      # GREEN (nogoon = green)
KHAR_NOGOON = (0, 150, 0) # DARK_GREEN (khar nogoon = dark green)
ULAAN = (200, 0, 0)       # RED (ulaan = red)
KHUKH = (40, 40, 40)      # GRAY (khukh = gray)

# -----------------------------
# 2. Helper Functions
# -----------------------------
def sanamsargui_koshig(mogoi):
    """Pick a random empty cell (not on the snake)."""
    while True:
        x = random.randint(0, NERGUI_URD - 1)
        y = random.randint(0, NERGUI_URGUN - 1)
        if (x, y) not in mogoi:
            return (x, y)

def koshig_zur(delgets, bairlal, ung):
    """Draw one square on the screen."""
    rect = pygame.Rect(bairlal[0] * NERGUI_KOSHIG, bairlal[1] * NERGUI_KOSHIG, NERGUI_KOSHIG, NERGUI_KOSHIG)
    pygame.draw.rect(delgets, ung, rect)

def toriig_zur(delgets):
    """Draw grid lines (optional, makes board clearer)."""
    for x in range(0, NERGUI_DELGETSIIN_URD, NERGUI_KOSHIG):
        pygame.draw.line(delgets, KHUKH, (x, 0), (x, NERGUI_DELGETSIIN_URGUN))
    for y in range(0, NERGUI_DELGETSIIN_URGUN, NERGUI_KOSHIG):
        pygame.draw.line(delgets, KHUKH, (0, y), (NERGUI_DELGETSIIN_URD, y))

# -----------------------------
# 3. Mogoi Class (Snake)
# -----------------------------
class Mogoi:
    def __init__(self):
        x = NERGUI_URD // 2
        y = NERGUI_URGUN // 2
        self.bie = [(x, y), (x - 1, y), (x - 2, y)]  # body (bie = body)
        self.chiglel = (1, 0)                        # direction (chiglel = direction)
        self.daraagiin_chiglel = (1, 0)              # next_direction (daraagiin = next)

    def khodol(self):
        """Move the snake in the current direction."""
        self.chiglel = self.daraagiin_chiglel
        tolgoi_x, tolgoi_y = self.bie[0]  # head (tolgoi = head)
        dx, dy = self.chiglel
        shine_tolgoi = ((tolgoi_x + dx) % NERGUI_URD, (tolgoi_y + dy) % NERGUI_URGUN)
        return shine_tolgoi

    def urg(self, shine_tolgoi):
        """Add new head (snake grows)."""
        self.bie.insert(0, shine_tolgoi)

    def bagas(self):
        """Remove last part (normal movement)."""
        self.bie.pop()

    def oortoo_morgold(self, shine_tolgoi):
        """Check if snake collided with itself."""
        return shine_tolgoi in self.bie

    def zur(self, delgets):
        """Draw the snake."""
        for i, koshig in enumerate(self.bie):
            ung = KHAR_NOGOON if i == 0 else NOGOON
            koshig_zur(delgets, koshig, ung)

# -----------------------------
# 4. Togloom Class (Game)
# -----------------------------
class Togloom:
    def __init__(self):
        pygame.init()
        self.delgets = pygame.display.set_mode((NERGUI_DELGETSIIN_URD, NERGUI_DELGETSIIN_URGUN))
        pygame.display.set_caption("Mogoi Togloom")  # Snake Game
        self.tsag = pygame.time.Clock()             # clock (tsag = clock/time)
        self.uusgver = pygame.font.SysFont(None, 36)
        self.tom_uusgver = pygame.font.SysFont(None, 72)

        self.mogoi = Mogoi()
        self.khool = sanamsargui_koshig(self.mogoi.bie)  # food (khool = food)
        self.ono = 0                                     # score (ono = score)
        self.khurd = NERGUI_EHELSEN_KHURD               # fps (khurd = speed)
        self.togloom_duusav = False                      # game_over (duusav = finished)

    def shineer_ehel(self):
        """Restart game when player dies."""
        self.mogoi = Mogoi()
        self.khool = sanamsargui_koshig(self.mogoi.bie)
        self.ono = 0
        self.khurd = NERGUI_EHELSEN_KHURD
        self.togloom_duusav = False

    def orolt_av(self):
        """Process player key presses."""
        for uil_ajillagaa in pygame.event.get():  # event (uil_ajillagaa = event)
            if uil_ajillagaa.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if uil_ajillagaa.type == pygame.KEYDOWN:
                if uil_ajillagaa.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if not self.togloom_duusav:
                    if uil_ajillagaa.key in (pygame.K_UP, pygame.K_w) and self.mogoi.chiglel != (0, 1):
                        self.mogoi.daraagiin_chiglel = (0, -1)
                    elif uil_ajillagaa.key in (pygame.K_DOWN, pygame.K_s) and self.mogoi.chiglel != (0, -1):
                        self.mogoi.daraagiin_chiglel = (0, 1)
                    elif uil_ajillagaa.key in (pygame.K_LEFT, pygame.K_a) and self.mogoi.chiglel != (1, 0):
                        self.mogoi.daraagiin_chiglel = (-1, 0)
                    elif uil_ajillagaa.key in (pygame.K_RIGHT, pygame.K_d) and self.mogoi.chiglel != (-1, 0):
                        self.mogoi.daraagiin_chiglel = (1, 0)
                else:
                    self.shineer_ehel()

    def shinechil(self):
        """Game logic: move snake, check collisions, food, score."""
        if not self.togloom_duusav:
            shine_tolgoi = self.mogoi.khodol()

            if self.mogoi.oortoo_morgold(shine_tolgoi):
                self.togloom_duusav = True
            else:
                self.mogoi.urg(shine_tolgoi)

                if shine_tolgoi == self.khool:
                    self.ono += 1
                    self.khurd = NERGUI_EHELSEN_KHURD + int(self.ono * NERGUI_KHURD_URGED)
                    self.khool = sanamsargui_koshig(self.mogoi.bie)
                else:
                    self.mogoi.bagas()

    def zur(self):
        """Draw everything on the screen."""
        self.delgets.fill(KHAR)
        toriig_zur(self.delgets)
        koshig_zur(self.delgets, self.khool, ULAAN)
        self.mogoi.zur(self.delgets)

        ono_garac = self.uusgver.render(f"Ono: {self.ono}", True, TSAGAAN)
        self.delgets.blit(ono_garac, (10, 10))

        if self.togloom_duusav:
            davhar = pygame.Surface((NERGUI_DELGETSIIN_URD, NERGUI_DELGETSIIN_URGUN), pygame.SRCALPHA)
            davhar.fill((0, 0, 0, 150))
            self.delgets.blit(davhar, (0, 0))
            duussan_tekst = self.tom_uusgver.render("Togloom Duusav", True, TSAGAAN)
            self.delgets.blit(duussan_tekst, duussan_tekst.get_rect(center=(NERGUI_DELGETSIIN_URD // 2, NERGUI_DELGETSIIN_URGUN // 2 - 30)))
            zaavar = self.uusgver.render("Dahij ehelkhiin tuld yamarch tovch dar", True, TSAGAAN)
            self.delgets.blit(zaavar, zaavar.get_rect(center=(NERGUI_DELGETSIIN_URD // 2, NERGUI_DELGETSIIN_URGUN // 2 + 30)))

        pygame.display.flip()

    def ajilluul(self):
        """Main game loop."""
        while True:
            self.orolt_av()
            self.shinechil()
            self.zur()
            self.tsag.tick(max(1, self.khurd))

# -----------------------------
# 5. Run the Game
# -----------------------------
if __name__ == "__main__":
    togloom = Togloom()
    togloom.ajilluul()