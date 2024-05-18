if 3>2: 
    print("It Works!") 
if 5>2:
    print("5 is greater than 2")
else:
    print("5 is not greater than 2")
name="Sophie"
if name=='Kai':
    print("Hey Kai")
elif name=="Sophie":
    print("Hey Sophie")
else:
    print ("Hey Anonymous")
volume = 586
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")
# Change the volume if it's too loud or too quiet
if volume < 20 or volume > 80:
    volume = 89
    print("That's better!")
def hi ():
    print("Hi There!")
    print ("How are you?")
hi()
def hi(name):
    if name == 'Sophie':
        print('Hi Sophie!')
    elif name == 'Kai':
        print('Hi Kai!')
    else:
        print('Hi anonymous!')
hi(name)
girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Sophie']
def hi(name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('Next girl')
for i in range(1, 6):
    print(i)