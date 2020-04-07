


import string 


letters=list(string.ascii_lowercase)


caesarFile= open("caesar_plain.txt","r+")
caesarOutFile= open("caesarOutput.txt","w+")

playFairFile=open("playfair_plain.txt","r")
playFairOutFile=open("playfairOutput.txt","w+")

hill2x2File=open("hill_plain_2x2.txt","r+")
hill2x2OutFile=open("Hill2x2output.txt","w+")

hill3x3File=open("hill_plain_3x3.txt","r+")
hill3x3OutFile=open("Hill3x3Output.txt","w+")

vernamFile=open("vernam_plain.txt","r+")
vernamOutFile=open("vernamOutput.txt","w+")

vigernereFile=open("vigenere_plain.txt","r+")
vigenereOutFile=open("vigenereOutput.txt","w+")


def Caesar(plainText,key):
    text = plainText
    text.strip() 
    text.lower()
    plain=list(plainText) 
    plain = [v.lower() for v in plain]
    plain = [v.strip() for v in plain]
    newText="" 

    for i in range(len(plain)):
        if plain[i] == '':
            continue
        shiftAmount= int(key)
        indexOfNewLetter=letters.index(plain[i]) + shiftAmount
        if indexOfNewLetter > 25 : 
            indexOfNewLetter =indexOfNewLetter - 26 
        newText+=letters[indexOfNewLetter] 

    # caesarOutFile.write("Caesar Output using "+str(key)+" as a key:"+newText+"\n")
    # caesarOutFile.write("\n") 
    print (newText)
    return newText 



def find_position(key_matrix,letter):
	x=y=0
	for i in range(5):
		for j in range(5):
			if key_matrix[i][j]==letter:
				x=i
				y=j

	return x,y
 
def playFair(plainText,key):
    letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    w, h = 5, 5
    plainText=plainText.replace("j", "i")
    # matrix = [[0 for x in range(w)] for y in range(h)]
    plain=list(plainText)
    plain = [v.lower() for v in plain]
    plain = [v.strip() for v in plain]
    keyText=list(key)
    newText=""
    i=0
    k=0
    keyIndex=0
    mymatrix = []
    for j in range(len(keyText)):
        if  not keyText[j]  in mymatrix:
            if keyText[i]=='j':
                mymatrix.append('i')
            else:
                mymatrix.append(keyText[j])           
    for j in letters:
        if j not in key: 
            mymatrix.append(letters[letters.index(j)])

    matrix = [mymatrix[i:i+5] for i in range(0, 25, 5) ]
    for i in range(0,len(plain)-1,2): 
        if plain[i]==plain[i+1]:
            plain.insert(i+1,'x')   
    if len(plain) % 2 !=0:
            plain.append('x') 
    for i in range(0,len(plain)-1,2):
        x1,y1=find_position(matrix,plain[i])
        x2,y2=find_position(matrix,plain[i+1])
        if x1==x2:
            newText+=matrix[x1][(y1+1) % 5]
            newText+=matrix[x2][(y2+1) % 5] 

        elif y1==y2:
            newText+=matrix[(x1+1) % 5][y1]
            newText+=matrix[(x2+1) % 5][y2] 
        else:
            newText+=matrix[x1][y2]
            newText+=matrix[x2][y1] 

    playFairOutFile.write("Play Fair Output using "+key+" as a key:"+newText+"\n")
    playFairOutFile.write("\n") 
    print(newText)



