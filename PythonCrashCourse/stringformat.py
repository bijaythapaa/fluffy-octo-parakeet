import dis
from string import Template

def greet(name, question):
	return f"Hello {name}! {question}"

string = greet('Ram', "What's your Problem?")
print(string)

dis.dis(greet)

name="Bijay Thapa"
errno = 50159747054

print(f"Hey {name}, there's a {errno:#x} error !!")

temp_string = "Hello $name, there's a $error"
output = Template(temp_string).substitute(name=name, error=hex(errno))
print(output)
