phrase = "Don't panic!"
# we turn the String into a list
plist = list(phrase)
print(phrase)
print(plist)

for i in range(4):
    plist.pop()

plist.pop(0)
plist.remove("'")
# Swap the two objects at the end of the list by
# first popping each object from the list, then using
# the popped objects to extend the list. This is a
# line of code that you'll need to think about for a
# little bit. Key point: the pops occur *first* (in
# the order shown), then the extend happens.
plist.extend([plist.pop(), plist.pop()])
plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)