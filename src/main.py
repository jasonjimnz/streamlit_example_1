import streamlit as st
import pandas as pd


DATASET_DIR = './dataset.zip'  # Ruta del dataset
st.set_page_config(
    page_title="Streamlit App"  # <title> de nuestra aplicación
)


# Función para obtener el dataframe de una ruta o URL
@st.cache_data
def load_dataset(dataset_url: str) -> pd.DataFrame:
    data = pd.read_csv(dataset_url, sep=',', compression='zip')
    return data


# Cabecera de la aplicación
st.write("# Hello Streamlit!")

# Carga del Dataset y
data_set_loading_state = st.text('Cargando dataset...')
ds = load_dataset(DATASET_DIR)
data_set_loading_state.text('Dataset cargado correctamente!')

st.write('### Raw data de nuestro Dataset')

st.dataframe(ds.head())

# Obtenemos la lista de especies y quitamos duplicados
species = ds['species'].unique()

# Creamos un dataframe con los datos que nos gustaría mostrar
# en una gráfica a partir del original
ds2 = pd.DataFrame(
    data={
        "species": species,
        "avg_length": [ds[ds['species'] == sp]['length'].mean() for sp in species],
        "avg_weight": [ds[ds['species'] == sp]['weight'].mean() for sp in species],
        "avg_wl_ratio": [ds[ds['species'] == sp]['w_l_ratio'].mean() for sp in species]
    }
)

# Mostramos el contenido de nuestro nuevo dataframe
st.write('### Agrupación de datos del Dataset')
st.write(ds2)

# Creamoes gráficas para mostrar los datos
st.write('### Gráfica de longitud por especies')
st.bar_chart(data=ds2, y='avg_length', x='species', y_label='Longitud', x_label='Especie')
st.write('### Gráfica de peso por especies')
st.bar_chart(data=ds2, y='avg_weight', x='species', y_label='Peso', x_label='Especie')
st.write('### Gráfica de relación longitud/peso por especies')
st.bar_chart(data=ds2, y='avg_wl_ratio', x='species', y_label='Relación longitud/peso', x_label='Especie')
