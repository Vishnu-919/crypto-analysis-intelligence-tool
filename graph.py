import networkx as nx
import matplotlib.pyplot as plt

def generate_spider_map(df, limit=200):
    if df.empty:
        print("No data to visualize.")
        return

    df = df.head(limit)

    G = nx.DiGraph()

    for _, row in df.iterrows():
        sender = row["from"]
        receiver = row["to"]
        amount = row["value_eth"]

        if sender and receiver:
            G.add_edge(sender, receiver, weight=amount)

    plt.figure(figsize=(14, 14))
    pos = nx.spring_layout(G, k=0.5)

    nx.draw(
        G,
        pos,
        node_size=30,
        node_color="skyblue",
        edge_color="gray",
        with_labels=False
    )

    plt.title("Crypto Transaction Spider Map")
    plt.savefig("static/spider_map.png")
    plt.show()

    print("Spider map saved as spider_map.png")
