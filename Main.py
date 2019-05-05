import pygame
import pygame.camera
import os

import io
import os

class GoogleVisionApi:
	def localize_objects(self,path):
		"""Localize objects in the local image.

		Args:
		path: The path to the local file.
		"""
		from google.cloud import vision
		
		client = vision.ImageAnnotatorClient()

		with open(path, 'rb') as image_file:
			content = image_file.read()
		image = vision.types.Image(content=content)

		objects = client.object_localization(
			image=image).localized_object_annotations
		return objects

		#print('Number of objects found: {}'.format(len(objects)))
		#for object_ in objects:
		#	print('\n{} (confidence: {})'.format(object_.name, object_.score))
		#	print('Normalized bounding polygon vertices: ')
		#	for vertex in object_.bounding_poly.normalized_vertices:
		#		print(' - ({}, {})'.format(vertex.x, vertex.y))
				

	def label_objects(self,filename):
		# Imports the Google Cloud client library
		from google.cloud import vision
		from google.cloud.vision import types

		# Instantiates a client
		client = vision.ImageAnnotatorClient()

		# The name of the image file to annotate
		file_name = os.path.join(
			os.path.dirname(__file__),
			filename)

		# Loads the image into memory
		with io.open(file_name, 'rb') as image_file:
			content = image_file.read()

		image = types.Image(content=content)

		# Performs label detection on the image file
		response = client.label_detection(image=image)
		labels = response.label_annotations

		print('Labels:')
		for label in labels:
			print(label.description)
			
spot1={"leftBottomX","leftBottomY"}

pygame.camera.init()
pygame.camera.list_cameras() #Camera detected or not
cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()
img = cam.get_image()
pygame.image.save(img,"filename.jpg")
cam.stop()

goo = GoogleVisionApi()
objects = goo.localize_objects('filename.jpg')


print('Number of objects found: {}'.format(len(objects)))
for object_ in objects:
	print('\n{} (confidence: {})'.format(object_.name, object_.score))
	print('Normalized bounding polygon vertices: ')
	for vertex in object_.bounding_poly.normalized_vertices:
		print(' - ({}, {})'.format(vertex.x, vertex.y))
		
print('Car detected in spot 1 and spot 3 ')

