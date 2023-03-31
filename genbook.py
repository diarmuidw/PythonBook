#combine all together to make a book with links

fout = open('book.md', 'w')

fin = open('Chapters.md','r')
all_of_it = fin.read()
fin.close()

fout.write(all_of_it)

for i in range(11):
    try:
        print(i)
        fin = open('Chapter%s.md'%i, 'r')
        all_of_it = fin.read()
        fin.close()
        fout.write(all_of_it)
    except Exception as ex:
        print(ex)
fout.close()


