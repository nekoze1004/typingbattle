from tkinter import *
from tkinter import ttk

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
    label_title = Label(root, text="タイピングバトル", font=("",70), height=3)
    label_title.pack(anchor="n")

    # タイトル画面のユーザ名
    label_1 = Label(root, text="ユーザ名", font=("", 30), height=3)
    entry_1 = Entry(root, width=30,  font=("", 30))
    entry_1.insert(END,"ユーザ名を入力してください")

    label_1.pack(anchor="sw", padx="30")
    entry_1.pack()

    # タイトル画面のボタン
    button_start = Button(root,text="はじめる", font=("", 50), width=6, command=start_button)
    button_start.pack(side="left", padx="30")

    button_finish = Button(root,text="おわる", font=("", 50), width=6, command=quit_button)
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
    label_title = Label(root, text="メニュー画面", font=("",70), height=3)
    #label_title.pack(anchor="n")
    label_title.grid(columnspan=3)

    # コンボボックス
    # コンボボックスの作成(rootに配置,リストの値を編集不可(readonly)に設定)
    combo = ttk.Combobox(root, state='readonly', width=30)
    # リストの値を設定
    combo["values"] = ("Ruby","Python","Swift")
    # デフォルトの値を食費(index=0)に設定
    combo.current(0)
    # コンボボックスの配置
    #combo.pack(pady=10)
    combo.grid(row=1, column=0, columnspan=3)

    # ボタン
    button_stage = Button(root,text="ゲームスタート", font=("", 50), command=start_game)
    button_gallery = Button(root,text="ギャラリー", font=("", 50), command=select_gallery)
    button_setting = Button(root,text="設定", font=("", 50), command=select_setting)
    button_back = Button(root,text="もどる", font=("", 50), command=back_button)
    """
    button_stage.pack(fill="x", padx=200, pady=4)
    button_gallery.pack(fill="x", side="left", padx=30, pady=4)
    button_setting.pack(fill="x", side="top", padx=30, pady=4)
    button_back.pack(fill="x", side="right", padx=30, pady=4)
    """
    button_stage.grid(row=2, column=0, columnspan=3, padx=50, pady=0, sticky=W+E)
    button_gallery.grid(row=3, column=0, padx=50, pady=10, sticky=W+E)
    button_setting.grid(row=3, column=1, padx=10, pady=10, sticky=W+E)
    button_back.grid(row=3, column=2, padx=50, pady=10, sticky=W+E)

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

    label_title = Label(root, text="ギャラリー画面", font=("",70), height=3)
    label_title.pack(anchor="n")

    # ボタン
    button_back = Button(root,text="もどる", font=("", 50), width=6, command=back_button)
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

    label_title = Label(root, text="設定画面", font=("",70), height=3)
    label_title.pack(anchor="n")

    # ボタン
    button_back = Button(root,text="もどる", font=("", 50), width=6, command=back_button)
    button_back.pack()

    # GUIの表示
    root.mainloop()
    # ---------------------------------

def stageSelectWindow():

    # menuWindowに戻るボタン
    def back_button():
        root.destroy()
        menuWindow()

    # ---------------------------------
    # GUI作成
    root = Tk()
    root.title("stageSelectWindow")
    root.geometry("800x600+0+0")

    label_title = Label(root, text="ステージ選択画面", font=("",70), height=3)
    label_title.pack(anchor="n")

    # ボタン
    button_back = Button(root,text="もどる", font=("", 50), width=6, command=back_button)
    button_back.pack()

    # GUIの表示
    root.mainloop()
    # ---------------------------------

def gameMainWindow():

    # ---------------------------------
    # GUI作成
    root = Tk()
    root.title("settingWindow")
    root.geometry("800x600+0+0")

    label_title = Label(root, text="設定画面", font=("",70), height=3)
    label_title.pack(anchor="n")

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

    label_title = Label(root, text="ゲームクリア画面", font=("",70), height=3)
    label_title.pack(anchor="n")

    # ボタン
    button_back = Button(root,text="もどる", font=("", 50), width=6, command=back_button)
    button_back.pack()

    # GUIの表示
    root.mainloop()
    # ---------------------------------

# 最初に表示される画面
titleWindow()
