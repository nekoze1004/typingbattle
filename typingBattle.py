from tkinter import *
from tkinter import ttk
from github import Github
import setting
import git
import os
import sqlite3
from contextlib import closing


windowSize = "800x600+0+0"  # 共通のウインドウサイズ

ext_dir = {"Ruby":"rb","Python":"py","Swift":"swift"} 

g = Github(setting.Github_User, setting.Github_Pass)
dbname = "database.sqlite"

# トップ画面
def titleWindow():
    # 「おわる」ボタンを押したら画面を閉じる
    def quit_button():
        root.destroy()

    # 「はじめる」ボタンを押してメニュー画面に遷移
    def start_button():
        # entry_1の中身を取得
        entryValue = entry_1.get()
        print(entryValue)
        root.destroy()
        menuWindow()

    # ---------------------------------
    # GUI作成
    root = Tk()
    root.title("titleWindow")
    root.resizable(0, 0)  # ウインドウサイズの変更不可設定
    root.geometry(windowSize)

    # タイトル画面のタイトル
    label_title = Label(root, text="タイピングバトル", font=("", 70), height=3)
    label_title.pack(anchor="n")

    # タイトル画面のユーザ名
    label_1 = Label(root, text="ユーザ名", font=("", 30), height=3)
    entry_1 = Entry(root, width=30, font=("", 30))
    entry_1.insert(END, "ユーザ名を入力してください")

    label_1.pack(anchor="sw", padx="30")
    entry_1.pack()

    # タイトル画面のボタン
    button_start = Button(root, text="はじめる", font=("", 50), width=6, command=start_button)
    button_start.pack(side="left", padx="30")

    button_finish = Button(root, text="おわる", font=("", 50), width=6, command=quit_button)
    button_finish.pack(side="right", padx="30")

    # GUIの表示
    root.mainloop()
    # ---------------------------------


# メニュー画面
def menuWindow():
    # 「ゲームスタート」を押してステージ選択に遷移するボタン

    def start_game():
        valueCombo = combo.get()
        set_language = valueCombo
        print(set_language)
        root.destroy()
        stageSelectWindow(set_language)

    # galleryWindowに遷移するボタン
    def select_gallery():
        root.destroy()
        galleryWindow()

    # 設定画面を開くボタン
    def select_setting():
        root.destroy()
        settingWindow()

    # titleWindowに戻るボタン
    def back_button():
        root.destroy()
        titleWindow()

    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.pack(expand=1, fill=Tk.BOTH, anchor=Tk.NW)
        self.create_widgets()

    # ---------------------------------
    # GUI作成
    root = Tk()
    root.title("menuWindow")
    root.resizable(0, 0)  # ウインドウサイズの変更不可設定
    root.geometry(windowSize)
    label_title = Label(root, text="メニュー画面", font=("", 70), height=3)
    # label_title.pack(anchor="n")
    label_title.grid(columnspan=3)

    # コンボボックス
    # コンボボックスの作成(rootに配置,リストの値を編集不可(readonly)に設定)
    combo = ttk.Combobox(root, state='readonly', width=30)
    # リストの値を設定
    combo["values"] = tuple(ext_dir.keys())
    # デフォルトの値を食費(index=0)に設定
    combo.current(0)
    # コンボボックスの配置
    # combo.pack(pady=10)
    combo.grid(row=1, column=0, columnspan=3)

    # ボタン
    button_stage = Button(root, text="ゲームスタート", font=("", 50), command=start_game)
    button_gallery = Button(root, text="ギャラリー", font=("", 50), command=select_gallery)
    button_setting = Button(root, text="設定", font=("", 50), command=select_setting)
    button_back = Button(root, text="もどる", font=("", 50), command=back_button)
    """
    button_stage.pack(fill="x", padx=200, pady=4)
    button_gallery.pack(fill="x", side="left", padx=30, pady=4)
    button_setting.pack(fill="x", side="top", padx=30, pady=4)
    button_back.pack(fill="x", side="right", padx=30, pady=4)
    """
    button_stage.grid(row=2, column=0, columnspan=3, padx=50, pady=0, sticky=W + E)
    button_gallery.grid(row=3, column=0, padx=50, pady=10, sticky=W + E)
    button_setting.grid(row=3, column=1, padx=10, pady=10, sticky=W + E)
    button_back.grid(row=3, column=2, padx=50, pady=10, sticky=W + E)

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1, minsize=10)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(2, weight=1)

    # GUIの表示
    root.mainloop()
    # ---------------------------------


