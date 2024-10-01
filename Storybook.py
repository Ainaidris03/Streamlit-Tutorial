import os
import streamlit as st
from openai import OpenAI

#my_secret = os.environ['OPENAI_API_KEY']
my_secret = st.secret['OPENAI_API_KEY']
client=OpenAI(api_key=my_secret)

# Story generator
def story_gen(prompt):
    system_prompt = """You're a world-renowned storyteller with
    50 years of experience in creating children's stories.
    You will be given a concept to generate a story suitable
    for ages 5-7 years old."""

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=1.3,  # Boost creativity
        max_tokens=200
    )
    return response.choices[0].message.content

# Cover prompt generator
def cover_gen(story):
    system_prompt = """You will be given a children's storybook.
    Generate a prompt for cover art that is suitable and
    showcases the story themes. The prompt will be sent to DALL
    E 2."""

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": story}
        ],
        temperature=1.3,  # Boost creativity
        max_tokens=100
    )
    return response.choices[0].message.content

# Image generator
def image_gen(prompt):
    response = client.images.generate(
        model='dall-e-2',
        prompt=prompt,
        size='256x256',
        n=1
    )
    return response.data[0].url

# Storybook method
def storybook(prompt):
    story = story_gen(prompt)
    cover = cover_gen(story)
    image = image_gen(cover)

    st.image(image)
    st.write(story)

st.title('Storybook Generator for Kids')
st.divider()

prompt = st.text_area("Enter your story concept:")

if st.button("Generate Storybook"):
  story=story_gen(prompt)
  cover=cover_gen(story)
  image=image_gen(cover)

  st.image(image)
  st.write(story)
