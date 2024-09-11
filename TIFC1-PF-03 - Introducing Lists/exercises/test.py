# 1
artist_list = ['al green', 'prince', 'phil collins']

for name in artist_list:
  print(name.title())

# 2
for name in artist_list:
  print(f'Hello {name.title()}, nice to meet you.')

# 3
book_list = ['goldfinger', 'pride and prejudice', 'catch-22']
author_list = ['iam flemming', 'jane austin', 'joseph heller']

for book in book_list:
  print(f'My favourite book is {book.title()}.')

for name, book in zip(author_list, book_list):
  print(f'Hello {name.title()}, I liked your book {book.title()}, it was interesting.')

print('/******************************************************/')

# 4
# original guest list
guest_list = ['elon musk', 'warren buffet', 'nikola tesla']

for guest in guest_list:
  print(f'Hello {guest.title()}, you are invited to dinner.')
print('Unfortunately Warren Buffet is unable to attend.')

print('/******************************************************/')

# updated guest list
guest_list = ['elon musk', 'jamie dimon', 'nikola tesla']

for guest in guest_list:
  print(f'Hello {guest.title()}, you are invited to dinner.')

print('/******************************************************/')

# found a bigger table and informing guests
for guest in guest_list:
  print(f'Hello {guest.title()}, I have managed to locate a larger table and therefore, we will be having more guests.')

print('/******************************************************/')

# adding new guests
guest_list.insert(0, 'girl one')
guest_list.insert(3, 'girl two')
guest_list.append('girl three')

print(guest_list)

# print new guest list invites
for guest in guest_list:
  print(f'Hello {guest.title()}, you are invited to dinner.')

print('/******************************************************/')

print('I only have a table big enough for 2 guests')

print('/******************************************************/')

print(guest_list)

while len(guest_list) > 2:
  guest = guest_list.pop()
  print(f'Sorry no space for you {guest}')
print(guest_list)

print('/******************************************************/')

print(guest_list)

for guest in guest_list:
  print(f'You\'re still on the list {guest}')

print('/******************************************************/')

print(guest_list)

del guest_list[0:2]

print(guest_list)

print(len(guest_list))