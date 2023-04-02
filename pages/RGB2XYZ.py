import streamlit as st
import numpy as np
from PIL import Image


def RGB2XYZ(I):
    Ir = I[:, :, 0]
    Ig = I[:, :, 1]
    Ib = I[:, :, 2]
    m, n = Ir.shape

    k = np.array([[0.49, 0.31, 0.20],
                  [0.17697, 0.81240, 0.01063],
                  [0.00, 0.01, 0.99]])

    Ixyz = np.zeros_like(I)
    for i in range(m):
        for j in range(n):
            rgb = [Ir[i, j], Ig[i, j], Ib[i, j]]
            xyz = (1/0.17697)*k.dot(rgb)
            Ixyz[i, j, 0] = xyz[0]
            Ixyz[i, j, 1] = xyz[1]
            Ixyz[i, j, 2] = xyz[2]

    return Ixyz


def main():
    st.title("Konversi Model Warna dari RGB ke XYZ")
    uploaded_file = st.file_uploader(
        "Upload gambar RGB", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gambar asli RGB", use_column_width=True)
        img_array = np.array(image)

        converted_image = RGB2XYZ(img_array)
        st.image(converted_image, caption="Gambar konversi XYZ",
                 use_column_width=True)


if __name__ == "__main__":
    main()
