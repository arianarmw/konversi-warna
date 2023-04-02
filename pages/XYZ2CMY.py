import streamlit as st
import numpy as np
from PIL import Image


def XYZ2CMY(I):
    X = np.array(I[:, :, 0]).astype(float)
    Y = np.array(I[:, :, 1]).astype(float)
    Z = np.array(I[:, :, 2]).astype(float)

    m, n = X.shape

    C = np.zeros_like(X)
    M = np.zeros_like(X)
    Y_ = np.zeros_like(X)

    for i in range(m):
        for j in range(n):
            C[i, j] = 1 - X[i, j]/255
            M[i, j] = 1 - Y[i, j]/255
            Y_[i, j] = 1 - Z[i, j]/255

    Icmy = np.zeros_like(I)
    Icmy[:, :, 0] = C
    Icmy[:, :, 1] = M
    Icmy[:, :, 2] = Y_

    return Icmy


def main():
    st.set_page_config(page_title="XYZ2CMY", page_icon=":paintbrush:")

    st.title("Konversi Model Warna dari XYZ ke CMY")

    uploaded_file = st.file_uploader(
        "Pilih gambar", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Gambar Asli', use_column_width=True)

        img_array = np.array(image)
        result = XYZ2CMY(img_array)

        st.image(result, caption='Hasil Konversi', use_column_width=True)


if __name__ == '__main__':
    main()
