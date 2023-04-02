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
            xyz = k.dot(rgb)
            Ixyz[i, j, 0] = xyz[0]
            Ixyz[i, j, 1] = xyz[1]
            Ixyz[i, j, 2] = xyz[2]

    return Ixyz


def XYZ2HSV(I):
    X = I[:, :, 0]
    Y = I[:, :, 1]
    Z = I[:, :, 2]
    m, n = X.shape

    # konversi ke RGB
    r = 3.2406*X - 1.5372*Y - 0.4986*Z
    g = -0.9689*X + 1.8758*Y + 0.0415*Z
    b = 0.0557*X - 0.2040*Y + 1.0570*Z

    # konversi ke kisaran HSV
    H = np.zeros_like(X)
    S = np.zeros_like(X)
    V = np.zeros_like(X)

    for i in range(m):
        for j in range(n):
            x, y, z = r[i, j], g[i, j], b[i, j]
            v = max(x, y, z)
            vm = v - min(x, y, z)
            if v == 0:
                s = 0
            else:
                s = vm / v
            if s == 0:
                h = 0
            elif v == x:
                h = 60.0 * (((y - z) / vm) % 6.0)
            elif v == y:
                h = 60.0 * (((z - x) / vm) + 2.0)
            elif v == z:
                h = 60.0 * (((x - y) / vm) + 4.0)
            H[i, j] = h
            S[i, j] = s
            V[i, j] = v
    return np.dstack((H, S, V))


def main():
    st.title("Aplikasi Konversi Warna")
    uploaded_file = st.sidebar.file_uploader(
        "Pilih sebuah gambar ...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # baca gambar menggunakan PIL
        img = Image.open(uploaded_file)
        st.image(img, caption="Gambar Asli")

        # konversi ke XYZ dan tampilkan
        img = np.array(img)
        converted_image = XYZ2HSV(img)
        st.image(converted_image, caption="Gambar konversi XYZ",
                 use_column_width=True)


if __name__ == "__main__":
    main()
