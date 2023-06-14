# from transformers import pipeline
#
# generator_lite = pipeline('text-generation', model='EleutherAI/gpt-neo-125M')
#
# def generate(prompt):
#     prompt = input("Enter Prompt: ")
#     result_lite = generator_lite(prompt, max_length=200, do_sample=True, temperature=0.9)
#     return result_lite[0]['generated_text']
#
