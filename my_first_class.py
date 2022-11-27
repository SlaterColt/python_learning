class MyFirstClass:
    print('Who wrote this?')
    index = 'Author-Book'

    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book: " + book)

whodunnit = MyFirstClass()
whodunnit.hand_list('Sun Tsu', 'The Art of War')