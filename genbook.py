#combine all together to make a book with links

fout = open('Pythonbook.md', 'w')

fin = open('prefix.md','r')
all_of_it = fin.read()
fin.close()
fout.write(all_of_it)

fin = open('Chapters.md','r')
all_of_it = fin.read()
fin.close()

fout.write(all_of_it)
fout.write('\n\n\n')


for i in range(11):
    try:
        print(i)
        fin = open('Chapter%s.md'%i, 'r')
        all_of_it = fin.read()
        fin.close()
        fout.write(all_of_it)
        fout.write('\n\n\n')

    except Exception as ex:
        print(ex)
fout.close()


