import math
import tkinter as tk


# ---------------------------- Main GUI ----------------------------
class SteamLevelHelper(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Steam Level Helper")
        self.minsize(400,200)

        self.rowconfigure([0, 1, 2], minsize=50, weight=1)
        self.columnconfigure([0, 1, 2, 3, 4], minsize=50, weight=1)

        # Title
        self.lbl_title = tk.Label(self, text="Steam Level Helper")
        self.lbl_title.grid(row=0, column=2)

        self.lbl_frm = tk.Label(self, text="From:")
        self.lbl_frm.grid(row=1, column=0)

        self.frm_entry = tk.Entry(self, width=10)
        self.frm_entry.grid(row=1, column=1)

        self.lbl_to = tk.Label(self, text="To:")
        self.lbl_to.grid(row=1, column=2)

        self.to_entry = tk.Entry(self, width=10)
        self.to_entry.grid(row=1, column=3)

        self.btn_calc = tk.Button(
                    self,
                    text="calculate",
                    command=self.calxp
                )
        self.btn_calc.grid(row=1, column=4)

        # results
        self.lbl_xp = tk.Label(self, text="XP:")
        self.lbl_xp.grid(row=2, column=1)

        self.lbl_sets = tk.Label(self, text="Sets:")
        self.lbl_sets.grid(row=2, column=3)

    # ----------- Functions -----------
    def levelxp(self, level):
        level = int(level)
        xp = (((math.floor(level / 10) + 1) * 100) * (level % 10))+(pow(math.floor(level / 10), 2) + math.floor(level / 10)) * 500
        return xp


    def fromto(self, fromLvl, toLvl):
        if toLvl > fromLvl:
            fromXp = self.levelxp(fromLvl)
            toXp = self.levelxp(toLvl)
            return toXp - fromXp
        else:
            return 0

    def calxp(self):
        lvlfrm = self.frm_entry.get()
        lvlto = self.to_entry.get()
        ans = self.fromto(lvlfrm, lvlto)
        self.lbl_xp["text"]= "XP: " + str(ans)
        self.lbl_sets["text"] = "Sets: " + str(int(ans/100))

if __name__ == "__main__":
    app = SteamLevelHelper()
    app.mainloop()
