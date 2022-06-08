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
    altura = float(st.session_state.altura)
    peso = float(st.session_state.peso)
    imc = peso/(altura*altura)
    st.write('O imc calculado foi de: ',imc)
    if imc<18.5:
        st.image('abaixoPeso.jpg')
    else:
        if imc>25:
            st.image('acimaPeso.jpg')
        else:
            st.image('imcNormal.jpg')
else:
    st.write('IMC ainda não calculado')

