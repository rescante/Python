class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("movie objesi oluşturuldu.")
    
    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration

    def __del__(self):
        print('movie silindi.')

m = Movie("başlık adı", "yönetmen adı", 120)

print(str(m))
# print(len(m))

