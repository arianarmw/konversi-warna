import streamlit as st
import numpy as np
from PIL import Image


def RGB2HSV(I):
    Ir = np.array(I[:, :, 0]).astype(float)
    Ig = np.array(I[:, :, 1]).astype(float)
    Ib = np.array(I[:, :, 2]).astype(float)
    m, n = Ir.shape

    Ih = np.zeros_like(Ir)
    Is = np.zeros_like(Ir)
    Iv = np.zeros_like(Ir)

    for i in range(m):
        for j in range(n):
            r = Ir[i, j]/255
            g = Ig[i, j]/255
            b = Ib[i, j]/255

            v = max(max(r, g), b)
            vm = v-min(r, min(g, b))
            if v == 0:
                s = 0
            elif v > 0:
                s = vm/v
            if s == 0:
                h = 0
            elif v == r:
                h = 60/360*(np.mod((g-b)/vm, 6))
            elif v == g:
                h = 60/360*(2+((b-r)/vm))
            elif v == b:
                h = 60/360*(4+((r-g)/vm))

            Iv[i, j] = v
            Is[i, j] = s
            Ih[i, j] = h

    Ihsv = np.zeros_like(I)
    Ihsv[:, :, 0] = Ih
    Ihsv[:, :, 1] = Is
    Ihsv[:, :, 2] = Iv

    return Ihsv


def main():
    st.set_page_config(page_title="RGB2HSV", page_icon=":paintbrush:")

    st.title("Konversi Model Warna dari RGB ke HSV")

    uploaded_file = st.file_uploader(
        "Pilih gambar", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Gambar Asli', use_column_width=True)

        img_array = np.array(image)
        result = RGB2HSV(img_array)

        st.image(result, caption='Hasil Konversi', use_column_width=True)


if __name__ == '__main__':
    main()
