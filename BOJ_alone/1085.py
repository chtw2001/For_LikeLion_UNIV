x,y,w,h = map(int, input().split())
loc = []
loc.append(x)
loc.append(y)
loc.append(w-x)
loc.append(h-y)
print(min(loc))