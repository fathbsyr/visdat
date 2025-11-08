import streamlit as st
import graphviz as graph

st.title("GRAPH CHART")
st.header("Praktikum 2 Visualisasi Data")
st.subheader("Bagian 5: Graph Chart")
st.markdown("""
Kelompok 14:
1. Fatih Mubasyir (0110222186)
2. Hisyam Wildan Alfath (0110222206) 
3. Dean Pramona (0110222163)
""")

st.subheader("Graph Chart Biasa")
st.graphviz_chart("""
    digraph {
        "Training Data" -> "ML Algorithm"
        "ML Algorithm" -> "Model"
        "Model" -> "Results Forecasting"
        "New Data" -> "Model"                                                 
    }
""")

st.subheader("Graph dengan Konspe Edge")
graph = graph.Digraph()
graph.edge("Training Data", "ML Algorithm")
graph.edge("ML Algorithm", "Model")
graph.edge("Model", "Results Forecasting")
graph.edge("New Data", "Model")
st.graphviz_chart(graph)
