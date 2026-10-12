import streamlit as st                                                                                                    

from recommendation import recommend_crops


# Page configuration
st.set_page_config(
    page_title="AP Crop Recommendation",
    page_icon="🌾",
    layout="wide"
)
# Load custom CSS
with open("style.css", "r") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# Title
st.title("🌾 Crop Recommendation Platform")
st.subheader("For Farmers of Andhra Pradesh")


st.write(
    "Enter your farm details below to get suitable crop recommendations."
)


# Sidebar
st.sidebar.header("🌱 Farm Details")


districts = [
    "Anantapur",
    "Sri Sathya Sai",
    "Kadapa",
    "Kurnool",
    "Guntur",
    "Palnadu",
    "Prakasam",
    "Krishna",
    "Nellore",
    "East Godavari",
    "West Godavari"
]


district = st.sidebar.selectbox(
    "Select District",
    districts
)


season = st.sidebar.selectbox(
    "Select Season", 
    ["Kharif", "Rabi"]
)


soil = st.sidebar.selectbox(
    "Select Soil Type",
    ["Red", "Black", "Alluvial", "Clay", "Sandy"]
)


water = st.sidebar.selectbox(
    "Water Availability",
    ["Low", "Medium", "High"]
)


rainfall = st.sidebar.selectbox(
    "Rainfall Level",
    ["Low", "Medium", "High"]
)


# Button
if st.sidebar.button("🌱 Recommend Crops"):

    results = recommend_crops(
        district,
        season,
        soil,
        water,
        rainfall
    )

    st.header("🌾 Recommended Crops")

    if results:

        for result in results:

            st.success(
                f"🌱 {result['crop']} — Match Score: "
                f"{result['score']}/5"
            )

            st.write(result["description"])

            st.write("---")

    else:

        st.warning(
            "No strong recommendation found. "
            "Try changing the farm details."
        )


# Information section
st.header("📚 About This Platform")

st.write(
    """
    This project provides simple crop recommendations
    based on basic farm information such as district,
    season, soil type, water availability and rainfall.

    The system uses Python decision-making logic and
    Streamlit to create an easy-to-use web interface.
    """
)


st.info(
    "Note: This is an educational project and should "
    "not replace advice from agricultural experts."
)