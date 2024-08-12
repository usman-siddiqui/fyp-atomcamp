def pinecone_upsertion(model):
  pinecone_api = userdata.get('pinecone_api')
  pc = Pinecone(api_key=pinecone_api)

  index_name = "restaurant-info-index"
  # To call the create_index at once. Try-except is used to avoid exception. Otherwise, it will create index and can cause error.
  try:
    if index_name not in pc.list_indexes():
        pc.create_index(
            index_name,
            dimension=model.get_sentence_embedding_dimension(),
            metric='cosine',
            spec=ServerlessSpec(
                cloud='aws',
                region='us-east-1'
            )
        )
  except:
    pass

  index = pc.Index(index_name)

  # Embedding the documents
  doc_embeddings = model.encode([json.dumps(info) for info in restaurant_info])
  # vector insertion to pinecone
  vectors_to_upsert = []
  for i, embedding in enumerate(doc_embeddings):
      data = vectors_to_upsert.append((str(i), embedding.tolist()))

  # Upsert data to Pinecone
  index.upsert(vectors=vectors_to_upsert)
  return index


openai_key = userdata.get('openai_api_key_turbo3')
openai.api_key = openai_key

# Load pre-trained model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
pc_index = pinecone_upsertion(model)
top_k = 3

# Retrieve relevant emebdding from pinecone

def retrieve(query, top_k=top_k):
    query_embedding = model.encode([query]).tolist()
    result = pc_index.query(vector=query_embedding, top_k=top_k, include_values=True)
    matches = result['matches']
    matches = result.get('matches', [])

    documents = []
    for match in matches:
        idx = int(match['id'])
        if 0 <= idx < len(restaurant_info):
            documents.append(restaurant_info[idx])

    return documents

# retrieve("what is the price of mutton karahi", top_k)



def insertdata_db(question, response):

    # print(question, response)
    mydb = connection_db()
    mycursor = mydb.cursor()
    sql = "INSERT INTO maintain_history (question, answer) VALUES (%s, %s)"
    val = (question, response)
    mycursor.execute(sql, val)
    print(mycursor.rowcount, "record inserted.")
    mydb.commit()
    return  mycursor.execute(sql, val)


def del_record_from_table():

    mydb = connection_db()
    mycursor = mydb.cursor()
    sql = "DELETE FROM maintain_history"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")
    mycursor.close()
    mydb.close()

def fetch_history():

    mydb = connection_db()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM maintain_history"
    mycursor.execute(sql)
    # mydb.commit()
    myresult = mycursor.fetchall()
    history = []
    for res in myresult:
      # add question
      history.append({
          "role": "user",
          "content": res[1]
      })
      # add answer
      history.append({
          "role": "assistant",
          "content": res[2]
      })

    mycursor.close()
    mydb.close()
    return history
# fetch_history()


 # Generate response with retrieval-augmentation
def generate_response(query, top_k=top_k):
    # Retrieve relevant documents
    relevant_docs = retrieve(query, top_k)
    # print(relevant_docs)
    context = "\n".join([json.dumps(doc) for doc in relevant_docs])
    history = fetch_history()
    print("history---", history)

    messages = [
      {
          "role": "system",
          "content": "You are an assistant. Provide to the point answer. Avoid hallucinations. If the answer is not available in the json of restaurant_info, Apologies, in a decent way."
      }
    ]

    if history:
          messages.extend(history)

    messages.append({
        "role": "user",
        "content": f"Context: {context}\n\nQuestion: {query}\nAnswer:"
    })


    # print(messages)
    response = openai.ChatCompletion.create(
        model= "gpt-4o-mini",
        messages=messages,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.3,
    )
    # print("query is : ", query)
    # print("response is ", response['choices'][0]['message']['content'].strip())
    setting_res_db = insertdata_db(query, response['choices'][0]['message']['content'].strip())
    return response['choices'][0]['message']['content'].strip()


# query = "What is the price of Chicken Handi and what is its average ratings?"
# response = generate_response(query)
# print(response)


def user_question(question, response):
  response = generate_response(question)
  return response

demo = gr.ChatInterface(user_question)
del_record_from_table()
demo.launch(debug = True)