from pygpt4all.models.gpt4all import GPT4All

def new_text_callback(text):
    print(text, end="")

model_path = "./models/gpt4all-converted.bin"
model = GPT4All(model_path)
model.generate("Once upon a time, ", n_predict=55, new_text_callback=new_text_callback)
