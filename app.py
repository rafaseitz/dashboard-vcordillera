import streamlit as st

st.set_page_config(
    page_title="Dashboard V Cordillera",
    layout="wide"
)

st.title("🚨 Centro de Monitoreo Zona V Cordillera")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Operativas", "23")

with col2:
    st.metric("Restricción", "1")

with col3:
    st.metric("Cerradas", "1")

st.divider()

st.subheader("Incidentes Activos")

st.error("🔴 FILE 446 - Olmué - Corte eléctrico comunal")

st.warning("🟡 FILE 639 - Limache - Calle cerrada")

st.success("🟢 FILE 54 - Los Andes - Problema eléctrico en marquesina")
