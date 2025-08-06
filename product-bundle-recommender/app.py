from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load rules
rules = pd.read_csv("rules.csv")

# If antecedents/consequents are strings like "{'Product'}", convert to list
rules['antecedents'] = rules['antecedents'].apply(lambda x: eval(x) if isinstance(x, str) else x)
rules['consequents'] = rules['consequents'].apply(lambda x: eval(x) if isinstance(x, str) else x)

def recommend_bundle(product_name, rules_df, top_n=5):
    recommendations = set()  # use set to avoid duplicates

    # Check if product in antecedents
    filtered = rules_df[rules_df['antecedents'].apply(lambda x: product_name in list(x))]
    for _, row in filtered.iterrows():
        for item in row['consequents']:
            if item != product_name:
                recommendations.add(item)

    # Check if product in consequents
    filtered = rules_df[rules_df['consequents'].apply(lambda x: product_name in list(x))]
    for _, row in filtered.iterrows():
        for item in row['antecedents']:
            if item != product_name:
                recommendations.add(item)

    return list(recommendations)[:top_n]  # return only top_n products

@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = None
    product_list = sorted(set([item for sublist in rules['antecedents'] for item in list(sublist)]))
    
    if request.method == "POST":
        product = request.form.get("product")
        recommendations = recommend_bundle(product, rules)

    return render_template("index.html", products=product_list, recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)


# To run the app, use the command:
# python app.py