def Hill(plainText,key):
    plain = [v.strip() for v in plainText]
    plain = [v.lower() for v in plainText]
    plain=list(plain)
    
   
    textMatrix=[]
    matrix=[]
    transMatrix=[]
    
    if len(key)==2:  
        for i in range(len(plainText)):
            if plain[i] == '':
                continue  
            textMatrix+=[letters.index(plain[i])]
        
        if(len(plain) %2 != 0 ):
            textMatrix.append(letters.index('x'))
        matrix = [textMatrix[i:i+2] for i in range(0, len(plainText), 2) ]
        transMatrix=[ [ 0 for x in range( len(matrix) ) ] for y in range( 2 )]
        for i in range(2):
            for j in range(len(matrix)):
                transMatrix[i][j]=matrix[j][i]
        result = [[ 0 for y in range( len(transMatrix[0]) ) ] for x in range( 2)]
        finalMatrix=""
        for i in range(len(key)):  
            for j in range(len(transMatrix[0])):  
                for k in range(len(transMatrix)): 
                    result[i][j] += ( transMatrix[k][j] * key[i][k] )
                    result[i][j]= result[i][j] % 26 
        for i in range(len(result[0])):
            for j in range(len(result)):
                finalMatrix+= letters[result[j][i]]  
        # hill2x2OutFile.write("Hill 2x2 Output: "+finalMatrix+"\n")
        # hill2x2OutFile.write("\n") 
        
    elif len(key)==3:
        for i in range(len(plainText)):
            if plain[i] == '':
                continue 
            textMatrix+=[letters.index(plain[i])]
        if(len(plain)%3 == 1):
            textMatrix.append(letters.index('x'))
            textMatrix.append(letters.index('x'))
        if(len(plain)%3 == 2 ):
            textMatrix.append(letters.index('x'))
        matrix = [textMatrix[i:i+3] for i in range(0, len(plainText), 3) ]
        transMatrix=[ [ 0 for x in range( len(matrix) ) ] for y in range( 3 )]
        for i in range(3):
            for j in range(len(matrix)):
                transMatrix[i][j]=matrix[j][i]
        print(transMatrix)
        result = [[ 0 for y in range( len(transMatrix[0]) ) ] for x in range( 3 )]
        finalMatrix=""
        for i in range(len(key)):  
            for j in range(len(transMatrix[0])):  
                for k in range(len(transMatrix)): 
                    result[i][j] += ( transMatrix[k][j] * key[i][k] ) 
                    result[i][j]= result[i][j] % 26 
        for i in range(len(result[0])):
            for j in range(len(result)):
                finalMatrix+= letters[result[j][i]] 
        hill3x3OutFile.write("Hill 3x3 Output: "+finalMatrix+"\n")
        print("fe eh")
        hill3x3OutFile.write("\n") 
    print(finalMatrix)   





    

def vegienere(plainText,key,mode):
    keyRep=list(key)
    keyAuto=list(key)
    plain=list(plainText)
    plain = [v.lower() for v in plain]
    plain = [v.strip() for v in plain]
    newText="" 
    if mode:
        for i in range(len(plainText)):
            if len(keyAuto)<len(plainText):
                keyAuto += plain[i]
        for i in range(len(plain)):
            if plain[i] == '':
                continue
            shiftAmount= letters.index(keyAuto[i])
            indexOfNewLetter=(letters.index(plain[i]) + shiftAmount) % 26
            newText+=letters[indexOfNewLetter]
        # vigenereOutFile.write("Vigenere auto Output using "+key+" as a key:"+newText+"\n")
        # vigenereOutFile.write("\n")
        print (newText)
        return newText
   
    else:
        for i in range(len(plainText)):
            if len(keyRep)<len(plainText):
                keyRep += keyRep[i]
        for i in range(len(plain)):
            if plain[i] == '':
                continue
            shiftAmount= letters.index(keyRep[i])
            indexOfNewLetter=(letters.index(plain[i]) + shiftAmount) % 26
            newText+=letters[indexOfNewLetter] 
        vigenereOutFile.write("Vigenere Repeating Output using "+key+" as a key:"+newText+"\n")
        vigenereOutFile.write("\n")
        print (newText)
        return newText
    
    




