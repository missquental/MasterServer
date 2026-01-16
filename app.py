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
def load_data():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text())
    return []

def save_data(data):
    DATA_FILE.write_text(json.dumps(data, indent=2))

# =========================
# SESSION INIT
# =========================
if "data" not in st.session_state:
    st.session_state.data = load_data()

# =========================
# STYLE
# =========================
st.markdown("""
<style>
body { background:#f4f6f8; }
.card {
    background:white;
    padding:16px;
    border-radius:12px;
    margin-bottom:12px;
    box-shadow:0 6px 16px rgba(0,0,0,0.08);
}
.url-text {
    font-size:15px;
    color:black;
    word-break:break-all;
    font-weight:600;
    margin-bottom:6px;
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
st.markdown('<div class="title">🔗 URL Launcher</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Edit keterangan langsung tanpa hapus URL</div>', unsafe_allow_html=True)

# =========================
# INPUT URL BARU
# =========================
url_input = st.text_input(
    "Masukkan URL",
    placeholder="https://serverlive1.streamlit.app"
)

if st.button("➕ Tambahkan URL"):
    if url_input.strip():
        st.session_state.data.append({
            "url": url_input.strip(),
            "note": ""
        })
        save_data(st.session_state.data)
        st.success("URL ditambahkan")
    else:
        st.warning("URL tidak boleh kosong")

st.divider()

# =========================
# LIST URL + EDIT KETERANGAN
# =========================
st.subheader("📂 Daftar URL")

if not st.session_state.data:
    st.info("Belum ada URL")
else:
    for i, item in enumerate(st.session_state.data):
        st.markdown(f"""
        <div class="card">
            <div class="url-text">{i+1}. {item['url']}</div>
        </div>
        """, unsafe_allow_html=True)

        # EDIT KETERANGAN (MANUAL)
        note = st.text_input(
            "Keterangan",
            value=item.get("note", ""),
            key=f"note_{i}",
            placeholder="Isi keterangan di sini..."
        )

        # AUTO SAVE JIKA BERUBAH
        if note != item.get("note", ""):
            st.session_state.data[i]["note"] = note
            save_data(st.session_state.data)

        col1, col2 = st.columns([1, 1])

        with col1:
            st.link_button("🌐 Open", item["url"])

        with col2:
            if st.button("❌ Hapus URL", key=f"del_{i}"):
                st.session_state.data.pop(i)
                save_data(st.session_state.data)
                st.experimental_rerun()
