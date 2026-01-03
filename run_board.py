from council import collect_responses
from chairman import synthesize

question = input("Enter decision question:\n")
responses = collect_responses(question)
final_output = synthesize(responses)

print(final_output)
