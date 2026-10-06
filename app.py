import streamlit as st
import pandas as pd

st.set_page_config(page_title="Correlatividades - ISPI 9054", page_icon="📚", layout="wide")

st.title("📚 Validador de Correlatividades - ISPI Nº 9054")
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
    "Espacio de Definición Institucional I", "Espacio de Definición Institucional II", 
    # Cuarto Año (3)
    "Ética, Trabajo Docente, Derechos Humanos y Ciudadanía",
    "Taller de Práctica IV", "Sexualidad Humana y Educación"
]

if 'estados' not in st.session_state:
    st.session_state.estados = {m: "Pendiente" for m in materias}

# Sidebar para control global
st.sidebar.header("Panel de Control")
if st.sidebar.button("Marcar todo como Pendiente"):
    for m in materias:
        st.session_state.estados[m] = "Pendiente"
    st.rerun()

def get_e(m):
    return st.session_state.estados.get(m, "Pendiente")

def evaluar_materias(m):
    cursar = "Faltan correlativas"
    rendir = "Faltan correlativas"
    
    # --- PRIMER AÑO ---
    if m in materias[:12]:
        cursar = "Sin correlativas"
        rendir = "Sin correlativas"

    # --- SEGUNDO AÑO ---
    elif m == "Didáctica General":
        cursar = "Sin correlativas"
        rendir = "Habilitada" if get_e("Pedagogía") == "Aprobada" and get_e("Psicología y Educación") == "Aprobada" else "Faltan correlativas"
    elif m == "Filosofía de la Educación":
        cursar = "Sin correlativas"
        rendir = "Sin correlativas"
    elif m == "Conocimiento y Educación":
        cursar = "Sin correlativas"
        rendir = "Sin correlativas"
    elif m == "Movimiento y Cuerpo II":
        cursar = "Sin correlativas"
        rendir = "Habilitada" if get_e("Movimiento y Cuerpo I") == "Aprobada" else "Faltan correlativas"
    elif m == "Taller de Práctica II":
        talleres_esp = sum([1 for x in ["Comunicación y Expresión Oral y Escrita", "Resolución de Problemas y Creatividad", 
                                       "Ciencias Naturales para una Cultura Ciudadana", "Problemáticas de las Ciencias Sociales", 
                                       "Área Estético Expresiva I", "Problemáticas Contemporáneas de la Educación Primaria I"] if get_e(x) == "Aprobada"])
        cond_cursar = (get_e("Taller de Práctica I") == "Aprobada" and 
                       get_e("Pedagogía") in ["Regular", "Aprobada"] and 
                       get_e("Psicología y Educación") in ["Regular", "Aprobada"] and 
                       talleres_esp >= 3)
        cursar = "Habilitada" if cond_cursar else "Faltan correlativas"
        rendir = "Sin correlativas"
    elif m == "Matemática y su Didáctica I":
        cursar = "Sin correlativas"
        rendir = "Habilitada" if get_e("Resolución de Problemas y Creatividad") == "Aprobada" else "Faltan correlativas"
    elif m == "Ciencias Naturales y su Didáctica I":
        cursar = "Sin correlativas"
        rendir = "Habilitada" if get_e("Ciencias Naturales para una Cultura Ciudadana") == "Aprobada" else "Faltan correlativas"
    elif m == "Ciencias Sociales y su Didáctica I":
        cursar = "Sin correlativas"
        rendir = "Habilitada" if get_e("Problemáticas de las Ciencias Sociales") == "Aprobada" else "Faltan correlativas"
    elif m == "Lengua y su Didáctica":
        cursar = "Sin correlativas"
        rendir = "Habilitada" if get_e("Comunicación y Expresión Oral y Escrita") == "Aprobada" else "Faltan correlativas"
    elif m == "Sujeto de la Educación Primaria":
        cursar = "Sin correlativas"
        rendir = "Habilitada" if get_e("Psicología y Educación") == "Aprobada" else "Faltan correlativas"

    # --- TERCER AÑO ---
    elif m == "Tecnologías de la Información y de la Comunicación":
        cursar = "Sin correlativas"
        rendir = "Sin correlativas"
    elif m == "Historia Social de la Educación y Política Educativa Argentina":
        cursar = "Sin correlativas"
        rendir = "Habilitada" if get_e("Historia Argentina y Latinoamericana") == "Aprobada" and get_e("Sociología de la Educación") == "Aprobada" else "Faltan correlativas"
    elif m == "Taller de Práctica III":
        aprobadas_1ro = sum([1 for x in materias[:12] if get_e(x) == "Aprobada"])
        cond_cursar = (aprobadas_1ro == 12 and get_e("Taller de Práctica II") == "Aprobada" and
                       get_e("Didáctica General") in ["Regular", "Aprobada"] and
                       get_e("Matemática y su Didáctica I") in ["Regular", "Aprobada"] and
                       get_e("Ciencias Sociales y su Didáctica I") in ["Regular", "Aprobada"] and
                       get_e("Ciencias Naturales y su Didáctica I") in ["Regular", "Aprobada"] and
                       get_e("Lengua y su Didáctica") in ["Regular", "Aprobada"] and
                       get_e("Sujeto de la Educación Primaria") in ["Regular", "Aprobada"] and
                       get_e("Conocimiento y Educación") in ["Regular", "Aprobada"])
        cursar = "Habilitada" if cond_cursar else "Faltan correlativas"
        rendir = "Sin correlativas"
    elif m == "Matemática y su Didáctica II":
        cursar = "Sin correlativas"
        rendir = "Habilitada" if get_e("Matemática y su Didáctica I") == "Aprobada" else "Faltan correlativas"
    elif m == "Ciencias Naturales y su Didáctica II":
        cursar = "Sin correlativas"
        rendir = "Habilitada" if get_e("Ciencias Naturales y su Didáctica I") == "Aprobada" else "Faltan correlativas"
    elif m == "Ciencias Sociales y su Didáctica II":
        cursar = "Sin correlativas"
        rendir = "Habilitada" if get_e("Ciencias Sociales y su Didáctica I") == "Aprobada" else "Faltan correlativas"
    elif m == "Literatura y su Didáctica":
        cursar = "Sin correlativas"
        rendir = "Habilitada" if get_e("Lengua y su Didáctica") == "Aprobada" else "Faltan correlativas"
    elif m == "Alfabetización Inicial":
        cursar = "Sin correlativas"
        rendir = "Habilitada" if get_e("Lengua y su Didáctica") == "Aprobada" and get_e("Sujeto de la Educación Primaria") == "Aprobada" else "Faltan correlativas"
    elif m == "Área Estético Expresiva II":
        cursar = "Sin correlativas"
        rendir = "Habilitada" if get_e("Área Estético Expresiva I") == "Aprobada" else "Faltan correlativas"
    elif m == "Problemáticas Contemporáneas de la Educación Primaria II":
        cursar = "Sin correlativas"
        rendir = "Habilitada" if get_e("Problemáticas Contemporáneas de la Educación Primaria I") == "Aprobada" else "Faltan correlativas"
    elif m in ["Espacio de Definición Institucional I", "Espacio de Definición Institucional II"]:
        cursar = "Sin correlativas"
        rendir = "Sin correlativas"

    # --- CUARTO AÑO ---
    elif m == "Ética, Trabajo Docente, Derechos Humanos y Ciudadanía":
        cursar = "Sin correlativas"
        rendir = "Habilitada" if get_e("Filosofía de la Educación") == "Aprobada" and get_e("Historia Social de la Educación y Política Educativa Argentina") == "Aprobada" else "Faltan correlativas"
    elif m == "Taller de Práctica IV":
        aprobadas_2do = sum([1 for x in materias[12:22] if get_e(x) == "Aprobada"])
        cond_cursar = (aprobadas_2do == 10 and get_e("Taller de Práctica III") == "Aprobada" and
                       get_e("Matemática y su Didáctica II") in ["Regular", "Aprobada"] and
                       get_e("Ciencias Sociales y su Didáctica II") in ["Regular", "Aprobada"] and
                       get_e("Ciencias Naturales y su Didáctica II") in ["Regular", "Aprobada"] and
                       get_e("Literatura y su Didáctica") in ["Regular", "Aprobada"] and
                       get_e("Alfabetización Inicial") in ["Regular", "Aprobada"])
        cursar = "Habilitada" if cond_cursar else "Faltan correlativas"
        rendir = "Sin correlativas"
    elif m == "Sexualidad Humana y Educación":
        cursar = "Sin correlativas"
        rendir = "Sin correlativas"

    return cursar, rendir

