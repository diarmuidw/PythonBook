from genchapter import run


CHAPTER = '##'
SECTION = '- '
f = open('Chapters.md', 'r')
lines = f.readlines()
currentchaptertitle = ''
sections = []
chapteroutline = ''
chapternumber = ''
for l in lines:
    try:
        prefix = l[:2]
        if prefix == CHAPTER:
            #so we have hit a new chapter. Now is the time to call openai to create each of the sections
            if currentchaptertitle != '' and int(chapternumber) == 1:
                print(title)
                print(chapternumber)
                print(sections)
                print(chapteroutline)
                run('0.1', chaptertitle=title, chapternumber=chapternumber, sections=sections, sectionoutline=chapteroutline)
                pass
            title =  l[3:]
            chapternumber = title.split(' ')[1].replace(':','')
            currentchaptertitle = title 
            #reset
            sections = []
            
            chapteroutline = ''
            
        elif prefix ==  SECTION:
            
            section = l[2:]
            sections.append(section)
            chapteroutline = chapteroutline + section
    except Exception as ex:
        print(ex)

    

#Now print the last one
run('0.1', chaptertitle=title, chapternumber=chapternumber, sections=sections, sectionoutline=chapteroutline)