# ギャラリー画面
def galleryWindow():
    # menuWindowに戻るボタン
    def back_button():
        root.destroy()
        menuWindow()

    # ---------------------------------
    # GUI作成
    root = Tk()
    root.title("galleryWindow")
    root.resizable(0, 0)  # ウインドウサイズの変更不可設定
    root.geometry(windowSize)

    label_title = Label(root, text="ギャラリー画面", font=("", 70), height=3)
    label_title.pack(anchor="n")

    # ボタン
    button_back = Button(root, text="もどる", font=("", 50), width=6, command=back_button)
    button_back.pack()

    # GUIの表示
    root.mainloop()
    # ---------------------------------


# 設定画面
def settingWindow():
    # menuWindowに戻るボタン
    def back_button():
        root.destroy()
        menuWindow()

    # ---------------------------------
    # GUI作成
    root = Tk()
    root.title("settingWindow")
    root.resizable(0, 0)  # ウインドウサイズの変更不可設定
    root.geometry(windowSize)

    label_title = Label(root, text="設定画面", font=("", 70), height=3)
    label_title.pack(anchor="n")

    # ボタン
    button_back = Button(root, text="もどる", font=("", 50), width=6, command=back_button)
    button_back.pack()

    # GUIの表示
    root.mainloop()
    # ---------------------------------


def stageSelectWindow(set_language):
    # menuWindowに戻るボタン
    def back_button():
        root.destroy()
        menuWindow()

    # gameMainWindowへ進むボタン
    def start_button():
        root.destroy()
        gameMainWindow(set_language)

    def search(gh,repo_keyword, language):
        return gh.search_repositories("{0}+language:{1}".format(repo_keyword,language),sort="stars")[0]

    def clone(repo, path):
        clone_path = "{0}/{1}".format(path, repo.name)
        if not os.path.exists(clone_path):
            git.Git().clone("{0}".format(repo.git_url), clone_path)
        regist(clone_path)

    def regist(p): # p=path以下のファイルをデータベースに登録
        with closing(sqlite3.connect(dbname)) as conn:
            c = conn.cursor()

            # テーブルが存在してないなら作成
            create_sql = "create table if not exists files(name, path, complete, extension)"
            c.execute(create_sql)

            regist_sql = '''insert into files(name, path, complete, extension) select ?,?,?,? where not exists(select * from files where path = ?);'''
            def crawling(path): # path以下のファイルを洗い出し
                l = []
                for i in os.listdir(path):
                    if i[0] == ".": # dotfileをスルー
                        continue
                    new_path = os.path.join(path, i)
                    if os.path.isdir(new_path):
                        l += crawling(new_path)
                    else:
                        name = i
                        path_s = os.path.abspath(new_path)
                        complete = 0
                        root, ext = os.path.splitext(path_s)
                        ext = ext.replace(".", "", 1)
                        l.append((name, path_s, complete, ext, path_s))
                return l
            file_list = crawling(p)

            print(file_list)

            c.executemany(regist_sql, file_list)
            conn.commit()
            conn.close()

    def prepare_souce(gh, repo_keyword,language):
        repo = search(gh,repo_keyword, language)
        clone(repo, "repos")

    repo_keyword = "sample"
    prepare_souce(g,repo_keyword,set_language)

    # ---------------------------------
    # GUI作成
    root = Tk()
    root.title("stageSelectWindow")
    root.resizable(0, 0)  # ウインドウサイズの変更不可設定
    root.geometry(windowSize)

    label_title = Label(root, text="ステージ選択画面", font=("", 70), height=3)
    label_title.pack(anchor="n")

    # ボタン
    button_back = Button(root, text="もどる", font=("", 50), width=6, command=back_button)
    button_back.pack()

    button_start = Button(root, text="ゲームスタート", font=("", 50), command=start_button)
    button_start.pack()



    # GUIの表示
    root.mainloop()
    # ---------------------------------


