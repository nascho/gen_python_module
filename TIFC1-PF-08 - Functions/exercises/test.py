# 1
# simple def method

def display_message():
  print("Hello today I am learning about Python Functions.")

# display_message()

# 2
# print a book title as an argument

def favourite_book(book='no book title submitted'):
  print(f"One of my favourite books is: {book}.")

# favourite_book('Alice in Wonderland')

# 3
# shirt method

def make_shirt(size='no shirt size submitted'):
  print(f"The shirt you have ordered is of size: {size.title()}.")
  print("The shirt will have your initials printed on the sleeves.")

# make_shirt()
# make_shirt('large')

def make_shirt_modified(size='large'):
  print("I love Python")
  size.lower()
  if size == 'large' or size == 'medium':
    print(f"The shirt you ordered is a {size.title()} in size.")
  else:
    print(f"The shirt you ordered is a {size.title()} in size.")

# make_shirt_modified()
# make_shirt_modified('medium')
# make_shirt_modified('small')

# 4
# city and country

def describe_city(city, country='Portugal'):
  print(f"{city.title()} is in {country.title()}")

# describe_city('lisbon')
# describe_city('lisbon', '')
# describe_city('porto')
# describe_city('berlin')
# describe_city('berlin', 'germany')

# 5
# music album

def make_album(artist_name, album_title, num_tracks=None):
    album = {
      'artist': artist_name,
      'title': album_title
    }
    if num_tracks:
      album['tracks'] = num_tracks

    return album

album_1 = make_album('The Beatles', 'Abbey Road')
album_2 = make_album('Pink Floyd', 'The Dark Side of the Moon')
album_3 = make_album('Radiohead', 'OK Computer')

# print(album_1)
# print(album_2)
# print(album_3)

# num of tracks
album_with_tracks = make_album('Nirvana', 'Nevermind', num_tracks=12)
# print(album_with_tracks)

# advanced task
while True:
  print("\nEnter the artist and album title (or type 'quit' to exit):")
  
  artist = input("Artist name: ").strip()
  if artist.lower() == 'quit':
      break
  
  title = input("Album title: ").strip()
  if title.lower() == 'quit':
      break

  # optional: ask for the number of tracks (can skip by pressing Enter)
  tracks = input("Number of tracks (press Enter to skip): ").strip()
  if tracks.lower() == 'quit':
      break

  # convert tracks input to integer if provided
  if tracks.isdigit():
      album = make_album(artist, title, num_tracks=int(tracks))
  else:
      album = make_album(artist, title)

  print("\n-----Album created:")
  print(album)
