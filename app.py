from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import joblib
import os

app = Flask(__name__, 
    static_folder=os.path.abspath("static"),
    static_url_path="/static")

# ==========================================
# 🔥 NEW: DISABLE BROWSER CACHE (Ye Add Karo)
# ==========================================
@app.after_request
def add_header(response):
    """
    Browser ko force karega ki wo page ko kabhi cache na kare.
    Har baar naya data load hoga.
    """
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

# ==========================================
# 1. LOAD SAVED MODEL
# ==========================================
try:
    model = joblib.load('models/crypto_liquidity_model.pkl')
    scaler = joblib.load('models/scaler.pkl')
    print("✅ Model & Scaler Loaded Successfully!")
except FileNotFoundError:
    print("❌ Error: Files nahi mili!")

# ==========================================
# 2. ROUTES
# ==========================================
@app.route('/')
def home():
    # URL se parameters utha rahe hain (GET Request)
    prediction_text = request.args.get('prediction_text')
    prob_text = request.args.get('prob_text')
    css_class = request.args.get('css_class')
    
    return render_template(
        'index.html',
        prediction_text=prediction_text,
        prob_text=prob_text,
        css_class=css_class
    )

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Data Fetch
            price = float(request.form['price'])
            vol_24h = float(request.form['vol_24h'])
            mkt_cap = float(request.form['mkt_cap'])
            
            # Default Values
            change_1h, change_24h, change_7d = 0.0, 0.0, 0.0
            p_chng_1d = 0.0
            log_volume = np.log1p(vol_24h)
            log_mkt_cap = np.log1p(mkt_cap)
            
            # Prediction
            input_data = [[price, change_1h, change_24h, change_7d, p_chng_1d, log_volume, log_mkt_cap]]
            input_scaled = scaler.transform(input_data)
            prediction = model.predict(input_scaled)[0]
            probability = model.predict_proba(input_scaled).max() * 100
            
            if prediction == 1:
                result_text = "✅ HIGH LIQUIDITY (Safe)"
                css_class = "success"
            else:
                result_text = "⚠️ LOW LIQUIDITY (Risky)"
                css_class = "danger"
                
            # Redirect wapas Home par (Data URL mein chipak kar jayega)
            return redirect(url_for('home', prediction_text=result_text, prob_text=f"{probability:.2f}%", css_class=css_class))
        
        except Exception as e:
            return redirect(url_for('home', prediction_text=f"Error: {str(e)}", css_class="danger"))

if __name__ == '__main__':
    app.run(debug=True)