import streamlit as st
import random

lista_de_palavras = ["rosa", "vestido", "ken", "moda", "sonho", "princesa"]

st.title("Jogo da Forca da Barbie")

if 'palavra' not in st.session_state:
    st.session_state.palavra = random.choice(lista_de_palavras)
    st.session_state.letras_certas = []
    for letra in st.session_state.palavra:
        if letra.isalpha():
            st.session_state.letras_certas.append(' ~ ')
        else:
            st.session_state.letras_certas.append(letra)
    st.session_state.letras_erradas = []



with st.form(key='lista_form'):
    input_letra = st.text_input(label='Digite uma letra: ')
    submit_button = st.form_submit_button('Verificar letra')


if submit_button:
    if input_letra.isalpha():
        if input_letra not in st.session_state.letras_certas and input_letra not in st.session_state.letras_erradas:
            if input_letra in st.session_state.palavra:
                for i in range(len(st.session_state.palavra)):
                    if st.session_state.palavra[i] == input_letra:
                        st.session_state.letras_certas[i] = input_letra
            else:
                st.session_state.letras_erradas.append(input_letra)

st.write(''.join(st.session_state.letras_certas))

st.write(f"Letras erradas: {', '.join(st.session_state.letras_erradas)}")

if len(st.session_state.letras_erradas) == 6:
    st.write('VOCÊ PERDEU!')
    if st.button('Reiniciar'):
        st.session_state.palavra = random.choice(lista_de_palavras)
        st.session_state.letras_certas = []
        st.session_state.letras_erradas = []

if ''.join(st.session_state.letras_certas) == st.session_state.palavra:
    st.write('VOCÊ GANHOU!')

    if st.button('Reiniciar'):
        st.session_state.palavra = random.choice(lista_de_palavras)
        st.session_state.letras_certas = []
        st.session_state.letras_erradas = []
