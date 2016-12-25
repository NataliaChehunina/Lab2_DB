from . import db
import json

class BaseModel:

	table = ''

	def __init__(self, table):
		self.table = table

	def add(self, data, whereKey = 'name'):
		if db.select(self.table, 'count(*) as `count`', db.getWhere({'name': data[whereKey]})) [0]['count'] > 0:
			return False
		return db.insert(self.table, data)

	def get(self):
		return db.select(self.table)

	def update(self, data):
		id = data['id']; del data['id']
		return db.update(self.table, data, db.getWhere({'id': id}))

	def delByID(self, id):
		db.delete(self.table, where = "WHERE `id` = '" + str(id) + "'")
		return self
# 
class IndexModel (BaseModel):

	def get(self):
		return []
	
	def add(self, emptyData):
		with open('lab2music/static/db.json') as dataFile:
			data = json.load(dataFile)
			for self.table in data:
				for row in data[self.table]:
					super().add(row)
		return True
#
class ArtistsModel (BaseModel):
	pass
#
class StudiosModel (BaseModel):
	pass
#
class AlbumsModel (BaseModel):
	
	def get(self):
		fields = '`artists`.`name` as `artist`, `studios`.`name` as `studio`, \
					`albums`.`id` as `id`, `albums`.`name` as `album`, `year`, `style`'
		tables = '`albums`, `artists`, `studios`'
		where = '`artist_id` = `artists`.`id` and `studio_id` = `studios`.`id`'
		return db.select(tables, fields, 'WHERE ' + where)

	def add(self, data):
		artist = db.select('`artists`', '`id`', db.getWhere({'name': data['artist']}))
		studio = db.select('`studios`', '`id`', db.getWhere({'name': data['studio']}))
		if len(artist) == 0 or len(studio) == 0:
			return False
		return super().add({'name': data['album'], 'year': data['year'], 'style': data['style'],
							'artist_id': artist[0]['id'], 'studio_id': studio[0]['id']})
#
class TracksModel (BaseModel):
	
	def get(self):
		fields = '`artists`.`name` as `artist`, `studios`.`name` as `studio`, `tracks`.`id` as `id`, `date_record`, \
					`albums`.`name` as `album`, `albums`.`style` as `style`, `tracks`.`name` as `track`, `duration`'
		tables = '`albums`, `artists`, `studios`, `tracks`'
		where = '`artist_id` = `artists`.`id` and `studio_id` = `studios`.`id` and `album_id` = `albums`.`id`'
		return db.select(tables, fields, 'WHERE ' + where)

	def add(self, data):
		album = db.select('`albums`', '`id`', db.getWhere({'name': data['album']}))
		if len(album) == 0:
			return False
		return super().add({'name': data['track'], 'duration': data['duration'],
							'date_record': data['date_record'], 'album_id': album[0]['id']})