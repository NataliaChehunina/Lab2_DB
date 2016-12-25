from .views import View
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

class AbstractController:

	table = ''
	model = ''

	def get(self, request):
		return View(self.table + '.html', request, self.model(self.table).get()).renderPage()

	def add(self, request):
		if self.model(self.table).add(request.GET):
			return HttpResponse(1)
		return HttpResponse(0)

	def delete(self, request):
		self.model(self.table).delByID(request.GET['id'])
		return HttpResponseRedirect('/' + self.table + '/get')

	def update(self, request):
		if self.model(self.table).update(request.GET.copy()):
			return HttpResponse(1)
		return HttpResponse(0)

class IndexController (AbstractController):

	def __init__(self):
		self.table = 'index'
		self.model = IndexModel

class ArtistsController (AbstractController):

	def __init__(self):
		self.table = 'artists'
		self.model = ArtistsModel

class TracksController (AbstractController):

	def __init__(self):
		self.table = 'tracks'
		self.model = TracksModel

class StudiosController (AbstractController):

	def __init__(self):
		self.table = 'studios'
		self.model = StudiosModel

class AlbumsController (AbstractController):

	def __init__(self):
		self.table = 'albums'
		self.model = AlbumsModel