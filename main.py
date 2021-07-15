import funcs
import tkinter as tk

def calxp():
    lvlfrm = frm_entry.get()
    lvlto = to_entry.get()
    ans = funcs.fromto(lvlfrm, lvlto)
    lbl_xp["text"]= "XP: " + str(ans)
    lbl_sets["text"] = "Sets: " + str(int(ans/100))

window = tk.Tk()
window.title("Steam Level Helper")

window.rowconfigure([0, 1, 2], minsize=50, weight=1)
window.columnconfigure([0, 1, 2, 3, 4], minsize=50, weight=1)

# Title
lbl_title = tk.Label(text="Steam Level Helper")
lbl_title.grid(row=0, column=2)

# to - from - calculate
lbl_frm = tk.Label(text="From:")
lbl_frm.grid(row=1, column=0)

frm_entry = tk.Entry(width=10)
frm_entry.grid(row=1, column=1)

lbl_to = tk.Label(text="To:")
lbl_to.grid(row=1, column=2)

to_entry = tk.Entry(width=10)
to_entry.grid(row=1, column=3)

btn_calc = tk.Button(
            text="calculate",
            command=calxp
        )
btn_calc.grid(row=1, column=4)

# results
lbl_xp = tk.Label(text="XP:")
lbl_xp.grid(row=2, column=1)

lbl_sets = tk.Label(text="Sets:")
lbl_sets.grid(row=2, column=3)

window.mainloop()
