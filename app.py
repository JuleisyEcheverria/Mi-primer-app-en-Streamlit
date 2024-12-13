import streamlit as st

st.title('Mi Primera Aplicación en Streamlit')
st.title('Juleisy Echeverría')
import streamlit as st


# Input Box para la edad
edad = st.number_input('Ingresa tu edad', min_value=0, max_value=100, value=25)

# Text Input para nombres y apellidos
nombre = st.text_input('Ingresa tu nombre completo')

# Slider para seleccionar el mes
mes = st.slider('Selecciona tu mes de nacimiento', min_value=1, max_value=12, value=1)

# Checkbox para aceptar términos
acepta = st.checkbox('Acepto los términos y condiciones')

# Radio Buttons para género
genero = st.radio('Selecciona tu género:', ['Masculino', 'Femenino', 'Otro'])

# Selectbox para país
pais = st.selectbox('Selecciona tu país:', ['Ecuador', 'Colombia', 'Perú', 'Argentina', 'Chile'])

# Botón para enviar información
if st.button('Enviar Información'):
    st.write('¡Gracias por enviar tus datos!')

# Cargar archivo
archivo = st.file_uploader('Sube un archivo')

# Selector de fecha
fecha = st.date_input('Selecciona una fecha')

# Selector de hora
hora = st.time_input('Selecciona una hora')



# Barra lateral con estilo
st.sidebar.title('Configuración Personalizada')

# Widget 1: Mes de nacimiento (Slider)
st.sidebar.header('Mes de Nacimiento')
mes = st.sidebar.slider(
    'Selecciona tu Mes de Nacimiento', 
    min_value=1, 
    max_value=12, 
    value=1
)
st.sidebar.markdown(f'Has seleccionado el mes: **{mes}**')

# Widget 2: País (Selectbox)
st.sidebar.header('Selección de País')
pais = st.sidebar.selectbox(
    'Selecciona tu País', 
    ['Ecuador', 'Colombia', 'Perú', 'Argentina', 'Chile', 'Otro']
)
st.sidebar.markdown(f'País seleccionado: **{pais}**')

# Mostrar resultados en la pantalla principal
st.subheader('Resultados de la Configuración')
st.write(f'Mes de Nacimiento: **{mes}**')
st.write(f'País Seleccionado: **{pais}**')

# Botón de confirmación para interacción adicional
if st.sidebar.button('Confirmar'):
    st.success('¡Tu configuración ha sido guardada correctamente!')