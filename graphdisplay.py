import pygame

class GraphDisplay(object):

	def __init__(self, graph, caption="Graph Display", logofile=None, screensize=(1280, 720), graph_surface_proportion=0.6, mbgc=(128, 128, 128)):

		self.graph = graph
		self.screensize = screensize

		self.graph_surface_proportion = graph_surface_proportion

		self.graph_surface_size = (self.screensize[0]*self.graph_surface_proportion, self.screensize[1])
		self.info_surface_size = (self.screensize[0]*(1.0-self.graph_surface_proportion), self.screensize[1])

		# initialize the pygame module
		pygame.init()
		# load and set the logo
		if logofile != None:
			logo = pygame.image.load("logo32x32.jpg")
			pygame.display.set_icon(logo)
		pygame.display.set_caption(caption)

		self.clock = pygame.time.Clock()

		self.screen = pygame.display.set_mode(self.screensize)

		self.graph_surface = pygame.Surface(self.graph_surface_size)

		self.mainbg_color = mbgc
		self.graph_surface.fill(self.mainbg_color)

		self.fps = 60

	def main_loop_end(self):
		self.graph_surface.fill(self.mainbg_color)

		self.graph.draw(self.graph_surface)

		self.graph_surface.fill(self.mainbg_color)
		self.graph.draw(self.graph_surface)

		self.screen.blit(self.graph_surface, (0, 0))

		pygame.display.update()

		self.clock.tick(self.fps)