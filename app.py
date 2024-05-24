import json
import numpy as np
import torch
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

class InferlessPythonModel:
    def initialize(self):
        self.model = AutoModelForCausalLM.from_pretrained(
            "microsoft/Phi-3-mini-128k-instruct", 
            device_map="cuda", 
            torch_dtype="auto", 
            trust_remote_code=True, 
        )
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-128k-instruct")
        self.pipe = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
        )
    
    def infer(self, input_data):
        if isinstance(input_data, dict):
            input_json = input_data
        else:
            input_json = json.loads(input_data)

        chunks = input_json['chunks']
        roles = input_json['roles']

        generation_args = {
            "max_new_tokens": 500,
            "return_full_text": False,
            "temperature": 0.0,
            "do_sample": False,
        }

        messages = []

        for i in range(len(chunks)) :
            messages.append({ "role": roles[i] , "content" : chunks[i] })
        
        output = self.pipe(messages, **generation_args)

        return {"result": output[0]['generated_text'] }


    def finalize(self):
        self.generator = None
        print("Pipeline finalized.", flush=True)
