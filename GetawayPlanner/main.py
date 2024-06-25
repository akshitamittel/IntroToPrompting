import llm_api
import streamlit as st

st.title("Getaway Planner")

# Input for city
city = st.text_input("Enter the city:", placeholder="e.g., San Francisco")

# Input for number of days
days = st.text_input("Enter the number of days:", placeholder="e.g., 3")

def generate_itinerary(city, days):
    try:
        days = int(days)
        if days < 1:
            st.error("Number of days must be a positive integer.")
            return

        inputs = {"city": city, "days": days}
        result = llm_api.e2e_chain.invoke(inputs)
        destination = result["destination"].strip()
        itinerary = result["itinerary"].strip()

        st.success(f"Suggested Destination: {destination}")
        st.text(f"Suggested Itinerary:\n{itinerary}")

    except ValueError:
        st.error("Please enter a valid number of days.")

# Button to generate itinerary
if st.button("Generate Itinerary"):
    if city and days:
        generate_itinerary(city, days)
    else:
        st.error("Please provide both the city and the number of days.")
