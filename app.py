import folium
from streamlit_folium import st_folium
import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium

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

c1.metric("EDS Totales", total)
c2.metric("Operativas", operativas)
c3.metric("Restricción", restriccion)
c4.metric("Cerradas", cerradas)

st.metric(
    "Disponibilidad Operacional",
    f"{disponibilidad}%"
)

st.divider()

st.subheader("🚨 Incidentes Activos")

incidentes = df[df["ESTADO"] != "Operativa"]

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

comuna = st.selectbox(
    "Filtrar comuna",
    ["Todas"] + sorted(df["COMUNA"].unique())
)

if comuna != "Todas":
    df = df[df["COMUNA"] == comuna]

st.dataframe(
    df,
    use_container_width=True
)

st.divider()

st.subheader("📈 Estado Operacional")

resumen = (
    df.groupby("ESTADO")
    .size()
    .reset_index(name="Cantidad")
)

fig = px.pie(
    resumen,
    names="ESTADO",
    values="Cantidad"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
