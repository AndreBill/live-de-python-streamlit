import streamlit as st
import time
def main():
    st.title('Este é o meu titulo')
    st.write('Texto simples')
    input_text = st.text_input("Digite um texto aqui")
    if input_text:
        st.write("Você digitou: ", input_text)
        
        st.header("Seleção")
        selected_option = st.selectbox("Selecione uma opção", [
                                        "Opção 1", "Opção 2", "Opção 3"])
        if selected_option:
            st.write("Opção selecionada: ", selected_option)
            
        st.header("Slider")
        slider_value = st.slider("Escolha um valor", 0, 100, 50)
        st.write("Valor escolhido: ", slider_value)
        
    
    


main()