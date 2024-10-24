def WordFreq(str):
    words = str.split()
    
    freq = {}
    
    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word] = 1
            
    for word, count in freq.items():
        print(f"frequency of {word} is : {count}")
        

MusicList = "Madcom RHCP TOOL RATM Primus Pink-Floyd The-beatles RHCP QUEEN RHCP RHCP RHCP RHCP The-B-52's RHCP RHCP Goreg-baker-selection bill-Whithers Nirvana XXX SEATBELTS KIL  Nirvana Mild-hight-club yuog-kanno MF-DOOM Woody-jackson yes Billie-Eillish BBNO$ skee-Lo Gorge-michael Fleetwood-mac Daft-punk Gorillaz RHCP Tame-Impala RHCP Dream-Theater Iron-maden Black-Sabbath Muse TOOL Ice-Cube Bernad-Weight RHCP Primus Primus Marcus-miller Eminem RHCP Måneskin RHCP Hushpuppets Green-day RHCP Patrice-rushen The-Beatles Eminem RHCP jojo RHCP RHCP The-Chemical-brothers RHCP Primus Metallica RHCP Primus Ben-E.-King The-Clash Primus The-B-52's Victor-Wooten Primus Her's Rammstein TOOL Primus Primus Primus Boney-M Primus Metallica Her's Mac-DeMarco Les-Claypool Primus Primus RATM RHCP RHCP artic-monkeys artic-monkeys Asop-rock Primus RHCP Her's Black-Eyed-peas stiftelsen The-Drums RHCP Primus takanaka"

WordFreq(MusicList)