#九九の答えを出力するプログラム 
for i in range(1, 10): #range(1, 10)は1から9までの整数を生成する
    for j in range(1 , 10):
        print(i * j, end=' ')
    print("「"+str(i)+"」の段です") #print()があることで改行し、str(i)でiの文字を返す
