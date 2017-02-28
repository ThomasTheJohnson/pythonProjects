import random;

print "\nI'm thinking of a number 1-10, care to guess?";

ans = random.randint(1,10);
correct = False;

while (not correct):
    guess = input("");
    if(guess == ans):
        correct = True;
    else:
        print "Nope.";
print "Yep!\n"
