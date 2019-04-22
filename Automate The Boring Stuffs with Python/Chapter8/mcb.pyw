import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')
    #Todo: Save clipboard Content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    #Todo: delete with keyword
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    mcbShelf.pop(sys.argv[2])
elif len(sys.argv) == 2:
    #List keywords and load content
    if sys.argv[1].lower() == 'list':
       # pyperclip.copy('sound double weird')
        pyperclip.copy(str(list(mcbShelf.keys())))
    #delete all keywords
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        


mcbShelf.close()