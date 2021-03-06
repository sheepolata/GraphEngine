import pygame
import drawer

class GraphDisplay(object):

	def __init__(self, graph, caption="Graph Display", logofile=None, fps=60, screensize=(1280, 720), graph_surface_width_proportion=0.6, info_surface_height_proportion=0.6, mbgc=(128, 128, 128), ibgc=(64, 64, 64), lbgc=(168, 168, 168)):

		self.graph = graph
		self.screensize = screensize

		self.graph_surface_width_proportion = graph_surface_width_proportion
		self.info_surface_height_proportion = info_surface_height_proportion

		self.graph_surface_size = (self.screensize[0]*self.graph_surface_width_proportion, self.screensize[1])
		self.info_surface_size  = (self.screensize[0]*(1.0-self.graph_surface_width_proportion), self.screensize[1]*self.info_surface_height_proportion)
		self.log_surface_size   = (self.screensize[0]*(1.0-self.graph_surface_width_proportion), self.screensize[1]*(1.0-self.info_surface_height_proportion))

		# initialize the pygame module
		pygame.init()
		# load and set the logo
		if logofile != None:
			logo = pygame.image.load("logo32x32.jpg")
			pygame.display.set_icon(logo)
		pygame.display.set_caption(caption)

		self.clock = pygame.time.Clock()

		self.screen = pygame.display.set_mode(self.screensize)

		self.graph_surface   = pygame.Surface(self.graph_surface_size)
		self.info_surface    = pygame.Surface(self.info_surface_size)
		self.log_surface     = pygame.Surface(self.log_surface_size)

		self.graph_surface_position = (0, 0)
		self.info_surface_position = (self.graph_surface_size[0], 0)
		self.log_surface_position = (self.graph_surface_size[0], self.info_surface_size[1])

		self.mainbg_color    = mbgc
		self.infobg_color    = ibgc
		self.consolebg_color = lbgc
		self.graph_surface.fill(self.mainbg_color)
		self.info_surface.fill(self.infobg_color)
		self.log_surface.fill(self.consolebg_color)

		self.fps = fps

		# Console type
		self.log = None
		self.info_console = None

	def set_log(self, log):
		self.log = log
		self.log_font_size = 12
		self.log_font = pygame.font.SysFont('Sans', self.log_font_size)
		self.log.max = int((self.log_surface_size[1] / self.log_font_size) / 1.2)

	def set_info(self, info_console, force_max=False):
		self.info_console = info_console
		self.info_font_size = 12
		self.info_font = pygame.font.SysFont('Sans', self.info_font_size)
		if not force_max:
			self.info_console.max = int((self.info_surface_size[1] / self.info_font_size) / 1.2)

	def clear_log(self):
		self.log.clear()

	def clear_info_console(self):
		self.info_console.clear()

	def display_log_console(self):
		shift = 0
		for line in self.log.get_lines():
			shift = drawer.draw_text(line, self.log_font, self.log_font_size, self.log_surface, (0,0,0), shift)

	def display_info_console(self):
		shift = 0
		for line in self.info_console.get_lines():
			shift = drawer.draw_text(line, self.info_font, self.info_font_size, self.info_surface, (255,255,255), shift)

	def fill_surfaces(self):
		self.graph_surface.fill(self.mainbg_color)
		self.info_surface.fill(self.infobg_color)
		self.log_surface.fill(self.consolebg_color)

	def blit_surfaces(self):
		self.screen.blit(self.graph_surface, self.graph_surface_position)
		self.screen.blit(self.info_surface, self.info_surface_position)
		self.screen.blit(self.log_surface, self.log_surface_position)

	def pygame_update_and_tick(self):
		pygame.display.update()

		if self.fps > 0:
			self.clock.tick(self.fps)

	def main_loop_logic(self):
		if self.log != None:
			self.display_log_console()
		if self.info_console != None:
			self.display_info_console()

		if self.graph != None:
			self.graph.draw(self.graph_surface)

	def main_loop_end(self):

		self.fill_surfaces()

		self.main_loop_logic()

		self.blit_surfaces()

		self.pygame_update_and_tick()
		