from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.llms import OpenAI
import os
from registered_keys import openapi_key

os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature=0.9)

# Define the prompt to suggest a destination based on the city and number of days
destination_prompt = PromptTemplate(
    input_variables=["city", "days"],
    template="Suggest a {days} day getaway place near the {city} of my choice. Only output the name of the place. ###city: {city} ###Getaway place:"
)

# Create the destination chain to use the LLM for suggesting a destination
destination_chain = LLMChain(
    llm=llm,
    prompt=destination_prompt,
    output_key="destination"
)

# Define the prompt to generate an itinerary based on the destination and number of days
itinerary_prompt = PromptTemplate(
    input_variables=["destination", "days"],
    template="Suggest names of places to visit on each day for {days} days to {destination}."
)

# Create the itinerary chain to use the LLM for generating an itinerary
itinerary_chain = LLMChain(
    llm=llm,
    prompt=itinerary_prompt,
    output_key="itinerary"
)

# Combine the chains into a SequentialChain
e2e_chain = SequentialChain(
    chains=[destination_chain, itinerary_chain],
    input_variables=["city", "days"],
    output_variables=["destination", "itinerary"],
    verbose=True
)