# --- INTERFAZ VISUAL ---
st.markdown("### Seleccioná tus materias:")
tab1, tab2, tab3, tab4 = st.tabs(["Primer Año", "Segundo Año", "Tercer Año", "Cuarto Año"])

def renderizar_materias(lista_materias):
    for m in lista_materias:
        col1, col2, col3 = st.columns([3, 2, 3])
        col1.write(f"**{m}**")
        st.session_state.estados[m] = col2.selectbox("Estado", ["Pendiente", "Regular", "Aprobada"], key=f"sel_{m}", index=["Pendiente", "Regular", "Aprobada"].index(get_e(m)), label_visibility="collapsed")
        c, r = evaluar_materias(m)
        
        # Colorear texto
        color_c = "green" if c in ["Habilitada", "Sin correlativas"] else "red"
        color_r = "green" if r in ["Habilitada", "Sin correlativas"] else "red"
        
        col3.markdown(f"<span style='font-size:0.9em'>Cursar: <strong style='color:{color_c}'>{c}</strong> | Rendir: <strong style='color:{color_r}'>{r}</strong></span>", unsafe_allow_html=True)
        st.divider()

with tab1:
    renderizar_materias(materias[:12])
with tab2:
    renderizar_materias(materias[12:22])
with tab3:
    renderizar_materias(materias[22:34])
with tab4:
    renderizar_materias(materias[34:])
