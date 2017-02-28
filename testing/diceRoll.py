import random;

print "\n Rolling the dice.."

done = False;
while (not done):
    d1 = random.randint(1,6);
    d2 = random.randint(1,6);
    print d1;
    print d2;
    ans = "";
    ans = raw_input("Done? Y/N\n");
    if(ans=="Y"):
        done = True;
