import streamlit as st
from streamlit.components.v1 import html

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="URL Launcher",
    page_icon="🚀",
    layout="centered"
)

# =========================
# STYLE CSS
# =========================
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}
.card {
    background: rgba(255,255,255,0.08);
    padding: 16px;
    border-radius: 14px;
    margin-bottom: 12px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.25);
}
.url-text {
    font-size: 15px;
    color: #ffffff;
    word-break: break-all;
}
.title {
    font-size: 32px;
    font-weight: bold;
    color: white;
}
.subtitle {
    color: #cfd8dc;
    margin-bottom: 20px;
}
.stButton > button {
    border-radius: 10px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# =========================
# SESSION STATE
# =========================
if "urls" not in st.session_state:
    st.session_state.urls = []

if "preview_url" not in st.session_state:
    st.session_state.preview_url = None

# =========================
# HEADER
# =========================
st.markdown('<div class="title">🚀 URL Launcher</div>', unsafe_allow_html=True)
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
    if st.button("➕ Tambahkan URL"):
        if url_input.strip():
            st.session_state.urls.append(url_input.strip())
            st.success("URL berhasil ditambahkan")
        else:
            st.warning("URL tidak boleh kosong")

with col2:
    if st.button("🧹 Reset Semua"):
        st.session_state.urls.clear()
        st.session_state.preview_url = None

st.divider()

# =========================
# DAFTAR URL
# =========================
st.subheader("📂 Daftar URL")

if not st.session_state.urls:
    st.info("Belum ada URL yang ditambahkan")
else:
    for i, url in enumerate(st.session_state.urls, start=1):
        st.markdown(f"""
        <div class="card">
            <div class="url-text">{i}. {url}</div>
        </div>
        """, unsafe_allow_html=True)

        c1, c2, c3 = st.columns([1, 1, 1])

        with c1:
            st.link_button("🌐 Open", url)

        with c2:
            if st.button("👁 Preview", key=f"preview_{i}"):
                st.session_state.preview_url = url

        with c3:
            if st.button("❌ Hapus", key=f"delete_{i}"):
                st.session_state.urls.pop(i - 1)
                st.experimental_rerun()

# =========================
# PREVIEW IFRAME
# =========================
if st.session_state.preview_url:
    st.divider()
    st.subheader("🔍 Preview")
    html(
        f"""
        <iframe 
            src="{st.session_state.preview_url}" 
            width="100%" 
            height="600"
            style="border-radius:14px;border:none;">
        </iframe>
        """,
        height=620
    )
