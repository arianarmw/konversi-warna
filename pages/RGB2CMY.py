import streamlit as st
import numpy as np
from PIL import Image

# Fungsi konversi warna dari RGB ke CMY


def RGB2CMY(image):
    Ir = np.array(image)[:, :, 0].astype(float)
    Ig = np.array(image)[:, :, 1].astype(float)
    Ib = np.array(image)[:, :, 2].astype(float)
    m, n = Ir.shape
    Ic = np.zeros((m, n))
    Im = np.zeros((m, n))
    Iy = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            c = 1 - Ir[i, j]/255
            m = 1 - Ig[i, j]/255
            y = 1 - Ib[i, j]/255
            Ic[i, j] = c
            Im[i, j] = m
            Iy[i, j] = y
    Icmy = np.stack((Ic, Im, Iy), axis=2)
    return Icmy


def main():
    st.title("Konversi Model Warna dari RGB ke CMY")
    image_file = st.file_uploader("Upload gambar", type=["jpg", "jpeg", "png"])
    if image_file is not None:
        image = Image.open(image_file)
        st.image(image, caption="Gambar asli", use_column_width=True)
        cmy_image = RGB2CMY(image)
        st.image(cmy_image, caption="Gambar hasil konversi",
                 use_column_width=True)


if __name__ == "__main__":
    main()
