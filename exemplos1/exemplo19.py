t = "25"
int(t)
# str→int
float("1.75")
str(100)
bool(1)


int("abc")
# ValueError!
int("3.5")
# ValueError!
float("3.5")
# OK: 3.5


bool(0) #False
bool(1) #True
bool(-5) #True
bool("") #False
bool("oi") #True
bool(None) #False