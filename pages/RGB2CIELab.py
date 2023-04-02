import streamlit as st
import numpy as np
import cv2

# Fungsi RGB2XYZ


def RGB2XYZ(RGB):
    RGB = RGB / 255
    mask = RGB > 0.04045
    RGB[mask] = ((RGB[mask] + 0.055) / 1.055) ** 2.4
    RGB[~mask] = RGB[~mask] / 12.92
    XYZ = np.zeros(RGB.shape)
    XYZ[..., 0] = 0.412453 * RGB[..., 0] + 0.357580 * \
        RGB[..., 1] + 0.180423 * RGB[..., 2]
    XYZ[..., 1] = 0.212671 * RGB[..., 0] + 0.715160 * \
        RGB[..., 1] + 0.072169 * RGB[..., 2]
    XYZ[..., 2] = 0.019334 * RGB[..., 0] + 0.119193 * \
        RGB[..., 1] + 0.950227 * RGB[..., 2]
    return XYZ

# Fungsi XYZ2LAB


def XYZ2LAB(XYZ):
    XYZ /= np.array([0.95047, 1.0, 1.08883])
    mask = XYZ > 0.008856
    XYZ[mask] = XYZ[mask] ** (1/3)
    XYZ[~mask] = (7.787 * XYZ[~mask]) + (16/116)
    LAB = np.zeros(XYZ.shape)
    LAB[..., 0] = (116 * XYZ[..., 1]) - 16
    LAB[..., 1] = 500 * (XYZ[..., 0] - XYZ[..., 1])
    LAB[..., 2] = 200 * (XYZ[..., 1] - XYZ[..., 2])
    return LAB

# Fungsi utama


def main():
    st.title("RGB ke CIELab")

    # Membaca citra
    uploaded_file = st.file_uploader(
        "Pilih file citra", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        file_bytes = np.asarray(
            bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Konversi RGB ke CIELab
        XYZ = RGB2XYZ(img)
        LAB = XYZ2LAB(XYZ)

        # Tampilkan citra asli dan hasil konversi
        st.image([img, LAB.astype(np.uint8)], caption=[
                 'Citra Asli', 'Citra Hasil Konversi'], width=256)


if __name__ == '__main__':
    main()
