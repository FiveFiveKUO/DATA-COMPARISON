import tkinter as tk
import subprocess

class MyFrame(tk.LabelFrame):

    def __init__(self, root):
        tk.LabelFrame.__init__(self, root, text="資料比對工具")
        # # 標籤: Label
        # self.l1 = tk.Label(self, text="DATA 1:")
        # self.l1.pack(expand=True, fill=tk.BOTH, pady=10, padx=5)
        # # 單行輸入: Entry
        # self.e1 = tk.Entry(self)
        # self.e1.pack(expand=True, fill=tk.BOTH, pady=10, padx=5)
        # 按紐: Button
        # self.b1 = tk.Button(self, text="匯入", command=self.DATA)
        # # tk.X
        # self.b1.pack(expand=True, fill=tk.BOTH, pady=10, padx=5)
        # # 標籤: Label
        # self.l2 = tk.Label(self, text="DATA 2:")
        # self.l2.pack(expand=True, fill=tk.BOTH, pady=10, padx=5)
        # # 單行輸入: Entry
        # self.e2 = tk.Entry(self)
        # self.e2.pack(expand=True, fill=tk.BOTH, pady=10, padx=5)
        # # 按紐: Button
        # self.b1 = tk.Button(self, text="匯入", command=self.DATA)
        # # tk.X
        # self.b1.pack(expand=True, fill=tk.BOTH, pady=10, padx=5)
        # # 標籤: Label
        # self.l3 = tk.Label(self, text="輸出檔案位置:")
        # self.l3.pack(expand=True, fill=tk.BOTH, pady=10, padx=5)
        # # 單行輸入: Entry
        # self.e3 = tk.Entry(self)
        # self.e3.pack(expand=True, fill=tk.BOTH, pady=10, padx=5)
        # 按紐: Button
        self.b1 = tk.Button(self, text="執行", command=self.DATA)
        # tk.X
        self.b1.pack(expand=True, fill=tk.BOTH, pady=10, padx=5)
        self.result = tk.Label(self, text="按上面按鈕進行資料比對...")
        self.result.pack(expand=True, fill=tk.BOTH, pady=10, padx=5)

    def DATA(self):
        DATA1 = open("DATA1.txt").read().split()
        DATA2 = open("DATA2.txt").read().split()

        cnt = 0
        for i, policynum in enumerate(DATA2):
            if policynum in DATA1:
                cnt = cnt + 1
                print("第", i + 1, "張POLICY", policynum, "!")

        print("相同POLICY共", cnt, "張")
        # 第二時間
        self.result["text"] = (("相同POLICY共"), cnt, ("張"))
        with open("FINALDATA.txt", "w") as f1, open("err.txt", "w") as f2:
            result = subprocess.run(stdout=f1, stderr=f2)
            print(result)

window = tk.Tk()
window.geometry("500x500+100+100")
f1 = MyFrame(window)
f1.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=20, pady=20)
window.mainloop()





