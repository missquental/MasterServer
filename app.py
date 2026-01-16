import streamlit as st
import json
from pathlib import Path

# =========================
# KONFIGURASI
# =========================
st.set_page_config(
    page_title="URL Launcher",
    page_icon="🔗",
    layout="centered"
)

DATA_FILE = Path("urls.json")

# =========================
# LOAD & SAVE
# =========================
def load_urls():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text())
    return []

def save_urls(urls):
    DATA_FILE.write_text(json.dumps(urls, indent=2))

# =========================
# SESSION INIT
# =========================
if "urls" not in st.session_state:
    st.session_state.urls = load_urls()

# =========================
# STYLE
# =========================
st.markdown("""
<style>
body { background:#f4f6f8; }
.card {
    background:white;
    padding:14px 18px;
    border-radius:12px;
    margin-bottom:10px;
    box-shadow:0 6px 16px rgba(0,0,0,0.08);
}
.url-text {
    font-size:15px;
    color:black;
    word-break:break-all;
    font-weight:500;
}
.title {
    font-size:30px;
    font-weight:bold;
    color:black;
}
.subtitle {
    color:#333;
    margin-bottom:18px;
}
.stButton>button {
    border-radius:8px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown('<div class="title">🔗 MASTER SERVER LIVE</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">URL tetap tersimpan meskipun refresh / pindah browser</div>', unsafe_allow_html=True)

# =========================
# INPUT
# =========================
url_input = st.text_input(
    "Masukkan URL",
    placeholder="https://serverlive1.streamlit.app"
)

c1, c2 = st.columns(2)

with c1:
    if st.button("➕ Tambahkan"):
        if url_input.strip():
            if url_input not in st.session_state.urls:
                st.session_state.urls.append(url_input.strip())
                save_urls(st.session_state.urls)
                st.success("URL tersimpan permanen")
            else:
                st.warning("URL sudah ada")
        else:
            st.warning("URL kosong")

with c2:
    if st.button("🧹 Hapus Semua"):
        st.session_state.urls = []
        save_urls([])
        st.success("Semua URL dihapus")

st.divider()

# =========================
# LIST URL
# =========================
st.subheader("📂 Daftar URL")

if not st.session_state.urls:
    st.info("Belum ada URL")
else:
    for i, url in enumerate(st.session_state.urls):
        st.markdown(f"""
        <div class="card">
            <div class="url-text">{i+1}. {url}</div>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns([1,1])

        with col1:
            st.link_button("🌐 Open", url)

        with col2:
            if st.button("❌ Hapus", key=f"del_{i}"):
                st.session_state.urls.pop(i)
                save_urls(st.session_state.urls)
                st.experimental_rerun()
