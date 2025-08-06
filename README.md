# 🛒 Product Bundle Recommender

## 📌 Project Overview
The **Product Bundle Recommender** is a data science project that uses **Market Basket Analysis** (Apriori algorithm) to suggest product bundles based on historical sales data.  
The recommendations are served through a **Flask web application** where users can select a product and view related items often bought together.

---

## 🚀 Features
- 📊 **Market Basket Analysis** using Apriori
- 🛍 **Product Bundle Recommendations**
- 🌐 **Interactive Flask Web App**
- 🎨 Styled UI with **CSS**
- ⚡ Fast loading by pre-generating association rules (`rules.csv`)

---

## 🗂 Project Structure
product_bundle_recommender/
│
├── app.py # Flask app
├── rules.csv # Pre-generated association rules
├── templates/
│ └── index.html # HTML template
├── static/
│ └── style.css # CSS styling
├── data.csv # Raw sales dataset

---

## 📊 Dataset
- **Source:** [Kaggle – Sales Data](https://www.kaggle.com/)
- **Columns Used:**
  - `Order ID`
  - `Product`
  - `Quantity Ordered`
  - `Price Each`
  - `Order Date`
  - `Purchase Address`

---

## 🛠 Tech Stack
- **Python** (Pandas, NumPy)
- **Flask** (Web Framework)
- **mlxtend** (Apriori Algorithm)
- **Matplotlib / Seaborn** (EDA & Visualizations)
- **HTML + CSS** (Frontend)

---

## 📈 Implementation Steps
1. **Data Cleaning**
   - Remove NaN values
   - Convert data types
   - Extract `Month`, `Hour`, `City`
2. **EDA**
   - Monthly sales trend
   - Sales by city
   - Best time to advertise
   - Most sold products
3. **Market Basket Analysis**
   - Group products by order
   - Run Apriori
   - Generate association rules
4. **Export Rules**
   - Save as `rules.csv` for faster app loading
5. **Flask App**
   - Load `rules.csv`
   - Search product & display recommendations

---

## ▶️ How to Run the Project

### **1️⃣ Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/product-bundle-recommender.git
    cd product-bundle-recommender
### **2️⃣ Install Dependencies**
    ```bash
    pip install -r requirements.txt
### **3️⃣ Run the Flask App**
    ```bash
    python app.py
### **4️⃣ Open in Browser**
    ```bash
    http://127.0.0.1:5000/

## **Screenshots**
<img width="1126" height="589" alt="image" src="https://github.com/user-attachments/assets/df8e482b-aec4-41b2-a376-fe92c3cf9649" />
<img width="1125" height="572" alt="image" src="https://github.com/user-attachments/assets/c9fd29fb-f949-4036-8711-7437a5453b9f" />


## **Author**
***Priyanshu Pandey***
🔗 LinkedIn
