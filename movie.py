class Movie:
  

  def __init__(self, title, director, year, duration):
    self.title = title
    self.director = director
    self.year = year
    self.duration = duration


  def __str__(self):
    return f"{self.title} ({self.year}) - Directed by {self.director} ({self.duration} minutes)"
  
  
  def play(self):
    print(f"Playing: {self.title}...")

    
  def play2(self):
    print(f"Playing: {self.title}...")

movie1 = Movie("RRR", "Jyothiswar", 2022, 142)
movie2 = Movie("Motu_Patulu", "Ramesh babu", 2000, 177)


print(movie1)
print(movie2)


movie1.play()
movie2.play2()

