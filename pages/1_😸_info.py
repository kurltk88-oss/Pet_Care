import streamlit as st
from openai import OpenAI

import json
from openai import OpenAI

client = OpenAI(
    api_key = st.secret['key']
)

def get_standard_response(system_prompt, user_prompt):
    """
    Sends a prompt to the ChatGPT API where it will return a standard response.
    ChatGPT will not remember any prior conversations.

    Parameters:
    - system_prompt (str): Directions on how ChatGPT should act.
    - user_prompt (str): A prompt from the user.

    Returns:
    - (str): ChatGPT's response.
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response.choices[0].message.content


if 'breed' in st.session_state:
    st.write('information about ' + st.session_state['breed'])

    st.write(get_standard_response('You are veterinarian','Give me general care information for a'+ st.session_state['breed'] ))






