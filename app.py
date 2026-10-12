import streamlit as st

st.title("Your Programming Language Selector")

st.subheader("A website in which, to select the language you want")

st.text("Welcome to your Programming Language Selector. Select your favorite language.")

lang = st.selectbox("Your fav. language:", ["C++", "C#", "Java", "Python", "JavaScript", "Ruby", "Rust", "Go", "Erlang", "Dart", ])

st.write(f"Your chose {lang}. Excellent Choice!")

st.success("Congratulations for your optimal choice!")