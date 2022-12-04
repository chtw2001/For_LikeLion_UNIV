NATO = {
    'A':"ALFA", 'B':"BRAVO",'C': "CHARLIE", 'D':"DELTA", 'E':"ECHO",
    'F': "FOXTROT",'G': "GOLF",'H': "HOTEL",'I': "INDIA",'J': "JULIETT",
    'K': "KILO",'L': "LIMA",'M': "MIKE",'N': "NOVEMBER",'O': "OSCAR",
    'P': "PAPA",'Q': "QUEBEC",'R': "ROMEO",'S': "SIERRA",'T': "TANGO",
    'U': "UNIFORM",'V': "VICTOR",'W': "WHISKEY",'X': "XRAY",'Y': "YANKEE",
    'Z': "ZULU"
}

s, q = input().split()
s1 = []
for i in s:
    s1.append(i)
for i in range(int(q)):
    a, b = map(int, input().split())
    if a == 2:
        s = s1
        s2 = ''
        for k in s1:
            s2 += k
        print(s2[b-1], end='')
        s1 = s
    else:
        for k in range(len(s1)):
            s1[k] = NATO[s1[k]]
    
