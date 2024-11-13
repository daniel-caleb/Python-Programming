# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 13:01:03 2024

@author: Daniel-Caleb Cheruiyot
"""
import tkinter as tk

def vote():
    global votes_A, votes_B, votes_C, total_votes
    vote = entry.get().upper()
    if vote == 'A':
        votes_A += 1
    elif vote == 'B':
        votes_B += 1
    elif vote == 'C':
        votes_C += 1
    else:
        result_label.config(text="Invalid vote. Please enter A, B, or C.")
        return
    total_votes += 1
    entry.delete(0, tk.END)

    # Update the result label after each vote
    result_label.config(text=f"A: {votes_A}\nB: {votes_B}\nC: {votes_C}\nTotal Votes: {total_votes}")

def end_voting():
    # No need to update the result label here, as it's already updated after each vote
    entry.config(state='disabled')
    button.config(state='disabled')

# Initialize vote counters
votes_A = 0
votes_B = 0
votes_C = 0
total_votes = 0

# Create the main window
window = tk.Tk()
window.title("E-Voting App")

# Create a label and entry field for voting
label = tk.Label(window, text="Enter your vote (A, B, or C):")
label.pack()
entry = tk.Entry(window)
entry.pack()

# Create a button to submit the vote
button = tk.Button(window, text="Vote", command=vote)
button.pack()

# Create a label to display results
result_label = tk.Label(window)
result_label.pack()

window.mainloop()