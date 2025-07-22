from flask import Flask, render_template_string, request, send_file
import requests
import pandas as pd
from datetime import datetime, timedelta
import io
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()
# Inicializa a aplicação Flask
app = Flask(__name__)

# Chave da API (lida do arquivo .env)
API_KEY = os.getenv("API_KEY")
BASE_URL = 'http://api.weatherapi.com/v1/history.json'

# Template HTML para a página da web
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Histórico do Tempo</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f9;
            color: #333;
        }
        .container {
            max-width: 900px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1, h2 {
            color: #333;
            border-bottom: 2px solid #007bff;
            padding-bottom: 10px;
        }
        form {
            margin-bottom: 20px;
            display: flex;
            gap: 10px;
        }
        input[type="text"] {
            flex-grow: 1;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }
        button {
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #0056b3;
        }
        a.button {
            display: inline-block;
            padding: 10px 20px;
            background-color: #28a745;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            margin: 20px 0;
            transition: background-color 0.3s;
        }
        a.button:hover {
            background-color: #218838;
        }
        .table-container {
            max-height: 500px;
            overflow-y: auto;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        thead th {
            background-color: #f8f9fa;
            position: sticky;
            top: 0;
            z-index: 1;
        }
        tbody tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        tbody tr:hover {
            background-color: #e9ecef;
        }
        .error {
            color: #d9534f;
            background-color: #f8d7da;
            border: 1px solid #f5c6cb;
            padding: 10px;
            border-radius: 4px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Consulta de Histórico do Tempo</h1>
        <form method="post">
            <input type="text" id="city" name="city" value="{{ city }}" placeholder="Digite o nome da cidade...">
            <button type="submit">Buscar</button>
        </form>

        {% if error %}
            <p class="error">{{ error }}</p>
        {% endif %}

        {% if data %}
            <h2>Exibindo dados para: <strong>{{ city }}</strong></h2>
            <a href="/download/excel?city={{ city }}" class="button">Baixar Tabela como Excel</a>
            <div class="table-container">
                {{ data|safe }}
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

def fetch_weather_data(city):
    """
    Busca os dados meteorológicos para uma cidade nos últimos 7 dias.
    Retorna um DataFrame do Pandas ou uma mensagem de erro.
    """
    all_hourly_data = []
    today = datetime.now()

    for i in range(7): # Loop para os últimos 7 dias
        date_to_fetch = today - timedelta(days=i)
        date_str = date_to_fetch.strftime('%Y-%m-%d')
        
        params = {'key': API_KEY, 'q': city, 'dt': date_str}

        try:
            response = requests.get(BASE_URL, params=params)
            response.raise_for_status()  # Lança um erro para respostas HTTP 4xx ou 5xx
            data = response.json()

            forecast_day = data.get('forecast', {}).get('forecastday', [])
            if forecast_day:
                hourly_data = forecast_day[0].get('hour', [])
                for hour in hourly_data:
                    all_hourly_data.append({
                        'Data e Hora': hour.get('time'),
                        'Temp (°C)': hour.get('temp_c'),
                        'Condição': hour.get('condition', {}).get('text'),
                        'Vento (km/h)': hour.get('wind_kph'),
                        'Umidade (%)': hour.get('humidity'),
                        'Sensação (°C)': hour.get('feelslike_c'),
                        'Precipitação (mm)': hour.get('precip_mm')
                    })
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 400: # Erro comum para cidade não encontrada
                return None, f"Cidade '{city}' não encontrada. Verifique o nome e tente novamente."
            return None, f"Erro de HTTP ao buscar dados: {e}"
        except requests.exceptions.RequestException as e:
            return None, f"Erro de conexão ao contatar a API: {e}"

    if not all_hourly_data:
        return None, f"Não foram encontrados dados históricos para a cidade '{city}'."
        
    df = pd.DataFrame(all_hourly_data)
    return df, None

@app.route('/', methods=['GET', 'POST'])
def index():
    """ Rota principal que exibe a página e lida com as submissões do formulário. """
    city = 'Belo Horizonte'  # Cidade padrão
    error = None
    df_html = None

    if request.method == 'POST':
        city_from_form = request.form.get('city', '').strip()
        if city_from_form:
            city = city_from_form
        else:
            error = "O nome da cidade não pode estar vazio. Exibindo dados para Belo Horizonte."

    df, error_fetch = fetch_weather_data(city)
    
    if error_fetch:
        error = error_fetch

    if df is not None:
        df_html = df.to_html(classes='data', index=False, border=0)

    return render_template_string(HTML_TEMPLATE, city=city, data=df_html, error=error)

@app.route('/download/excel')
def download_excel():
    """ Rota para gerar e baixar o arquivo Excel com os dados. """
    city = request.args.get('city', 'Belo Horizonte')
    df, error = fetch_weather_data(city)

    if df is None:
        return f"<h1>Erro ao gerar o arquivo para {city}</h1><p>{error}</p>", 404

    output = io.BytesIO() # Cria um buffer de bytes na memória
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Historico_Tempo')
    output.seek(0)
    
    filename = f"historico_tempo_{city.replace(' ', '_').lower()}_{datetime.now().strftime('%Y-%m-%d')}.xlsx"

    return send_file(
        output,
        as_attachment=True,
        download_name=filename,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

if __name__ == '__main__':
    app.run(debug=True)