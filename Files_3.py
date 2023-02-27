## Appending demotstration:
h = open('wasteland.txt', mode = 'at' , encoding = 'utf-8')
h.writelines([' Son of a man\n',
              'You cannot say ,or guess,\n'
              'for you know only\n,'
              'A heap of broken images\n'])

h.close()
