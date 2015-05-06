class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["happy birthday to you",
					"I dont want to get sued",
					"So I'll stop right there"])

happy_bday.sing_a_song()
