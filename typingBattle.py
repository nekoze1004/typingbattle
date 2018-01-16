from tkinter import *
from tkinter import ttk
import os


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
    root.geometry("800x600+0+0")

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
        print(valueCombo)
        root.destroy()
        stageSelectWindow()

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
    root.geometry("800x600+0+0")
    label_title = Label(root, text="メニュー画面", font=("", 70), height=3)
    # label_title.pack(anchor="n")
    label_title.grid(columnspan=3)

    # コンボボックス
    # コンボボックスの作成(rootに配置,リストの値を編集不可(readonly)に設定)
    combo = ttk.Combobox(root, state='readonly', width=30)
    # リストの値を設定
    combo["values"] = ("Ruby", "Python", "Swift")
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
    root.geometry("800x600+0+0")

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
    root.geometry("800x600+0+0")

    label_title = Label(root, text="設定画面", font=("", 70), height=3)
    label_title.pack(anchor="n")

    # ボタン
    button_back = Button(root, text="もどる", font=("", 50), width=6, command=back_button)
    button_back.pack()

    # GUIの表示
    root.mainloop()
    # ---------------------------------


def stageSelectWindow():
    # menuWindowに戻るボタン
    def back_button():
        root.destroy()
        menuWindow()

    # gameMainWindowへ進むボタン
    def start_button():
        root.destroy()
        gameMainWindow()

    # ---------------------------------
    # GUI作成
    root = Tk()
    root.title("stageSelectWindow")
    root.geometry("800x600+0+0")

    label_title = Label(root, text="ステージ選択画面", font=("", 70), height=3)
    label_title.pack(anchor="n")

    # ボタン
    button_back = Button(root, text="もどる", font=("", 50), width=6, command=back_button)
    button_back.pack()

    button_start = Button(root, text="ゲームスタート", font=("", 50), width=6, command=start_button)
    button_start.pack()

    # GUIの表示
    root.mainloop()
    # ---------------------------------

def gameMainWindow():
    # menuWindowに戻るボタン
    def back_button():
        root.destroy()
        menuWindow()

    # 入力時に正しいかどうか判定する
    # 入力した時に何かしたいときは個々に書く
    def check_input(event):
        print("pressed", repr(event.char))
        true_text = trueStr_buff.get()
        your_text = yourStr_buff.get()
        your_over = len(your_text)
        if(true_text[your_over] == os.linesep):
            # 改行があったときは飛ばす
            your_over += 1
            your_text += os.linesep
        if(true_text[your_over] == event.char):
            your_text += event.char
            yourStr_buff.set(your_text)

    # ---------------------------------
    # GUI作成
    root = Tk()
    root.title("settingWindow")
    root.geometry("800x600+0+0")

    """label_title = Label(root, text="設定画面", font=("",70), height=3)
    label_title.pack(anchor="n")"""

    # フレームの装飾設定
    cnf = {"bg": "white", "bd": 5, "relief": GROOVE}
    # 戦闘画面のフレーム生成
    battleFrame = Frame(root, cnf, width=785, height=245)
    battleLabel = Label(battleFrame, text="unk", bg="green")

    trueStr = """if __name__ == "__main__":
        print("Hello World!")
        i = input(">>> ")
        for n in range(int(i)):
            print(n)
    """

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

    # ボタンの装飾の設定
    buttonCnf = {"bg": "white", "bd": 3, "relief": RAISED}
    # 戻るボタンの生成
    backButton = Button(root, buttonCnf, text="もどる", command=back_button)

    battleFrame.place(x=10, y=10)
    battleLabel.place(x=10, y=10)

    trueFrame.place(x=10, y=260)
    trueLabel.place(x=10, y=10)

    yourFrame.place(x=405, y=260)
    yourLabel.place(x=20, y=35)

    backButton.place(x=700, y=570)

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
    root.geometry("800x600+0+0")

    label_title = Label(root, text="ゲームクリア画面", font=("", 70), height=3)
    label_title.pack(anchor="n")

    # ボタン
    button_back = Button(root, text="もどる", font=("", 50), width=6, command=back_button)
    button_back.pack()

    # GUIの表示
    root.mainloop()
    # ---------------------------------


# 最初に表示される画面
titleWindow()
