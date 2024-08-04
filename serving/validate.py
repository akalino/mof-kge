from fastapi import FastAPI
import pandas as pd
import gradio as gr
from serve import generate_keys

app = FastAPI()

class Validation:

    def __init__(self, prediction_file):

        print("Initializing validation")
        self.filepath = f'predictions/{prediction_file}'
        self.pred_df = pd.read_csv(self.filepath)
        self.row_iterator = iter(self.pred_df.iterrows())

    def get_new_row(self):
        # Get the next row from the iterator
        self.index, self.row = next(self.row_iterator)
        # Convert the row to a dictionary
        row_dict = self.row.to_dict()
        return f"{row_dict['subject_mof_key']} predicate: {row_dict['p']} name: {row_dict['name']}"

    def approve(self):
        self.pred_df.at[self.index, 'valid'] = 'yes'

    def deny(self):
        self.pred_df.at[self.index, 'valid'] = 'no'

    def save(self):
        self.pred_df.to_csv("predictions/testing.csv", index=False)

    def execute(self):
        generate_keys()

        with gr.Blocks() as validate:
            gr.Markdown("Click **Generate New** and validate the mof.")

            with gr.Row():
                out = gr.Textbox()

            skip_button = gr.Button("Generate New")
            yes_button = gr.Button("Valid")
            no_button = gr.Button("Invalid")
            save_button = gr.Button("Save")

            skip_button.click(fn=self.get_new_row, inputs=[], outputs=out)
            yes_button.click(fn=self.approve, inputs=[], outputs=[])
            no_button.click(fn=self.deny, inputs=[], outputs=[])
            save_button.click(fn=self.save, inputs=[], outputs=[])

        print("Generated new columns")
        global app
        app = gr.mount_gradio_app(app, validate, path="/gradio")

v = Validation("top_small.csv")
v.execute()



