def synthesize(responses):
    output = "\nFINAL CONSOLIDATED RESPONSE\n\n"
    for model, response in responses.items():
        output += f"[{model.upper()} VIEW]\n"
        output += response[:500] + "\n\n"
    return output
