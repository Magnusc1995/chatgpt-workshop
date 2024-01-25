import http.client
import json

api_key = "tom"

def query_openai(prompt):
    
    params = json.dumps({
        "model": "gpt-3.5-turbo",
        "messages": [
            #{"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 300
    })

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    connection = http.client.HTTPSConnection("api.openai.com")
    connection.request("POST", "/v1/chat/completions", params, headers)
    response = connection.getresponse()

    result = json.loads(response.read().decode())
    connection.close()
    return result["choices"][0]["message"]["content"]

ingrediences = []

print()
print("----------------------------------")
print("Welcome to the recepie builder!")
print("Add an ingredience, and how much you have.")
print("When you have added all ingrediences, write done, and you will get an appropriate recepie! :))")
print()

while (True):

    ingredient = str(input("Write an ingredient and amount or type done if finished: "))

    if ingredient.lower() == "done":
        break

    ingrediences.append(ingredient)

recepie_prompt = "I have some ingrediences and need help with what I can cook with them. These are my ingrediences: " + str(ingrediences)

print()
print(recepie_prompt)
print()
print("Getting recepie...")
print()

response = query_openai(recepie_prompt)
print(response)

