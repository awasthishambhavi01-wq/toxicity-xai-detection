import gradio as gr


def detect_toxicity(text):
    # Dummy implementation for toxicity detection
    # In a real implementation, this could be a model prediction
    toxic_words = ['bad', 'hate', 'anger']
    return any(word in text.lower() for word in toxic_words)


iface = gr.Interface(fn=detect_toxicity,
                     inputs=gr.inputs.Textbox(lines=2, placeholder="Type your message here..."),
                     outputs='label',
                     title='Toxicity Detection',
                     description='Enter a text message to check for toxicity.')


iface.launch()