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
            
div.stDownloadButton > button {{
 background-color: #007BFF;
    color: white;
    border-radius: 8px;
    padding: 10px 16px;
    font-weight: bold;
    border: none;
}}

/* Hover effect */
div.stDownloadButton > button:hover {{
    background-color: #0056b3;
    color: white;
}}

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
    opsi_list = ["Sakit", "Izin", "Interupsi"]
else:  # Praktek
    opsi_list = ["Sakit", "Izin", "Pindah Section", "Interupsi"]

opsi = st.selectbox("Jenis Perizinan", opsi_list)

# ======================
# 📦 LOGIC
# ======================

if opsi == "Sakit":
    st.subheader("🤒 Sakit")
    durasi = st.radio("Durasi sakit", ["1 Hari", "> 1 Hari"])

    if durasi == "1 Hari":
        if section == "Teori":
            st.markdown("""
            <div style="
                    background-color: rgba(255,255,255,0.8);
                    padding: 15px;
                    border-radius: 10px;
                    color: black;
                ">
                <p style="font-size:20px; color:black;">
                    <b>Prosedur :</b>
                </p>
            1. Lapor kepada kepala bengkel pada hari H (melalui WA).\n
            2. Ketika masuk, siapkan:\n
               -<b> Forum surat izin Tidak Masuk dengan tanda tangan orang tua/wali\n
               -<b> Surat dari orang tua/wali (dengan tanda tangan)\n
               </b>          
            3. Minta tanda tangan forum surat izin kepada kepala bengkel.\n
            4. Kumpulkan semua surat kepada penghitung jam plus-minus
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### Surat Izin Tidak Masuk:")
            with open("surat_ijin_tidak_masuk.pdf", "rb") as f:
             st.download_button(
               label="📥 Download Surat",
               data=f,
               file_name="surat_ijin_tidak_masuk.pdf",
               mime="application/pdf" )

        elif section == "Praktek":
            st.markdown("""
            <div style="
                    background-color: rgba(255,255,255,0.8);
                    padding: 15px;
                    border-radius: 10px;
                    color: black;
                ">
            <p style="font-size:20px; color:black;">
                <b>Prosedur :</b>
            </p>
            1. Lapor kepada instruktur/dosen pada hari H (melalui WA).\n
            2. Ketika masuk siapkan:\n
               -<b> Forum surat izin Tidak Masuk dengan tanda tangan orang tua/wali\n
               -<b> Surat dari orang tua/wali *(dengan tanda tangan)*\n
               </b>      
            3. Minta tanda tangan forum surat izin kepada instruktur/dosen.\n
            4. Kumpulkan semua surat kepada penghitung jam plus-minus
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### Surat Izin Tidak Masuk:")
            with open("surat_ijin_tidak_masuk.pdf", "rb") as f:
             st.download_button(
              label="📥 Download Surat",
              data=f,
              file_name="surat_ijin_tidak_masuk.pdf",
              mime="application/pdf" )
         
    else:
         if section == "Teori":
            st.markdown("""
            <div style="
                    background-color: rgba(255,255,255,0.8);
                    padding: 15px;
                    border-radius: 10px;
                    color: black;
                ">
                <p style="font-size:20px; color:black;">
                    <b>Prosedur :</b>
                </p>
            1. Lapor kepada kepala bengkel pada hari H (melalui WA).\n
            2. Ketika masuk, siapkan:\n
               -<b> Forum surat izin Tidak Masuk dengan tanda tangan orang tua/wali\n
               -<b> Surat dari orang tua/wali (dengan tanda tangan)\n
               -<b> Surat dokter (rumah sakit/puskesmas)\n      
            3. Minta tanda tangan forum surat izin kepada kepala bengkel.\n
            4. Kumpulkan semua surat kepada penghitung jam plus-minus 
            </b>  
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### Surat Izin Tidak Masuk:")
            with open("surat_ijin_tidak_masuk.pdf", "rb") as f:
             st.download_button(
               label="📥 Download Surat",
               data=f,
               file_name="surat_ijin_tidak_masuk.pdf",
               mime="application/pdf" )

         elif section == "Praktek":
            st.markdown("""
            <div style="
                    background-color: rgba(255,255,255,0.8);
                    padding: 15px;
                    border-radius: 10px;
                    color: black;
                ">
            <p style="font-size:20px; color:black;">
                <b>Prosedur :</b>
            </p>
            1. Lapor kepada instruktur/dosen pada hari H (melalui WA).\n
            2. Ketika masuk siapkan:\n
               -<b> Forum surat izin Tidak Masuk dengan tanda tangan orang tua/wali\n
               -<b> Surat dari orang tua/wali *(dengan tanda tangan)*\n
               -<b> Surat dokter (rumah sakit/puskesmas)\n
               </b>      
            3. Minta tanda tangan forum surat izin kepada instruktur/dosen.\n
            4. Kumpulkan semua surat kepada penghitung jam plus-minus
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### Surat Izin Tidak Masuk:")
            with open("surat_ijin_tidak_masuk.pdf", "rb") as f:
             st.download_button(
               label="📥 Download Surat",
               data=f,
               file_name="surat_ijin_tidak_masuk.pdf",
               mime="application/pdf")
         
elif opsi == "Izin":
    st.subheader("📝 Izin")
    Jenis = st.radio("Jenis Izin", ["Terencana", "Tidak Masuk"])

    if Jenis == "Terencana":
        if section == "Teori":
            st.markdown("""
            <div style="
                    background-color: rgba(255,255,255,0.8);
                    padding: 15px;
                    border-radius: 10px;
                    color: black;
                ">
                <p style="font-size:20px; color:black;">
                    <b>Prosedur :</b>
                </p>
            1.Lapor kepada kepala bengkel maksimal H-1\n
            2.Dengan menyiapkan:\n
              -<b> Forum surat izin Terencana (dengan tanda tangan orangtua/wali)\n
              -<b> Bukti Acara (Contoh: Surat Undangan)\n
            3.Minta tanda tangan Forum surat izin kepada kepala bengkel\n
            4.Kumpulkan semua surat kepada penghitung jam plus-minus\n
            </b>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### Surat Izin Terencana:")
            with open("surat_ijin_tidak_masuk_terencana.pdf", "rb") as f:
             st.download_button(
               label="📥 Download Surat",
               data=f,
               file_name="surat_ijin_tidak_masuk_terencana.pdf",
               mime="application/pdf" )

        elif section == "Praktek":
            st.markdown("""
            <div style="
                    background-color: rgba(255,255,255,0.8);
                    padding: 15px;
                    border-radius: 10px;
                    color: black;
                ">
            <p style="font-size:20px; color:black;">
                <b>Prosedur :</b>
            </p>
            1.Lapor kepada instruktur/dosen maksimal H-1\n
            2.Dengan menyiapkan:\n
              -<b> Forum surat izin Terencana (dengan tanda tangan orangtua/wali)\n
              -<b> Bukti Acara (Contoh: Surat Undangan)\n
            3.Minta tanda tangan Forum surat izin kepada instruktur/dosen\n
            4.Kumpulkan semua surat kepada penghitung jam plus-minus\n
            </b>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### Surat Izin Terencana:")
            with open("surat_ijin_tidak_masuk_terencana.pdf", "rb") as f:
             st.download_button(
              label="📥 Download Surat",
              data=f,
              file_name="surat_ijin_tidak_masuk_terencana.pdf",
              mime="application/pdf" )
         
    else:
         if section == "Teori":
            st.markdown("""
            <div style="
                    background-color: rgba(255,255,255,0.8);
                    padding: 15px;
                    border-radius: 10px;
                    color: black;
                ">
                <p style="font-size:20px; color:black;">
                    <b>Prosedur :</b>
                </p>
            1. Lapor kepada kepala bengkel pada hari H (melalui WA).\n
            2.Dengan menyiapkan:\n
              -<b> Forum surat izin Tidak Masuk (dengan tanda tangan orangtua/wali)\n
              -<b> Bukti Acara (Contoh: Surat melayu orang meninggal)\n
            3.Minta tanda tangan Forum surat izin kepada kepala bengkel\n
            4.Kumpulkan semua surat kepada penghitung jam plus-minus\n
            </b>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### Surat Izin Tidak Masuk:")
            with open("surat_ijin_tidak_masuk.pdf", "rb") as f:
             st.download_button(
               label="📥 Download Surat",
               data=f,
               file_name="surat_ijin_tidak_masuk.pdf",
               mime="application/pdf" )

         elif section == "Praktek":
            st.markdown("""
            <div style="
                    background-color: rgba(255,255,255,0.8);
                    padding: 15px;
                    border-radius: 10px;
                    color: black;
                ">
            <p style="font-size:20px; color:black;">
                <b>Prosedur :</b>
            </p>
            1. Lapor kepada instruktur/dosen pada hari H (melalui WA).\n
            2.Dengan menyiapkan:\n
              -<b> Forum surat izin Tidak Masuk (dengan tanda tangan orangtua/wali)\n
              -<b> Bukti Acara (Contoh: Surat melayu orang meninggal)\n
            3.Minta tanda tangan Forum surat izin kepada instruktur/dosen\n
            4.Kumpulkan semua surat kepada penghitung jam plus-minus\n
            </b>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### Surat Izin Tidak Masuk:")
            with open("surat_ijin_tidak_masuk.pdf", "rb") as f:
             st.download_button(
               label="📥 Download Surat",
               data=f,
               file_name="surat_ijin_tidak_masuk.pdf",
               mime="application/pdf")

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
        <li>Tanya istruktur asal dan yang dituju apakah bisa pindah section</li>
        <li>Cari teman yang ingin pindah ke section awal(jika ada)</li>
        <li>Konfirmasi ke kepala bengkel</li>
        <li>Ambil Surat Pindah Section di Resepsionis (jika tempat tersedia)</li>
        <li>Isi dengan benar </li>
        <li>Tanda tangan instruktur/dosen section yang dituju</li>
        <li>Setelah selesai pindah section lapor dan serahkan surat ke kepala bengkel
    </ol>
    </div>
    """, unsafe_allow_html=True)

elif opsi == "Interupsi":
    st.subheader("⏸ Interupsi")

    if section == "Teori":
            st.markdown("""
            <div style="
                    background-color: rgba(255,255,255,0.8);
                    padding: 15px;
                    border-radius: 10px;
                    color: black;
                ">
            <p style="font-size:40px; color:black;">
                <b>Prosedur :</b>
            </p>
            <ol>
                <li>Ambil surat interupsi di AA</li>
                <li>Isi surat dengan benar</li>
                <li>Minta tanda tangan kepada petugas AA</li>
                <li>Laporkan kepada dosen pengampu dengan menyerahkan surat secara langsung, meletakkannya di meja dosen di kelas, atau menitipkannya melalui ketua kelas.</li>
                <li>Jangan lupa tapping interupsi out sebelum keluar</li>
                <li>Pastikan surat tersampaikan kepada penghitung jam plus minus (setelah dosen pengajar mengetahui)</li>
            </ol>
            </div>
            """, unsafe_allow_html=True)

    elif section == "Praktek":
            st.markdown("""
            <div style="
                    background-color: rgba(255,255,255,0.8);
                    padding: 15px;
                    border-radius: 10px;
                    color: black;
                ">
            <p style="font-size:40px; color:black;">
                <b>Prosedur :</b>
            </p>
            <ol>
                <li>izin instruktur section</li>
                <li>siapkan buku jam minus /MKL tergantung instruktur </li>
                <li>isi buku/MKL dengan benar</li>
                <li>Jangan lupa tapping interupsi out sebelum keluar</li>
            </ol>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("### Surat Pernyataan:")
    with open("surat_pernyataan.pdf", "rb") as f:
         st.download_button(
           label="📥 Download Surat",
           data=f,
           file_name="surat_pernyataan.pdf",
           mime="application/pdf" )

# ======================
# FOOTER
# ======================
st.markdown("---")
st.caption("✨ Sistem Perizinan | By.atmi 58")