def gameMainWindow(set_language):
    # menuWindowに戻るボタン
    def back_button():
        root.destroy()
        menuWindow()

    # gameResultWindowへ進むボタン
    # デバック用?
    # 本来はタイピングがクリア出来たらgameResultWindowへ行く
    def result_button():
        root.destroy()
        gameResultWindow()

    # もしtext[count]がコメントならば次のコメンドじゃないところまでcountをすすめて返す
    comment = {"Ruby":("#"), "Python":("#"), "swift":("//")}
    def overComment(text, count, set_language):
        puls = 0
        for c in comment[set_language]:
            print("コメントチェック:{0}".format(c))
            print(text[count])
            if c == text[count]:
                print("発見")
                while text[count+puls] != os.linesep:
                    puls += 1
                return puls+count
        return count


    # 入力時に正しいかどうか判定する
    # 入力した時に何かしたいときは個々に書く
    def check_input(event):
        print("pressed", repr(event.char))
        true_text = trueStr_buff.get()
        your_text = yourStr_buff.get()
        your_over = len(your_text)
        while True:
            next_over = overComment(true_text,your_over, set_language)
            if your_over < next_over:
                for i in range(your_over,next_over):
                    your_text += true_text[your_over]
                    your_over += 1
            else:
                break
        if true_text[your_over] == os.linesep:
            # 改行があったときは飛ばす
            your_over += 1
            your_text += os.linesep
            while true_text[your_over] == " " or true_text[your_over] == "\t":
                # 更に行頭の空白を飛ばす
                if true_text[your_over] == " ":
                    your_over += 1
                    your_text += " "
                elif true_text[your_over] == "\t":
                    your_over += 1
                    your_text += "\t"
            while True:
                next_over = overComment(true_text,your_over, set_language)
                if your_over < next_over:
                    for i in range(your_over,next_over):
                        your_text += true_text[your_over]
                        your_over += 1
                else:
                    break
        if true_text[your_over] == event.char:
            # キー入力が正しいとき
            your_text += true_text[your_over]
            your_over += 1
        yourStr_buff.set(your_text)

    # ---------------------------------
    # GUI作成
    root = Tk()
    root.title("gameMainWindow")
    root.resizable(0, 0)  # ウインドウサイズの変更不可設定
    root.geometry(windowSize)

    # フレームの装飾設定
    cnf = {"bg": "white", "bd": 5, "relief": GROOVE}
    # 戦闘画面のフレーム生成
    battleFrame = Frame(root, cnf, width=785, height=245)
    battleLabel = Label(battleFrame, text="unk", bg="green")

    trueStr = """if __name__ == "__main__":
        print("Hello World!")
        i = input(">>> ")
        for n in range(int(i)):
            print(n)"""
    
    def select_source(ext):
        with closing(sqlite3.connect((dbname))) as conn:
            c = conn.cursor()
            sql = "select * from files where extension like '%{0}' order by complete asc;".format(ext)
            c.execute(sql)
            return c.fetchone()

    def load_source(path):
        f = open(path)
        source = f.read()
        f.close()
        print(source)
        return source

    print(set_language)
    row = select_source(ext_dir[set_language])
    print(row)
    set_language = "Python"
    trueStr = load_source("./debug.py")


    # 正解を表示するフレームの生成
    trueFrame = Frame(root, cnf, width=390, height=310)
    trueStr_buff = StringVar()
    trueStr_buff.set(trueStr)
    trueLabel = Label(trueFrame, textvariable=trueStr_buff)

    # 入力していくフレームの生成
    yourFrame = Frame(root, cnf, width=390, height=310)
    yourStr_buff = StringVar()
    yourStr_buff.set("")
    yourLabel = Label(yourFrame, textvariable=yourStr_buff, bg="red")
    yourLabel.focus_set()
    yourLabel.bind("<Key>", check_input)
    class Dummy_event:
        char=""
    dummy = Dummy_event()
    check_input(dummy)

    # ボタンの装飾の設定
    buttonCnf = {"bg": "white", "bd": 3, "relief": RAISED}
    # 戻るボタンの生成
    backButton = Button(root, buttonCnf, text="もどる", command=back_button)

    resultButton = Button(root, buttonCnf, text="すすむ", command=result_button)

    battleFrame.place(x=10, y=10)
    battleLabel.place(x=10, y=10)

    trueFrame.place(x=10, y=260)
    trueLabel.place(x=10, y=10)

    yourFrame.place(x=405, y=260)
    yourLabel.place(x=10, y=10)
    
    backButton.place(x=700, y=570)
    resultButton.place(x=750, y=570)

    # GUIの表示
    root.mainloop()
    # ---------------------------------


def gameResultWindow():
    # menuWindowに戻るボタン
    def back_button():
        root.destroy()
        menuWindow()

    # ---------------------------------
    # GUI作成
    root = Tk()
    root.title("gameResultWindow")
    root.resizable(0, 0)  # ウインドウサイズの変更不可設定
    root.geometry(windowSize)

    label_title = Label(root, text="ゲームクリア画面", font=("", 70), height=3)
    label_title.pack(anchor="n")

    # ボタン
    button_back = Button(root, text="もどる", font=("", 50), width=6, command=back_button)
    button_back.pack()

    # GUIの表示
    root.mainloop()
    # ---------------------------------


if __name__ == "__main__":
    # 最初に表示される画面
    titleWindow()
