import streamlit as st
from copy_of_fasttext_bismillah import main2  # Import your main2() function

def main():
    st.title("Recipe Recommendation App")
    st.write("This app provides recipe recommendations based on your input.")

    # Streamlit inputs to replace terminal inputs in main2()
    categories = st.multiselect("Pilih kategori:", 
                                 options=["ayam", "ikan", "kambing", "sapi", "tahu", "telur", "tempe", "udang"], 
                                 default=[])
    allergens = st.text_input("Masukkan alergen untuk dihindari (pisahkan dengan koma):")
    ingredients = st.text_input("Masukkan bahan yang ingin digunakan (pisahkan dengan koma):")

    if st.button("Dapatkan Rekomendasi"):
        # Redirect inputs to your `main2()` logic
        # Modify `main2()` to accept arguments instead of using `input()`
        main2(categories, allergens, ingredients)  # You will need to modify `main2()` to handle these args

if __name__ == "__main__":
    main()
