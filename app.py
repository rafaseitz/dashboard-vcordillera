import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Centro de Monitoreo V Cordillera",
    page_icon="⛽",
    layout="wide"
)

df = pd.read_csv("eds.csv")

operativas = len(df[df["ESTADO"] == "Operativa"])
restriccion = len(df[df["ESTADO"] == "Operativa con restricción"])
cerradas = len(df[df["ESTADO"] == "Cerrada"])
total = len(df)

disponibilidad = round(
    ((operativas + restriccion) / total) * 100,
    1
)

st.title("🚨 Centro de Monitoreo Zona V Cordillera")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("EDS Totales", total)

with c2:
    st.metric("Operativas", operativas)

with c3:
    st.metric("Restricción", restriccion)

with c4:
    st.metric("Cerradas", cerradas)

st.metric(
    "Disponibilidad Operacional",
    f"{disponibilidad}%"
)

st.divider()

st.subheader("🚨 Incidentes Activos")

incidentes = df[df["ESTADO"] != "Operativa"]

if len(incidentes) == 0:
    st.success("No existen incidentes reportados")
else:

    for _, row in incidentes.iterrows():

        if row["ESTADO"] == "Cerrada":
            st.error(
                f"FILE {row['FILE']} | {row['COMUNA']} | {row['OBSERVACION']}"
            )

        elif row["ESTADO"] == "Operativa con restricción":
            st.warning(
                f"FILE {row['FILE']} | {row['COMUNA']} | {row['OBSERVACION']}"
            )

st.divider()

st.subheader("📊 Estado de Estaciones")

filtro = st.selectbox(
    "Comuna",
    ["Todas"] + sorted(df["COMUNA"].unique().tolist())
)

if filtro != "Todas":
    df = df[df["COMUNA"] == filtro]

st.dataframe(
    df,
    use_container_width=True
)
