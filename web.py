import streamlit as st
import base64

st.set_page_config(
    page_title="Prosedur Perizinan",
    page_icon="📄",
    layout="centered"
)

def tampilkan_pdf(file):
    with open(file, "rb") as f:
        pdf_bytes = f.read()
    base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
    pdf_display = f"""
    <iframe src="data:application/pdf;base64,{base64_pdf}" 
    width="100%" height="600px" type="application/pdf"></iframe>
    """
    return pdf_display

# ======================
# 📷 LOAD BACKGROUND IMAGE
# ======================
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("ATMI-SOLO-500x250.jpg")

# ======================
# 🎨 CUSTOM CSS + BACKGROUND
# ======================
st.markdown(f"""
<style>       
/* label radio (judulnya) */
div[data-testid="stRadio"] label p {{
    font-size: 20px !important;
    font-weight: bold;
    color: white;            
}}
                       
div[data-testid="stSelectbox"] label {{
    font-size: 22px !important;
    font-weight: 600;
    color: white;         
}}            

.box-text {{
    background-color: rgba(0, 0, 0, 0.06); /* hitam transparan */
    padding: 10px;
    border-radius: 15px;
    color: black;
    margin-top: 10px;
    margin-bottom: 10px;
}}

.block-container:hover {{
    transform: scale(1.01);
    transition: 0.3s;
    box-shadow: 0 0 30px rgba(0, 150, 255, 0.6);
}}

.block-container {{
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.2);
}}
            
div[role="radiogroup"]:hover {{
    transform: scale(1.02);
    transition: 0.2s;
}}          

.stApp {{
    background-image: url("data:image/jpg;base64,{img}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    color: white;
}}

.block-container {{
    animation: fadeIn 0.8s ease-in-out;
}}

@keyframes fadeIn {{
    from {{
        opacity: 0;
        transform: translateY(20px);
    }}
    to {{
        opacity: 1;
        transform: translateY(0);
    }}
}}

.stApp::before {{
     content: "";
    position: fixed;
    inset: 0;

    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);

    background: rgba(0, 0, 0, 0.06);
    z-index: 0;
}}
.block-container {{
    position: relative;
    z-index: 1;
    max-width: 850px;

    /* 🔥 JARAK DARI ATAS */
    margin: 80px auto;

    background: rgba(0, 99, 215, 0.79);
    padding: 30px;

    /* 🔥 LENGKUNG SEMUA SISI */
    border-radius: 25px;

    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}}
.main-box * {{
    color: black ;
}}
h1 {{
    text-align: center;
    color: #ffffff;
}}

.block-container {{
    padding-top: 2rem;
}}

div[data-baseweb="select"], 
textarea, 
input {{
    background-color: #fff3b0 !important;
    border: 2px solid rgba(255,255,255,0.6) !important;
    border-radius: 10px !important;
    color: black !important;
}}

div[role="radiogroup"] {{
    background-color: #90caf9;
    padding: 10px;
    border-radius: 10px;
    border: 2px solid rgba(255,255,255,0.6) !important;
    margin-top: 1px;
    margin-bottom: 1px;

}}

.stButton button {{
    background-color: #ffb300;
    color:black;
    border-radius: 8px;
    border: 2px solid #ff6f00;
    font-weight: bold;
}}

.stButton button {{
    transition: all 0.2s ease;
}}

.stButton button:active {{
    transform: scale(0.95);
}}

.stButton button:hover {{
    background-color: #ff9800;
}}
</style>
""", unsafe_allow_html=True)

# ======================
# 🧾 HEADER
# ======================
st.title("📄 Prosedur Perizinan")
st.write("Silakan pilih jenis perizinan di bawah ini:")

# ======================
# 📌 PILIH SECTION
# ======================

section = st.selectbox(
    
    "Pilih Section",
    ["Teori", "Praktek"]
)

# ======================
# 📌 OPSI DINAMIS
# ======================
if section == "Teori":
    opsi_list = ["Sakit", "Izin", "Interupsi", "Surat Pernyataan"]
else:  # Praktek
    opsi_list = ["Sakit", "Izin", "Pindah Section", "Interupsi", "Surat Pernyataan"]

opsi = st.selectbox("Jenis Perizinan", opsi_list)

