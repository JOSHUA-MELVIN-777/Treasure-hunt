import streamlit as st
import random
st.title("Guessing Game")
st.write("Guess a number btw 1 - 15\nYou have 5 attempts")
if "number_to_guess" not in st.session_state:
    st.session_state.number_to_guess=random.randint(1,15)
if "attempts" not in st.session_state:
    st.session_state.attempts=0
if "numbers_tried" not in st.session_state:
    st.session_state.numbers_tried=[]

user_guess=st.number_input("Guess the number",min_value=0,max_value=15,step=1)

if st.button("Submit Guess"):

    st.session_state.attempts += 1
    st.session_state.numbers_tried(user_guess)

    if user_guess < st.session_state.number_to_guess:
        st.write("Too low! Try again.")
    elif user_guess > st.session_state.number_to_guess:
        st.write("Too high! Try again.")
    else:
        st.write("Congratulations! You've guessed the number!")
        st.session_state.number_to_guess = random.randint(1, 15)
        st.session_state.attempts = 0
        st.session_state.numbers_tried = []

    attempts_left = 5 - st.session_state.attempts
    if attempts_left > 0:
        st.write(f"You have {attempts_left} attempts left.")
    else:
        st.write(f"Game over! The number was {st.session_state.number_to_guess}.")
        st.session_state.number_to_guess = random.randint(1, 15)
        st.session_state.attempts = 0
        st.session_state.numbers_tried = []

if st.session_state.numbers_tried:
    st.write("Your guesses:", st.session_state.numbers_tried)
