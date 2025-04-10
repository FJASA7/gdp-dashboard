import streamlit as st
import urllib.parse

st.set_page_config(page_title="Image & Phone Search Tool", layout="centered")

st.title("أداة خاصه للبحث عن الصور والأرقام")
st.markdown("حمّل صورة أو اكتب رقم جوال، وراح نبحث لك وين تم استخدامهم على الإنترنت.")

# البحث بالصورة
st.header("البحث باستخدام صورة")
image_file = st.file_uploader("ارفع صورة للبحث", type=["jpg", "jpeg", "png"])

if image_file:
    st.image(image_file, caption="الصورة المرفوعة", use_column_width=True)
    st.markdown("اضغط الزر للبحث عنها في Yandex:")
    if st.button("ابحث في Yandex"):
        st.info("جارٍ تجهيز الرابط...")
        st.markdown("افتح الرابط التالي:")
        st.markdown("[بحث Yandex](https://yandex.com/images/)")
        st.warning("انسخ الصورة يدويًا وابحث عنها هناك (يا محمد ترا ياندكس يمنع رفعها تلقائيًا حالياً).")

# البحث برقم الجوال
st.header("البحث باستخدام رقم جوال")
phone = st.text_input("اكتب رقم الجوال (مثال: 0500000000)")

if phone:
    encoded_number = urllib.parse.quote(phone)
    st.markdown("نتائج البحث:")
    google_url = f"https://www.google.com/search?q={encoded_number}"
    bing_url = f"https://www.bing.com/search?q={encoded_number}"
    st.markdown(f"[ابحث في Google]({google_url})")
    st.markdown(f"[ابحث في Bing]({bing_url})")