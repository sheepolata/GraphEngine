import pygame

class GraphDisplay(object):

	def __init__(self, graph, caption="Graph Display", logofile=None, screensize=(1280, 720), graph_surface_width_proportion=0.6, info_surface_height_proportion=0.6, mbgc=(128, 128, 128), ibgc=(64, 64, 64), cbgc=(168, 168, 168)):

		self.graph = graph
		self.screensize = screensize

		self.graph_surface_width_proportion = graph_surface_width_proportion
		self.info_surface_height_proportion = info_surface_height_proportion

		self.graph_surface_size   = (self.screensize[0]*self.graph_surface_width_proportion, self.screensize[1])
		self.info_surface_size    = (self.screensize[0]*(1.0-self.graph_surface_width_proportion), self.screensize[1]*self.info_surface_height_proportion)
		self.console_surface_size = (self.screensize[0]*(1.0-self.graph_surface_width_proportion), self.screensize[1]*(1.0-self.info_surface_height_proportion))

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
		self.console_surface = pygame.Surface(self.console_surface_size)

		self.mainbg_color    = mbgc
		self.infobg_color    = ibgc
		self.consolebg_color = cbgc
		self.graph_surface.fill(self.mainbg_color)
		self.info_surface.fill(self.infobg_color)
		self.console_surface.fill(self.consolebg_color)

		self.main_surface_position = (0, 0)
		self.info_surface_position = (self.graph_surface_size[0], 0)
		self.console_surface_position = (self.graph_surface_size[0], self.info_surface_size[1])

		self.fps = 60

		self.console = None

	def set_console(self, console):
		self.console = console

	def main_loop_end(self):
		self.graph_surface.fill(self.mainbg_color)
		self.info_surface.fill(self.infobg_color)
		self.console_surface.fill(self.consolebg_color)

		self.graph.draw(self.graph_surface)

		self.screen.blit(self.graph_surface, self.main_surface_position)
		self.screen.blit(self.info_surface, self.info_surface_position)
		self.screen.blit(self.console_surface, self.console_surface_position)

		pygame.display.update()

		self.clock.tick(self.fps)