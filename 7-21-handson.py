# 2026/7/21　メンター山野さん主催　「pythonで作る　CUIアプリ開発」
print("~~~ 習慣コケッコーへようこそ ~~~")

while True:             #ずっとループするよ
    count_h = int(input("今日の習慣をチェック（1～5）："))
    
    if count_h > 0 and count_h <= 5:
        break           #1～5の数字が入力されたらループから抜ける
    print("1~5の数字を入力してください")

habits = []
for i in range(count_h):
    name = input(str(i+1)+"つ目を入力：")
    habits.append(name)
print("\n---チェック開始---")
success_count = 0

for habit in habits:
    result = input("「"+habit +"」はできた？(y/n)")

    if result == "y" or result == "Y":
        print("ｺｹｯｺｯｺー（おめでとう）")
        success_count = success_count + 1
    else:
        print("ｺｹｯｺ!!(次は頑張ろう)")

# coke = int(success_count / count_h * 100)

print("\n" + "=" *30)
print("結果"+str(success_count)+"/"+ str(count_h) + "　　" + str(int(success_count / count_h * 100)) + "%")

if success_count == count_h and success_count > 0:
    print("ｺｯｺｯｺ…ｺｹ~~~!!（パーフェクトだウォルター）")
elif success_count >= count_h/2:
    print("ｺｯｺｯｹ!!（半分以上…やるやん）")
else:
    print("明日からがんばろな")
print("="*30)