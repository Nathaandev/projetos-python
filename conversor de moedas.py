import json
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer

taxas = {
    'real_para_dolar': 0.20,
    'dolar_para_real': 4.96,
    'real_para_euro': 0.19,
    'euro_para_real': 5.32,
    'dolar_para_euro': 0.93,
    'euro_para_dolar':1.07
}

class ConversorMoedas(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/converter'):
            partes_url = urlparse(self.path)
            consulta = parse_qs(partes_url.query)
            valor = float(consulta['valor'][0])
            moeda_origem = consulta['moeda_origem'][0]
            moeda_destino = consulta['moeda_destino'][0]
            resultado = self.converter_moeda(valor, moeda_origem, moeda_destino)
            self.send_response(200)
            self.send_header('content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(resultado).encode())
        else:
            self.send_response(404)
            self.end_headers()
    def converter_moeda(self, valor, moeda_origem, moeda_destino):
        valor_convertido = 0
        if moeda_origem == 'real' and moeda_destino == 'dolar':
            valor_convertido = valor * taxas['real_para_dolar']
        elif moeda_origem == 'dolar' and moeda_destino == 'real':
            valor_convertido = valor * taxas['dolar_para_real']
        elif moeda_origem == 'real' and moeda_destino == 'euro':
            valor_convertido = valor * taxas['real_para_euro']
        elif moeda_origem == 'euro' and moeda_destino == 'real':
            valor_convertido = valor * taxas['euro_para_real']
        elif moeda_origem == 'dolar' and moeda_destino == 'euro':
            valor_convertido = valor * taxas['dolar_para_euro']
        elif moeda_origem == 'euro' and moeda_destino == 'dolar':
            valor_convertido = valor * taxas['euro_para_dolar']
        
        return {
            'valor convertido': valor_convertido,
            'moeda': moeda_destino.upper()
        }

host = 'localhost'
porta = 8000

def executar_servidor():
    endereço_servidor = (host, porta)
    httpd = HTTPServer(endereço_servidor, ConversorMoedas)
    print(f'Servidor rodando em https://{host}:{porta}')
    httpd.serve_forever()

if __name__ == '__main__':
    executar_servidor()

            
