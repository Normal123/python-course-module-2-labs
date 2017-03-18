"""
Write a script that creates a new output file called myfile.txt
"""
creator= open('files\myfile.txt', 'w')
"""
writes the string "Hello file world!" into it
"""
creator.write('Hello file world')
creator.close()
"""
write another code that opens myfile.txt in r+ mode
read and print its content
"""
editor=open('files\myfile.txt', 'r+')
print(editor.read())
"""
write into “Hello file” string new value “my” – “Hello my file”
"""
editor.seek(len('Hello'))
editor.write('my file world')

"""
Save changes without file object close
"""
editor.flush()
editor.close()

printer= open('files/myfile.txt')
print(printer.read())
printer.close()
