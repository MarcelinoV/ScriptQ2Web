testfile = open("testfile.txt", "w")
# Code above creates new file
# Code below writes into that new file
testfile.write('''
Do you like python?\n
How good are you at it?\n
Show me something.
''')
# Code below closes the file
testfile.close()