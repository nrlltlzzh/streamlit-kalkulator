import streamlit as st

st.set_page_config(
    page_title="Aplikasi Multifungsi",
    page_icon="🌸",
    layout="centered"
)

st.markdown(
    """
    <style>
    body {
        background-color: #fff0f6;
    }
    .stApp {
        background: linear-gradient(135deg, #ffe6f0, #fff5fa);
        color: #4a154b;
    }
    h1, h2, h3 {
        color: #cc0066 !important;
        text-align: center;
    }
    .stButton>button {
        background-color: #ff80bf;
        color: white;
        font-weight: bold;
        border-radius: 12px;
        padding: 0.6em 1.2em;
    }
    .stButton>button:hover {
        background-color: #ff4da6;
        color: white;
    }
    
    .css-1d391kg {
        background: linear-gradient(180deg, #f8f0f5, #f0e6f0);
        border-right: 1px solid #e6ccdd;
    }
    
    .sidebar-header {
        background-color: #ff99cc;
        color: white;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
        font-weight: 600;
        font-size: 16px;
    }
    
    .stRadio > div {
        background-color: white;
        padding: 12px;
        border-radius: 8px;
        margin: 8px 0;
        border: 1px solid #f0c0d0;
        transition: all 0.2s ease;
    }
    
    .stRadio > div:hover {
        border-color: #ff99cc;
        background-color: #fff5fa;
    }
    
    .stRadio > div > label {
        color: #4a154b;
        font-weight: 500;
        font-size: 14px;
    }
    
    .info-box {
        background-color: #fff5fa;
        border: 1px solid #f0c0d0;
        border-radius: 8px;
        padding: 12px;
        margin: 15px 0;
    }
    
    .info-box p {
        margin: 0;
        font-size: 13px;
        color: #666;
        line-height: 1.4;
    }
    
    .simple-divider {
        height: 1px;
        background-color: #f0c0d0;
        margin: 20px 0;
    }

    .sidebar-footer {
        text-align: center;
        font-size: 12px;
        color: #999;
        margin-top: 30px;
        padding-top: 15px;
        border-top: 1px solid #f0c0d0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def to_celsius(value: float, unit: str) -> float:
    if unit == "Celcius":
        return value
    elif unit == "Reamur":
        return value * 5.0 / 4.0
    elif unit == "Fahrenheit":
        return (value - 32.0) * 5.0 / 9.0

def from_celsius(c: float, unit: str) -> float:
    if unit == "Celcius":
        return c
    elif unit == "Reamur":
        return c * 4.0 / 5.0
    elif unit == "Fahrenheit":
        return c * 9.0 / 5.0 + 32.0

def fibonacci(n: int):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

st.sidebar.markdown('<div class="sidebar-header">Menu</div>', unsafe_allow_html=True)

menu = st.sidebar.radio(
    "Pilih fitur:",
    [
        "🧮 Kalkulator",
        "🌡️ Konversi Suhu", 
        "🔢 Fibonacci"
    ],
    key="menu_selection"
)

st.sidebar.markdown('<div class="simple-divider"></div>', unsafe_allow_html=True)

if "Kalkulator" in menu:
    st.sidebar.markdown(
        """
        <div class="info-box">
            <p><strong>Kalkulator</strong><br>
            Operasi matematika dasar: tambah, kurang, kali, bagi, dan pangkat.</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
elif "Konversi Suhu" in menu:
    st.sidebar.markdown(
        """
        <div class="info-box">
            <p><strong>Konversi Suhu</strong><br>
            Konversi antara Celsius, Reamur, dan Fahrenheit dengan mudah.</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
elif "Fibonacci" in menu:
    st.sidebar.markdown(
        """
        <div class="info-box">
            <p><strong>Fibonacci</strong><br>
            Generate deret Fibonacci dengan visualisasi grafik interaktif.</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

if "Kalkulator" in menu:
    st.title("🧮 Kalkulator")
    st.markdown("### Lakukan perhitungan matematika dengan mudah")

    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input("Masukkan angka pertama", value=0.0, step=1.0)
    with col2:
        b = st.number_input("Masukkan angka kedua", value=0.0, step=1.0)

    operator = st.selectbox("Pilih operator", ["Tambah (+)", "Kurang (-)", "Kali (×)", "Bagi (÷)", "Pangkat (^)"])

    if st.button("Hitung"):
        result = None
        if operator.startswith("Tambah"):
            result = a + b
        elif operator.startswith("Kurang"):
            result = a - b
        elif operator.startswith("Kali"):
            result = a * b
        elif operator.startswith("Bagi"):
            if b == 0:
                st.error("❌ Tidak bisa membagi dengan nol!")
            else:
                result = a / b
        elif operator.startswith("Pangkat"):
            result = a ** b

        if result is not None:
            st.success(f"Hasil: **{result}**")

elif "Konversi Suhu" in menu:
    st.title("🌡️ Konversi Suhu")
    st.markdown("### Konversi suhu antar satuan dengan mudah")

    nilai = st.number_input("Masukkan nilai suhu", value=0.0, step=0.5)
    satuan_asal = st.selectbox("Dari satuan", ["Celcius", "Reamur", "Fahrenheit"])
    satuan_tujuan = st.selectbox("Ke satuan", ["Celcius", "Reamur", "Fahrenheit"])

    if st.button("Konversi"):
        if satuan_asal == satuan_tujuan:
            st.info(f"Tidak perlu konversi, hasilnya tetap {nilai} {satuan_asal}")
        else:
            c = to_celsius(nilai, satuan_asal)
            hasil = from_celsius(c, satuan_tujuan)
            st.success(f"{nilai} {satuan_asal} = **{hasil:.2f} {satuan_tujuan}**")

elif "Fibonacci" in menu:
    st.title("🔢 Deret Fibonacci")
    st.markdown("### Generate dan visualisasi deret Fibonacci")

    n = st.number_input("Masukkan jumlah bilangan (n)", min_value=1, max_value=100, value=10, step=1)

    if st.button("Hasilkan Deret"):
        seq = fibonacci(int(n))
        st.write("Deret Fibonacci:")
        st.code(", ".join(map(str, seq)))
        st.line_chart(seq, height=250, use_container_width=True)