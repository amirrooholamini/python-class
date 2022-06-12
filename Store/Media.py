class Media:
    def __init__(self, id, name, director, score, casts, url=None):
        self.id = id
        self.name = name     
        self.director = director 
        self.score = score    
        self.url = url    
        self.casts = casts    

    def show_info(self):
        print("id: ", self.id, ' name: ', self.name, ' director: ', self.director, ' score ', self.score)

    def download(self):
        pass


class Clip(Media):
    def __init__(self, id, name, director, score, duration, casts, url=None):
        self.duration = duration
        super().__init__(id, name, director, score, casts, url)

class Documentary(Media):
    def __init__(self, id, name, director, score, duration, casts, url=None):
        self.duration = duration
        super().__init__(id, name , director, score, casts, url)


class Series(Media):
    def __init__(self, id, name, director, score, casts, url=None, parts=0):
        self.parts = parts
        super().__init__(id, name, director, score, casts, url)


class Film(Media):
    def __init__(self, id, name, director, score, duration, casts, url=None, genre=''):
        self.genre = genre
        self.duration = duration
        super().__init__(id, name, director, score, casts, url)


    