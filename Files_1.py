# Writing text to files:

f = open('wasteland.txt', mode = 'wt' , encoding = 'utf-8')   # w - write, t - text sring

f.write("I like learing Python\n")
f.write("THis will overwrite the current text file\n")
f.write("I have to learn Data analysis")

f.close()
