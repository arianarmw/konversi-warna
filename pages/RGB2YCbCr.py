import streamlit as st
import numpy as np
from PIL import Image


def RGB2YCBCR(I):
    Ir = I[:, :, 0]
    Ig = I[:, :, 1]
    Ib = I[:, :, 2]
    m, n = Ir.shape

    k = np.array([0, 128, 128])
    l = np.array([[0.299, 0.587, 0.114],
                 [-0.169, -0.331, 0.500],
                 [0.500, -0.419, -0.081]])

    Iy = np.zeros((m, n))
    Icb = np.zeros((m, n))
    Icr = np.zeros((m, n))

    for i in range(m):
        for j in range(n):
            rgb = np.array([Ir[i, j], Ig[i, j], Ib[i, j]])
            ycbcr = k + np.dot(l, rgb)
            Iy[i, j] = ycbcr[0]
            Icb[i, j] = ycbcr[1]
            Icr[i, j] = ycbcr[2]

    Iycbcr = np.zeros((m, n, 3), dtype=np.uint8)
    Iycbcr[:, :, 0] = Iy.astype(np.uint8)
    Iycbcr[:, :, 1] = Icb.astype(np.uint8)
    Iycbcr[:, :, 2] = Icr.astype(np.uint8)

    return Iycbcr


def main():
    st.title("RGB to YCbCr Converter")

    # Upload image
    uploaded_file = st.file_uploader(
        "Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Convert uploaded file to numpy array
        image = Image.open(uploaded_file)
        img_array = np.array(image)

        # Convert RGB to YCbCr
        img_ycbcr = RGB2YCBCR(img_array)

        # Show original and converted images
        col1, col2 = st.beta_columns(2)
        with col1:
            st.subheader("Original Image")
            st.image(image, use_column_width=True)
        with col2:
            st.subheader("Converted Image (YCbCr)")
            st.image(img_ycbcr, use_column_width=True)


if __name__ == "__main__":
    main()
