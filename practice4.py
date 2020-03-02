def modifySong(songStr):
    for ch in songStr:
        if ch in ",.?":
            songStr = songStr.replace(ch,'')
    return songStr

def wordCount(songCount):
    global mydict
    songList = songCount.split()
    mydict = {wd:songList.count(wd) for wd in set(songList)}

def print_list(listeds):
    global songsorted
    for i in range(len(listeds)):
        print(songsorted[i][0],end = " ")


fn = "ch14_51.txt"
with open(fn) as file_Obj:
    data = file_Obj.read()
mydict = {}
song = modifySong(data.lower())

wordCount(song)
print("以下是最後執行結果")
print(mydict)

songsorted = sorted(mydict.items(),key = lambda item:item[1])
songsorted.reverse()
print(songsorted)
print_list(songsorted)