import webbrowser


class Video():
    """Describes a Video"""

    def __init__(self, title, main_actors, storyline, poster_image):
        """Initializes a Video object"""
        self.title = title
        self.main_actors = main_actors
        self.storyline = storyline
        self.poster_image_url = poster_image

    def is_movie(self):
        """Determine if a Video is a Tvshow or a Movie"""
        pass


class Tvshow(Video):
    """Describes a Video which is a Tvshow with channel information"""

    def __init__(self, title, main_actors, storyline, poster_image, channel):
        """Initializes the Tvshow object"""
        Video.__init__(self, title, main_actors, storyline, poster_image)
        self.channel = channel

    def is_movie(self):
        """Returns that this is not a movie"""
        return False


class Movie(Video):
    """Describes a Video which is a Movie with a youtube trailer"""

    def __init__(self, title, main_actors, storyline, poster_image,
                 trailer_youtube):

        """Initializes the Movie object"""
        Video.__init__(self, title, main_actors, storyline, poster_image)
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens the trailer of a Movie object"""
        webbrowser.open(self.trailer_youtube_url)

    def is_movie(self):
        """Returns that this is a movie"""
        return True
