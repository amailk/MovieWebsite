import webbrowser

class Video():
    def __init__(self, title, main_actors, storyline, poster_image):
        self.title = title
        self.main_actors = main_actors
        self.storyline = storyline
        self.poster_image_url = poster_image


        VALID_RATINGS= ["G", "PG","PG-13", "R"]

    def is_movie(self):
        pass

class Tvshow(Video):
    def __init__(self, title, main_actors, storyline,poster_image,channel):
        Video.__init__(self,title,main_actors,storyline,poster_image)
        self.channel = channel
            
    def is_movie(self):
        return False

class Movie(Video):

    def __init__(self, title, main_actors, storyline, poster_image, trailer_youtube):
        Video.__init__(self, title, main_actors, storyline, poster_image)
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def is_movie(self):
        return True
