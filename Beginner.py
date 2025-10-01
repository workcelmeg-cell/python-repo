import tkinter as tk
import random

root = tk.Tk()
root.title("Fun Dice Roller 🎲")
root.geometry("400x400")

# Dice faces
dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

# Label for dice results
dice_label = tk.Label(root, text="🎲", font=("Helvetica", 60))
dice_label.pack(pady=20)

# Entry to choose number of dice
tk.Label(root, text="How many dice? (1-6)").pack()
dice_count_entry = tk.Entry(root, width=5)
dice_count_entry.insert(0, "2")  # default
dice_count_entry.pack(pady=5)

# History log
history_box = tk.Text(root, height=8, width=35, state="disabled")
history_box.pack(pady=10)


def roll_dice():
    try:
        count = int(dice_count_entry.get())
        if count < 1 or count > 6:
            raise ValueError
    except ValueError:
        dice_label.config(text="❌")
        return

    rolls = [random.choice(dice_faces) for _ in range(count)]
    total = sum(dice_faces.index(r) + 1 for r in rolls)

    # Show result
    dice_label.config(text=" ".join(rolls))

    # Update history
    history_box.config(state="normal")
    history_box.insert("end", f"You rolled: {' '.join(rolls)} (Total = {total})\n")
    history_box.see("end")
    history_box.config(state="disabled")


# Button
roll_button = tk.Button(root, text="Roll Dice", command=roll_dice, font=("Helvetica", 14))
roll_button.pack()

root.mainloop()
