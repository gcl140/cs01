#initial state: constants
# state/models: global variables
# controller: keypress functions (changes variables only)
# draw function : view code clear, ball, paddles, draw
# update code modifies: x, y, vx, vy... 
# u can set paddles with velocity too, but no need


mylist = [1,2,3,4,5]
i = 0
while i < len(mylist):
    item = mylist[i]
    item *= 2
    print(item)
    i += 1

print(mylist)
print("-----")
# for item in mylist:
for i in range(len(mylist)):
    mylist[i] *= 2
    print(mylist[i])
print(mylist)

for index in [0,1,2,3,4]:
    mylist[index] -= 200
    print(mylist[index])
print(mylist)

for index in range(len(mylist)):
    mylist[index] *= 3
    print(mylist[index])