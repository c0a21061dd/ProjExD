import random



def shutudai():
    global moji_lst
    moji_lst = []
    for i in range(10):
        a = random.choice(alphabet_lst)
        moji_lst.append(str(a))
        alphabet_lst.remove(a)
    print("対象文字:")
    print(moji_lst)

def kaitou():
    moji1 = moji_lst
    a = []
    for i in range(2):
        random.shuffle(moji_lst)
        a.append((moji_lst).pop())
    print("表示文字:")
    print(moji_lst)
    #print(len(moji_lst))

    ans1P = int(input("欠損文字数はいくつあるでしょうか？"))
    if ans1P == (10 - len(moji_lst)):
        print("正解です。それでは具体的に欠損文字数を1ずつ入力してください")
        ans2P = input("1つ目の文字を入力してください")
        ans3P = input("2つ目の文字を入力してください")
        if (ans2P and ans3P in a) and ans2P != ans3P:
            print("正解です。おめでとうございます。")
        else:
            print("不正解です。またチャレンジしてください。")
    else:
        print("不正解です。またチャレンジしてください。")


if __name__ == "__main__":
    alphabet_lst = ([chr(ord("a")+i) for i in range(26)])
    shutudai()
    kaitou()