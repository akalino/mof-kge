from fastapi import FastAPI
import pandas as pd
import gradio as gr
from serve import generate_keys

app = FastAPI()
top = pd.read_csv('predictions/top_small.csv')

CUSTOM_PATH = "/gradio"
# Create an iterator from the DataFrame
row_iterator = iter(top.iterrows())

@app.get("/")
async def root():
    return {"message": "Hi World"}

@app.get("/validate")
async def get_data():
    # Get the next row from the iterator
    index, row = next(row_iterator)
    # Convert the row to a dictionary
    row_dict = row.to_dict()
    # return "Info goes here"
    print(row_dict)
    return f"{row_dict['subject_mof_key']} predicate: {row_dict['p']} name: {row_dict['name']}"
    
    #return top.head().to_dict(orient="records")

# demo2 = gr.Interface(
#     fn=get_data,
#     inputs=[],
#     outputs=["text"],
# )



# def update(name):
#     return f"Welcome to Gradio, {name}!"

with gr.Blocks() as validate:
    gr.Markdown("Click **Generate New** and validate the mof.")
    with gr.Row():
        out = gr.Textbox()
    skip_button = gr.Button("Generate New")
    yes_button = gr.Button("Valid")
    no_button = gr.Button("Invalid")
    skip_button.click(fn=get_data, inputs=[], outputs=out)

generate_keys()
app = gr.mount_gradio_app(app, validate, path="/gradio")
