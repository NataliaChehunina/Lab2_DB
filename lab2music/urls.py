from django.conf.urls import url
from .controllers import *

urlpatterns = [

    url(r'^$', IndexController().get),

    url(r'artists/get', ArtistsController().get),
    url(r'artists/add', ArtistsController().add),
    url(r'artists/upd', ArtistsController().update),
    url(r'artists/delete', ArtistsController().delete),

    url(r'studios/get', StudiosController().get),
    url(r'studios/add', StudiosController().add),
    url(r'studios/delete', StudiosController().delete),

    url(r'albums/get', AlbumsController().get),
    url(r'albums/add', AlbumsController().add),
    url(r'albums/delete', AlbumsController().delete),

    url(r'tracks/get', TracksController().get),
    url(r'tracks/add', TracksController().add),
    url(r'tracks/delete', TracksController().delete),

    url(r'fill-db-from-json', IndexController().add)

]
