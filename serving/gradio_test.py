from fastapi import FastAPI
import pandas as pd
import gradio as gr
from serve import generate_keys

app = FastAPI()
filepath = f'predictions/topology_small.csv'
pred_df = pd.read_csv(filepath)
row_iterator = iter(pred_df.iterrows())

def get_new_row():
    # Get the next row from the iterator
    index, row = next(row_iterator)
    # Convert the row to a dictionary
    row_dict = row.to_dict()
    return f"{row_dict['subject_mof_key']} predicate: {row_dict['p']} name: {row_dict['name']}"

def approve():
    row["valid"] = "yes"

def deny():
    row["valid"] = "no"

with gr.Blocks() as validate:
    gr.Markdown("Click **Generate New** and validate the mof.")

    with gr.Row():
        out = gr.Textbox()

    skip_button = gr.Button("Generate New")
    yes_button = gr.Button("Valid")
    no_button = gr.Button("Invalid")

    skip_button.click(fn=get_new_row, inputs=[], outputs=out)
    yes_button.click(fn=approve, inputs=[], outputs=[])
    no_button.click(fn=deny, inputs=[], outputs=[])

generate_keys()
print("Generated new columns")
app = gr.mount_gradio_app(app, validate, path="/gradio")