def Vernam(plainText,key):
    keylist=list(key)
    plain=list(plainText)
    plain = [v.lower() for v in plain]
    keylist = [v.lower() for v in keylist]
    plain = [v.strip() for v in plain]
    newText="" 
    for i in range(len(plain)):
        if plain[i] == '':
            continue
        shiftAmount= letters.index(keylist[i])
        indexOfNewLetter=(letters.index(plain[i]) + shiftAmount) % 26
        newText+=letters[indexOfNewLetter]
    vernamOutFile.write("Vernam Output using "+key+" as a key:"+newText+"\n")
    vernamOutFile.write("\n") 
    print(newText)





def main():
    f1=caesarFile.readlines()    
    for x in f1:
        test = Caesar(x,3)
    for x in f1:
        test = Caesar(x,6)
    for x in f1:
        test = Caesar(x,12)

    fPlay=playFairFile.readlines() 
    # playFair("rkesbbra","rats")
    # playFair("umtqoejz","rats")
    # playFair("ccwobhnb","rats")
    # playFair("ymnqicpx","rats")
    # playFair("ipmxxpzw","rats")  
    # playFair("rkesbbra","archangel")
    # playFair("umtqoejz","archangel")
    # playFair("ccwobhnb","archangel")
    # playFair("ymnqicpx","archangel")
    # playFair("ipmxxpzw","archangel")   
    for x in fPlay:
        playFair(x,"rats")
        
    for x in fPlay:
       
        playFair(x,"archangel")

    fveg=vigernereFile.readlines()   
    for x in fveg:
        x.strip()
        vegienere(x,"pie",False)
    for x in fveg:
        x.strip()
        vegienere(x,"aether",True)

    Hill("VVMSQFGA",[[5,17],[8,3]])
    Hill("IUETTRZQ",[[5,17],[8,3]])
    Hill("DAKYTDGF",[[5,17],[8,3]])
    Hill("VQUNPMHV",[[5,17],[8,3]])

    Hill("YGREBGHZ",[[2,4,12],[9,1,6],[7,5,3]])
    Hill("BKDLPUKN",[[2,4,12],[9,1,6],[7,5,3]])
    Hill("FSSZULIH",[[2,4,12],[9,1,6],[7,5,3]])
    Hill("JFOXRSFQ",[[2,4,12],[9,1,6],[7,5,3]])
    fhill2=hill2x2File.readlines() 
    for x in fhill2:
        Hill(x,[[5,17],[8,3]]) 
    fhill3=hill3x3File.readlines() 
    for x in fhill3:
        Hill(x,[[2,4,12],[9,1,6],[7,5,3]])   

    fver=vernamFile.readlines()    
    for x in fver:
        Vernam(x,"SPARTANS") 

    caesarInput = raw_input("Enter Plain Text for Caeser Cipher : ")
    caesarInputKey = int(raw_input("Enter Key for Caeser Cipher : "))
    
    Caesar(caesarInput,caesarInputKey)
    
    x = raw_input("Enter Plain Text for Play Fair Cipher : ")
    y = raw_input("Enter Key for Play Fair Cipher : ")
    playFair(x,y)
    
    hillinput = raw_input("Enter Plain Text for Hill Cipher : ")
    keylist = [ ] 
    size = int(input("Enter number of rows of the hill matrix : ")) 
    if (size==2):
        for i in range(0, size): 
            row = [int(input()),int(input())] 
            keylist.append(row)  
    elif (size==3):
        for i in range(0, size): 
            row = [int(input()),int(input()),int(input())] 
            keylist.append(row)  
    
    Hill(hillinput,keylist)
    
    verinput = raw_input("Enter Plain Text for Vernam Cipher : ")
    verkey = raw_input("Enter Key for Vernam Cipher : ")
    Vernam(verinput,verkey)
    
    viginput = raw_input("Enter Plain Text for Vigenere Cipher : ")
    vigkey = raw_input("Enter Key for Vigenere Cipher : ")
    mode = raw_input("Enter mode for Vigenere Cipher,False for repetitve mode or True for auto mode : ")
    if(mode=="False"):
        vegienere(viginput,vigkey,False)
    elif(mode=="True"):
        vegienere(viginput,vigkey,True)
        
    raw_input()

if __name__== "__main__":
    main()
    






