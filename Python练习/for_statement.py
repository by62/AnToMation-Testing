words = ['cat','window','defenestrate']
for w in words:
    print w,len(w)
    
for s in words[:]:
    if len(s) >=6:
        words.insert(0,s)
        print words
