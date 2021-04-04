# import the pygame module, so you can use it
import pygame
from pygame.locals import *
import warnings
import random
import numpy as np
import math
from scipy.spatial import Delaunay

import delaunaytriangulation as dt
import graphmodel as gm
import drawer
import ggraph
import utils
import graphdisplay as gd



# define a main function
def main():

	# define a variable to control the main loop
	running = True

	graph = ggraph.gGraph(node_type=ggraph.gNode)
	
	display = gd.GraphDisplay(graph)

	nb_node = 30
	# sparseness = random.randint(nb_node-1, int(nb_node*(nb_node-1)/2.0))
	sparseness = nb_node-1

	collision_on = True

	apply_forces_on = True

	def generate():
		# graph.complete_graph(nb_node)
		# graph.random_connected_graph(nb_node, random.randint(nb_node-1, nb_node*(nb_node-1)/2.0), True)
		# graph.random_connected_graph(nb_node, sparseness, True)
		graph.random_connected_graph(nb_node, sparseness, False)
		# graph.random_tree_graph(nb_node)
		for n in graph.nodes:
			n.info["pos"] = [random.randint(0, display.graph_surface_size[0]), random.randint(0, display.graph_surface_size[1])]
			n.info["radius"] = 12
			# n.info["color"] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
			n.info["color"] = (0, 0, 0)
		graph.setDelaunay()
		print(graph.serialise())
	generate()


	# print(graph.serialise())

	selected = None

	# main loop
	while running:

		t = pygame.time.get_ticks()
		# deltaTime in seconds.
		# deltaTime = (t - getTicksLastFrame) / 1000.0

		# event handling, gets all event from the event queue
		for event in pygame.event.get():
			# only do something if the event is of type QUIT
			if event.type == pygame.QUIT:
				# change the value to False, to exit the main loop
				running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == K_r:
					graph.reset()
					generate()
				if event.key == K_c:
					collision_on = not collision_on
				if event.key == K_SPACE:
					apply_forces_on = not apply_forces_on
				if event.key == K_s:
					for n in graph.nodes:
						n.info["pos"] = [random.randint(0, display.graph_surface_size[0]), random.randint(0, display.graph_surface_size[1])]
				if event.key == K_p:
					for n in graph.nodes:
						n.info["pos"] = [display.graph_surface_size[0]/2, display.graph_surface_size[1]/2]
				if event.key == K_d:
					graph._draw_delaunay = not graph._draw_delaunay


		graph.computeDelaunay()

		if apply_forces_on:
			for n in graph.nodes:
				n.applyForces(collision=collision_on)

		display.main_loop_end()

	 
	 
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
	# call the main function
	main()