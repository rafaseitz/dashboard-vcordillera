import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Centro de Monitoreo V Cordillera",
    layout="wide"
)

st.title("🚨 Centro de Monitoreo Zona V Cordillera")

df = pd.read_csv("eds.csv")

operativas = len(df[df["ESTADO"]=="Operativa"])
restriccion = len(df[df["ESTADO"]=="Operativa con restricción"])
cerradas = len(df[df["ESTADO"]=="Cerrada"])

c1,c2,c3 = st.columns(3)

c1.metric("Operativas", operativas)
c2.metric("Restricción", restriccion)
c3.metric("Cerradas", cerradas)

st.divider()

st.subheader("Estado Estaciones")

st.dataframe(df)

st.divider()

st.subheader("Incidentes Activos")

for _, row in df.iterrows():

    if row["ESTADO"] == "Cerrada":
        st.error(
            f"FILE {row['FILE']} - {row['COMUNA']} - {row['OBSERVACION']}"
        )

    elif row["ESTADO"] == "Operativa con restricción":
        st.warning(
            f"FILE {row['FILE']} - {row['COMUNA']} - {row['OBSERVACION']}"
        )