# ======================
# 📦 LOGIC
# ======================
if opsi == "Sakit":
    st.subheader("🤒 Sakit")
    durasi = st.radio("Durasi sakit", ["1 Hari", "> 1 Hari"])
    if durasi == "1 Hari":
        st.markdown("""
        <div style="
            background-color: rgba(255,255,255,0.8);
            padding: 15px;
            border-radius: 10px;
            color: black;
        ">
            <p style="font-size:20px; color:black;">
                Prosedur:
            </p>
        1. Lapor kepada instruktur/dosen yang mengampu pembelajaran.\n
        2. Siapkan:\n
           -<b> Surat izin tidak terencana (boleh menyusul)\n
           -<b> Surat dari orang tua/wali (dengan tanda tangan)\n
        3. lapor kepala bengkel sesuai prodi.\n
        </b>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Surat Izin tidak terencana:")
        st.markdown(tampilkan_pdf("Surat_ijin_tidak_masuk.pdf"), unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="
        background-color: rgba(255,255,255,0.8);
        padding: 15px;
        border-radius: 10px;
        color: black;
        ">
            <p style="font-size:20px; color:black;">
                Prosedur:
            </p>
        1. Lapor kepada instruktur/dosen yang mengampu pembelajaran.\n
        2. Siapkan:\n
           -<b> Surat dokter (rumah sakit / puskesmas)\n
           -<b> Surat izin tidak terencana\n
           -<b> Surat dari orang tua/wali *(dengan tanda tangan)*\n
        3. lapor kepala bengkel sesuai prodi.\n
        </b>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Surat Izin tidak terencana:")
        st.markdown(tampilkan_pdf("Surat_ijin_tidak_masuk.pdf"), unsafe_allow_html=True)

elif opsi == "Izin":
    st.subheader("📝 Izin")
    Jenis = st.radio("Jenis Izin", ["Terencana", "Tidak Terencana"])

    if Jenis == "Terencana":
        st.markdown("""
        <div style="
            background-color: rgba(255,255,255,0.8);
            padding: 15px;
            border-radius: 10px;
            color: black;
        ">
            <p style="font-size:20px; color:black;">
                Prosedur:
             </p>
        1. Lapor kepada instruktur/dosen yang mengampu pembelajaran.\n
        2. Siapkan:\n
           -<b> Surat izin terencana \n
           -<b> Bukti Acara (contoh surat undangan)\n
        3. lapor kepala bengkel sesuai prodi.\n
        </b>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Surat Izin terencana:")
        st.markdown(tampilkan_pdf("Surat_ijin_tidak_masuk_terencana.pdf"), unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="
            background-color: rgba(255,255,255,0.8);
            padding: 15px;
            border-radius: 10px;
            color: black;
        ">
            <p style="font-size:20px; color:black;">
                <b>Prosedur:</b>
             </p>
        1. Lapor kepada instruktur/dosen yang mengampu pembelajaran.\n
        2. Siapkan:\n
           -<b> Surat izin tidak terencana\n
           -<b> Bukti Acara (contoh surat lelayu)\n
        3. lapor kepala bengkel sesuai prodi.\n
        </b>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Surat Izin tidak terencana:")
        st.markdown(tampilkan_pdf("Surat_ijin_tidak_masuk.pdf"), unsafe_allow_html=True)

elif opsi == "Pindah Section":
    st.subheader("🔄 Pindah Section")
    st.markdown("""
    <div style="
            background-color: rgba(255,255,255,0.8);
            padding: 15px;
            border-radius: 10px;
            color: black;
        ">
    <p style="font-size:40px; color:black;">
                <b>Prosedur:</b>
             </p>
    <ol>
        <li>Tanya istruktur section apakah bisa pindah section</li>
        <li>Ambil Surat Pindah Section di Resepsionis (jika tempat tersedia)</li>
        <li>Isi dengan benar </li>
        <li>Tanda tangan instruktur/dosen pengajar</li>
        <li>lapor instruktur terkait
    </ol>
    </div>
    """, unsafe_allow_html=True)

elif opsi == "Interupsi":
    st.subheader("⏸ Interupsi")
    st.markdown("""
    <div style="
            background-color: rgba(255,255,255,0.8);
            padding: 15px;
            border-radius: 10px;
            color: black;
        ">
    <p style="font-size:40px; color:black;">
                <b>Prosedur:</b>
             </p>
    <ol>
        <li>Izin ke kepala bengkel minimal H-1</li>
        <li>Pergi ke resepsionis </li>
        <li>Isi surat dengan benar </li>
        <li>Pastikan sampai ke dosen/intruktur pengajar</li>
        <li>Jangan lupa tapping interupsi out sebelum keluar
    </ol>
    </div>
    """, unsafe_allow_html=True)

elif opsi == "Surat Pernyataan":
    st.subheader("📑 Surat Pernyataan")
    st.markdown("""
    <div style="
            background-color: rgba(255,255,255,0.8);
            padding: 15px;
            border-radius: 10px;
            color: black;
        ">
    <p style="font-size:40px; color:black;">
                <b>Prosedur:</b>
             </p>
    <ol>
        <li>Cetak surat pernyataan</li>
        <li>Isi dengan benar</li>
        <li>Lapor instruktur/dosen</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

    
    st.markdown("### Surat Pernyataan:")
    st.markdown(tampilkan_pdf("Surat_pernyataan.pdf"), unsafe_allow_html=True)

# ======================
# FOOTER
# ======================
st.markdown("---")
st.caption("✨ Sistem Perizinan | By.atmi 58")
