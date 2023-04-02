import streamlit as st
import numpy as np
from PIL import Image


def XYZ2RGB(I):
    Ix = I[:, :, 0]
    Iy = I[:, :, 1]
    Iz = I[:, :, 2]
    m, n = Ix.shape

    k = np.array([[0.41847, -0.15866, -0.082835],
                  [-0.091169, 0.25243, 0.015708],
                  [0.00092090, 0.0025498, 0.17860]])

    Ir = np.zeros((m, n), dtype=np.uint8)
    Ig = np.zeros((m, n), dtype=np.uint8)
    Ib = np.zeros((m, n), dtype=np.uint8)

    for i in range(m):
        for j in range(n):
            xyz = np.array([Ix[i, j], Iy[i, j], Iz[i, j]])
            rgb = np.dot(k, xyz)
            Ir[i, j] = np.uint8(rgb[0])
            Ig[i, j] = np.uint8(rgb[1])
            Ib[i, j] = np.uint8(rgb[2])

    Irgb = np.zeros((m, n, 3), dtype=np.uint8)
    Irgb[:, :, 0] = Ir
    Irgb[:, :, 1] = Ig
    Irgb[:, :, 2] = Ib

    return Irgb


def main():
    st.title("Konversi Model Warna dari XYZ ke RGB")
    uploaded_file = st.file_uploader(
        "Upload gambar RGB", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gambar asli XYZ", use_column_width=True)
        img_array = np.array(image)

        converted_image = XYZ2RGB(img_array)
        st.image(converted_image, caption="Gambar konversi RGB",
                 use_column_width=True)


if __name__ == "__main__":
    main()
