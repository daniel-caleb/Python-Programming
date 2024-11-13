# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 13:01:03 2024

@author: Meshewa
"""

import tkinter as tk
from tkinter import messagebox

# Initialize the root window
root = tk.Tk()
root.title("E-Voting App")

# Initialize vote counters
votesA = 0
votesB = 0
votesC = 0
totalVotes = 0

# Function to handle voting for each candidate
def vote(candidate):
    global votesA, votesB, votesC, totalVotes
    if candidate == 'A':
        votesA += 1
    elif candidate == 'B':
        votesB += 1
    elif candidate == 'C':
        votesC += 1
    totalVotes += 1
    messagebox.showinfo("Vote Cast", f"You have voted for Candidate {candidate}. Thank you!")
    
# Function to display results
def display_results():
    result_message = (
        f"Results:\n\n"
        f"Votes for Candidate A: {votesA}\n"
        f"Votes for Candidate B: {votesB}\n"
        f"Votes for Candidate C: {votesC}\n\n"
        f"Total votes cast: {totalVotes}"
    )
    messagebox.showinfo("Voting Results", result_message)

# Create GUI layout
instructions_label = tk.Label(root, text="Please vote for a candidate below:")
instructions_label.pack(pady=10)

# Create buttons for each candidate
buttonA = tk.Button(root, text="Vote for Candidate A", command=lambda: vote('A'), width=20)
buttonA.pack(pady=5)

buttonB = tk.Button(root, text="Vote for Candidate B", command=lambda: vote('B'), width=20)
buttonB.pack(pady=5)

buttonC = tk.Button(root, text="Vote for Candidate C", command=lambda: vote('C'), width=20)
buttonC.pack(pady=5)

# Button to end voting and display results
end_button = tk.Button(root, text="END Voting and Show Results", command=display_results, width=25, bg="red", fg="white")
end_button.pack(pady=15)

# Run the application
root.mainloop()
