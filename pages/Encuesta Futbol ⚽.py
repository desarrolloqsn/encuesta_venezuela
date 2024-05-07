import streamlit as st
import pandas as pd
import pymongo
import plotly.express as px
import plotly.graph_objects as go




# Conexión a la base de datos MongoDB
uri = 'mongodb+srv://desarrolloqsn:fYMrZhrAQN1ka8ca@etldatastore-deprecated.p9th3.mongodb.net/?retryWrites=true&w=majority'
cliente = pymongo.MongoClient(uri)
base_de_datos = cliente["PRUEBA"]
coleccion = base_de_datos["prueba1"]

st.set_page_config(
    page_title='Encuestas Venezuela',
    page_icon=':bar-chart:',
    layout='wide'
)

with st.sidebar:
    st.header("Navegación")

st.header("Encuestas Fútbol",divider='rainbow')


placeholder = st.empty() #crea un contenedor vacío en la interfaz de Streamlit. Este contenedor se utiliza para actualizar dinámicamente

#######################################
# Visualizaciones
#######################################

def plot_metric(label, value, prefix="", suffix="", show_graph=False, color_graph=""):
    fig = go.Figure()

    fig.add_trace(
        go.Indicator(
            value=value,
            gauge={"axis": {"visible": False}},
            number={
                "prefix": prefix,
                "suffix": suffix,
                "font.size": 100,
            },
            title={
                "text": label,
                "font": {"size": 75},
            },
        )
    )


    st.plotly_chart(fig, use_container_width=True)
    # fig = go.Figure()


def donut_chart(labels, values, title, colors=None, textinfo='percent+label'):
    if colors is None:
        colors = ['#636efa', '#EF553B', '#00cc96', '#ab63fa', '#FFA15A', '#19d3f3', '#FF6692', '#B6E880']
    
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3, textinfo=textinfo)])
    fig.update_traces(marker=dict(colors=colors))
    fig.update_layout(title={'text': title, 'x':0.5, 'xanchor': 'center'})
    
    st.plotly_chart(fig, use_container_width=True)
    # fig = go.Figure()

def bar_chart(x, y, title, colors=None):
    if colors is None:
        colors = ['#636efa'] * len(x)  # Si no se especifican colores, se usa un color por defecto
    
    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color=colors)])
    fig.update_layout(title=title, xaxis_title="X-axis Title", yaxis_title="Y-axis Title")

    st.plotly_chart(fig, use_container_width=True)
    # fig = go.Figure()


def stacked_bar_chart(x, y_data, category_names, title, colors=None):
    if colors is None:
        colors = ['#636efa', '#EF553B', '#00cc96']  # Colores predeterminados para las categorías
    
    fig = go.Figure()
    for i, y in enumerate(y_data):
        fig.add_trace(go.Bar(x=x, y=y, name=category_names[i], marker_color=colors[i]))
    
    fig.update_layout(barmode='stack', title=title, xaxis_title="X-axis Title", yaxis_title="Y-axis Title")
    
    st.plotly_chart(fig, use_container_width=True)
    # fig = go.Figure()

# while True:
# Obtener datos actualizados de MongoDB
data = coleccion.find()
df = pd.DataFrame(list(data))
df = df.drop('_id', axis=1)

# Ordenar datos
p2 = df.groupby(['p2']).agg(
cantidad=('p2','size')
)
p2 = p2.sort_values(by='cantidad', ascending=False) # Ordenar p2 según la cantidad en orden descendente

p3 = df.groupby(['p3']).agg(
cantidad=('p3','size')
)
p2 = p2.sort_values(by='cantidad', ascending=False) # Ordenar p2 según la cantidad en orden descendente

#_____________________________________
#|--------|---------|---------|-------
#|--------|---------|---------|-------
#|--------|---------|---------|-------
#|--------------Copa america----------
#|
#|
#|
#|
#|
#_____________________________________
with placeholder.container(border=True):
    with st.expander("Base de datos"):
        st.dataframe(df)

    pos11, pos12, pos13, pos14= st.columns(4)

    with pos11:
        plot_metric(
            "Encuestados",
            len(df),
            prefix="",
            suffix="",
            show_graph=True,
            color_graph="rgba(255, 43, 43, 0.2)",
        )

    with pos12:
        donut_chart(p3.index,p3['cantidad'],'Distribución por edad')

    with pos13:
        donut_chart(p3.index,p3['cantidad'],'Distribución por edad')

    with pos14:
        donut_chart(p3.index,p3['cantidad'],'Distribución por edad')

    #Divisor Copa América 
    st.markdown("<h1 style='text-align: center; font-size: 36px;'>Copa América</h1>", unsafe_allow_html=True)
    st.markdown("<hr style='border: 1px solid #d3d3d3;'>", unsafe_allow_html=True)  # Línea divisoria
    st.markdown("<style>div.stMarkdown {margin-top: -10px;}</style>", unsafe_allow_html=True)  # Ajuste de margen superior

    pos21, pos22, pos23, pos24= st.columns((0.4,0.2,0.2,0.2))
    with pos21:

        bar_chart(p2.index, p2['cantidad'], 'Cantidad por rango de edad', colors=None)

    with pos22:
        donut_chart(p3.index,p3['cantidad'],'Distribución por edad')

    with pos23:
        donut_chart(p3.index,p3['cantidad'],'Distribución por edad')

    with pos24:
        donut_chart(p3.index,p3['cantidad'],'Distribución por edad')

    pos31, pos32, pos33= st.columns((0.5,0.25,0.25))

    with pos31:
        bar_chart(p2.index, p2['cantidad'], 'Cantidad por rango de edad', colors=None)
        bar_chart(p2.index, p2['cantidad'], 'Cantidad por rango de edad', colors=None)

    with pos32:
        donut_chart(p3.index,p3['cantidad'],'Distribución por edad')
        bar_chart(p2.index, p2['cantidad'], 'Cantidad por rango de edad', colors=None)


    with pos33:
        donut_chart(p3.index,p3['cantidad'],'Distribución por edad')


    bar_chart(p2.index, p2['cantidad'], 'Cantidad por rango de edad', colors=None)

    # stacked_bar_chart()

    #Divisor Champion 
    st.markdown("<h1 style='text-align: center; font-size: 36px;'>Eurocopa</h1>", unsafe_allow_html=True)
    st.markdown("<hr style='border: 1px solid #d3d3d3;'>", unsafe_allow_html=True)  # Línea divisoria
    st.markdown("<style>div.stMarkdown {margin-top: -10px;}</style>", unsafe_allow_html=True)  # Ajuste de margen superior

    # Definir el número de columnas y la relación de anchos
    columnas = st.columns(5)

