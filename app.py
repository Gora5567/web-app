
import streamlit as st
import random

st.set_page_config(page_title="моя веб-страница", page_icon="🚀", layout="wide")

st.title("добро пожаловать на мою веб-страницу 🙃")

tab1, tab2, tab3 = st.tabs(["про меня", "мой инструмент", "🔗 полезные ссылки"])

with tab1:

    st.header("узнай обо мне")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("https://cdn.britannica.com/36/147936-050-8E84B614/Dwayne-Johnson.jpg", width=200)

    with col2:
        st.subheader("привет, я будущий python разработчик")
        st.write("я учусь в академии it step")

with tab2:

    st.header("🎲 игра — угадай число")

    if "secret_number" not in st.session_state:
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.session_state.hint = ""

    st.subheader("угадай число от 1 до 100")

    user_guess = st.number_input(
        "твой вариант",
        min_value=1,
        max_value=100,
        step=1
    )

    if st.button("проверить"):
        if not st.session_state.game_over:
            st.session_state.attempts += 1

            if user_guess < st.session_state.secret_number:
                st.session_state.hint = "📈 загаданное число больше"

            elif user_guess > st.session_state.secret_number:
                st.session_state.hint = "📉 загаданное число меньше"

            else:
                st.session_state.hint = f"🎉 поздравляем! ты угадал число за {st.session_state.attempts} попыток"
                st.session_state.game_over = True

    if st.session_state.hint:
        if st.session_state.game_over:
            st.success(st.session_state.hint)
        else:
            st.info(st.session_state.hint)

    st.write(f"количество попыток: {st.session_state.attempts}")

    if st.button("сыграть снова"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.session_state.hint = ""
        st.rerun()

with tab3:

    st.header("🔗 полезные ссылки")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("[📚 википедия](https://www.wikipedia.org)")
        st.markdown("[💻 w3schools](https://www.w3schools.com)")

    with col2:
        st.markdown("[🎮 coolmath games](https://www.coolmathgames.com)")
        st.markdown("[🧠 quizlet](https://quizlet.com)")
