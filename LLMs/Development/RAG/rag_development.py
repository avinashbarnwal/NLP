import requests
import json

corpus_of_documents = [
    "Take a leisurely walk in the park and enjoy the fresh air.",
    "Visit a local museum and discover something new.",
    "Attend a live music concert and feel the rhythm.",
    "Go for a hike and admire the natural scenery.",
    "Have a picnic with friends and share some laughs.",
    "Explore a new cuisine by dining at an ethnic restaurant.",
    "Take a yoga class and stretch your body and mind.",
    "Join a local sports league and enjoy some friendly competition.",
    "Attend a workshop or lecture on a topic you're interested in.",
    "Visit an amusement park and ride the roller coasters.",
]




def jaccard_similarity(query, document):
    query = query.lower().split(" ")
    document = document.lower().split(" ")
    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))
    return len(intersection) / len(union)


def return_response(query, corpus):
    similarities = []
    for doc in corpus:
        similarity = jaccard_similarity(user_input, doc)
        similarities.append(similarity)
    return corpus_of_documents[similarities.index(max(similarities))]


def main():
    # Define the API URL
    url = "http://127.0.0.1:11434/api/chat"
    # Define the payload
    data = {"model": "llama2", "messages": [{"role": "user", "content": prompt}]}
    # Define the headers
    headers = {"Content-Type": "application/json"}
    # Make the POST request with stream=True to handle streaming response
    response = requests.post(url, json=data, headers=headers, stream=True)
    full_response = []
    # Process each line of the response as JSON objects
    for line in response.iter_lines():
        if line:
            # Decode each line (which is a JSON object) and print it
            decoded_line = json.loads(line.decode("utf-8"))
            full_response.append(decoded_line["message"]["content"])
            # print(decoded_line['message']['content'])
    res = "".join(full_response)
    return res

user_input = "I like to hike"
relevant_document = return_response(user_input, corpus_of_documents)
full_response = []
# https://github.com/jmorganca/ollama/blob/main/docs/api.md
prompt = f"""
You are a bot that makes recommendations for activities. You answer in very short sentences and do not include extra information.
This is the recommended activity: {relevant_document}
The user input is: {user_input}
Compile a recommendation to the user based on the recommended activity and the user input.
"""

if __name__ == "__main__":
    result = main()
    print(result)
