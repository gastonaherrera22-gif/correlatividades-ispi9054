import streamlit as st
import pandas as pd

st.set_page_config(page_title="Correlatividades - ISPI 9054", page_icon="📚", layout="wide")

st.title("📚 Verificador de correlatividades - ISPI Nº 9054")
st.markdown("### Profesorado de Educación Primaria")
st.write("Seleccioná el estado actual de tus materias para verificar automáticamente cuáles tenés habilitadas para cursar y rendir.")

# Inicializar estados en la sesión si no existen
materias = [
    # Primer Año (12)
    "Psicología y Educación", "Pedagogía", "Sociología de la Educación", 
    "Historia Argentina y Latinoamericana", "Movimiento y Cuerpo I", "Taller de Práctica I",
    "Comunicación y Expresión Oral y Escrita", "Resolución de Problemas y Creatividad", 
    "Ciencias Naturales para una Cultura Ciudadana", "Problemáticas de las Ciencias Sociales", 
    "Área Estético Expresiva I", "Problemáticas Contemporáneas de la Educación Primaria I",
    # Segundo Año (10)
    "Didáctica General", "Filosofía de la Educación", "Conocimiento y Educación", 
    "Movimiento y Cuerpo II", "Taller de Práctica II", "Matemática y su Didáctica I", 
    "Ciencias Naturales y su Didáctica I", "Ciencias Sociales y su Didáctica I", 
    "Lengua y su Didáctica", "Sujeto de la Educación Primaria", 
    # Tercer Año (12)
    "Tecnologías de la Información y de la Comunicación", 
    "Historia Social de la Educación y Política Educativa Argentina",
    "Taller de Práctica III", "Matemática y su Didáctica II", "Ciencias Naturales y su Didáctica II", 
    "Ciencias Sociales y su Didáctica II", "Literatura y su Didáctica", "Alfabetización Inicial", 
    "Área Estético Expresiva II", "Problemáticas Contemporáneas de la Educación Primaria II",
