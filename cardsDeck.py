class Deck(object):
  '''Will simulate a deck of cards using Unicode Character(emojis)'''
  
  def __init__(self, *args, **kwargs):
    '''Initialize the deck of cards'''
    self.back = chr(127136)
    self.spades = list()
    self.hearts = list()
    self.clubs = list()
    self.diamonds = list()

  def put_hearts(self, *args, **kwargs):
    '''Populates the hearts list'''
    i = 127153
    while True:
      self.hearts.append(chr(i))
      i += 1
      if i == 127167:
        break
    return self.hearts

  def put_spades(self, *args, **kwargs):
    '''Populates the spades list'''
    i = 127137
    while True:
      self.spades.append(chr(i))
      i += 1
      if i == 127151:
        break
    return self.spades

  def put_diamonds(self, *args, **kwargs):
    '''Populates the diamonds list'''
    i = 127169
    while True:
      self.diamonds.append(chr(i))
      i += 1
      if i == 127183:
        break
    return self.diamonds
  
  def put_clubs(self, *args, **kwargs):
    '''Populates the clubs list'''
    i = 127185
    while True:
      self.clubs.append(chr(i))
      i += 1
      if i == 127199:
        break
    return self.clubs

class Game(Deck):
  '''Model for the game class'''
    
  def generate_deck(self, *args, **kwargs):
    '''Will create the game deck'''
    deck = Deck()
    hearts = deck.put_hearts()
    spades = deck.put_spades()
    diamonds = deck.put_diamonds()
    clubs = deck.put_clubs()
    self.play_deck = [ spades, hearts, clubs, diamonds]
    return self.play_deck
  
  def generate_ranks(self, suit):
    '''will generate the ranks for later counting'''
    self.ace = suit[0]
    self.numbered = [item for item in suit[1:10]]
    self.court = [item for item in suit[10:14]]

    return self.ace, self.numbered, self.court
      
  def generate_colors(self, play_deck):
  
    '''Will separate suits between red and black'''
    self.reds = play_deck[0] + play_deck[2]
    self.blacks = play_deck[1] + play_deck[3]
    
    return self.reds, self.blacks

game = Game()
cards = game.generate_deck()
game.generate_colors(cards)
print(game.reds)
game.generate_ranks(cards[0])
print(game.ace)
print(game.numbered)
print(game.court)

print(Deck().back)

Deck.put_hearts()

