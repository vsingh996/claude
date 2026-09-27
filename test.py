import chromadb
chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="vehicles")

collection.add(
    ids=["car", "truck", "boat", "fish"],
    documents=[
        "Car has many brands and models. it runs on roads and highways",
        "Truck is a large vehicle used for transporting goods",
        "Boat is a watercraft used for transportation on water",
        "Fish is an aquatic animal that lives in water"
    ]
)
results = collection.query(
    query_texts=["sharks eat which animals?"], # Chroma will embed this for you
    n_results=2, # how many results to return
    include = ["embeddings"]
)
print(results)