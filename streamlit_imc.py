# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 18:29:21 2022

@author: mirkos
"""

#programa IMC streamlit

import streamlit as st

altura=1
peso=1
st.title('IMC calculator:')

st.text_input("Digite sua altura (em metros)",key='altura')
st.text_input('Digite seu peso: (em kg)',key='peso')

if st.button('Calcular IMC'):
    altura = float(st.session_state.altura.replace(',','.'))
    peso = float(st.session_state.peso.replace(',','.'))
    imc = peso/(altura*altura)
    st.write('O imc calculado foi de: ',imc)
    if imc<18.5:
        st.image('abaixoPeso.jpg')
        st.write('Abaixo do peso.')
    else:
        if imc>25:
            st.image('acimaPeso.jpg')
            st.write('Acima do peso.')
        else:
            st.image('imcNormal.jpg')
            st.write('No peso ideal.')
else:
    st.write('IMC ainda não calculado')

