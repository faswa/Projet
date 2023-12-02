import leafmap
import streamlit as st
url = 'cartes intepolees/date 02'

images = 'cartes intepolees/date 02/*.tif'
leafmap.create_timelapse(
    images,
    out_gif='carte.gif',
    bands=[0, 1, 2],
    fps=10,
    progress_bar_color='blue',
    add_text=True,
    text_xy=('3%', '3%'),
    text_sequence=list(range(-6, 1)),
    font_size=20,
    font_color='black',
    mp4=False,
    reduce_size=False,
)
leafmap.show_image('carte.gif')
st.image('carte.gif')