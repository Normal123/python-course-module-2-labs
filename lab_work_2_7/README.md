##Laboratory Work 2.7

####Description
Here is its solution code:
 *solution_2_7.py*
```python

Write the code to do following: 
* Write a script that creates a new output file called myfile.txt 
* writes the string "Hello file world!" into it 
* write another code that opens myfile.txt in w+ mode 
* read and print its contents 
* write into “Hello file” string new value “my” – “Hello my file” 
* Save changes without file object close
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