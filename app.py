import streamlit as st

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="URL Launcher",
    page_icon="🔗",
    layout="centered"
)

# =========================
# STYLE CSS
# =========================
st.markdown("""
<style>
body {
    background: #f4f6f8;
}
.card {
    background: white;
    padding: 14px 18px;
    border-radius: 12px;
    margin-bottom: 10px;
    box-shadow: 0 6px 16px rgba(0,0,0,0.08);
}
.url-text {
    font-size: 15px;
    color: #000000;
    word-break: break-all;
    font-weight: 500;
}
.title {
    font-size: 30px;
    font-weight: bold;
    color: #000000;
}
.subtitle {
    color: #333333;
    margin-bottom: 18px;
}
.stButton > button {
    border-radius: 8px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# =========================
# SESSION STATE
# =========================
if "urls" not in st.session_state:
    st.session_state.urls = []

# =========================
# HEADER
# =========================
st.markdown('<div class="title">🔗 URL Launcher</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Masukkan URL dan buka dengan satu klik</div>', unsafe_allow_html=True)

# =========================
# INPUT URL
# =========================
url_input = st.text_input(
    "Masukkan URL",
    placeholder="https://serverlive1.streamlit.app"
)

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("➕ Tambahkan"):
        if url_input.strip():
            st.session_state.urls.append(url_input.strip())
            st.success("URL ditambahkan")
        else:
            st.warning("URL tidak boleh kosong")

with col2:
    if st.button("🧹 Reset"):
        st.session_state.urls.clear()

st.divider()

# =========================
# LIST URL
# =========================
st.subheader("📂 Daftar URL")

if not st.session_state.urls:
    st.info("Belum ada URL")
else:
    for i, url in enumerate(st.session_state.urls, start=1):
        st.markdown(f"""
        <div class="card">
            <div class="url-text">{i}. {url}</div>
        </div>
        """, unsafe_allow_html=True)

        c1, c2 = st.columns([1, 1])

        with c1:
            st.link_button("🌐 Open", url)

        with c2:
            if st.button("❌ Hapus", key=f"delete_{i}"):
                st.session_state.urls.pop(i - 1)
                st.experimental_rerun()
