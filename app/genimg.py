import google.generativeai as gemini
#ver api que gera img
API_KEY = "chave_api(add .env)" #api aqui
# Se a chave não for encontrada
if not API_KEY:
    print("ATENÇÃO: A chave de API GEMINI_API_KEY não foi encontrada nas variáveis de ambiente.")
    print("Por favor, defina a variável de ambiente ou substitua 'SUA_API_KEY' abaixo.")
    API_KEY = "AIzaSyDGfaG7gLJccDcHfxn7ooNXEEYzE2THStM" #api aqui
gemini.configure(api_key=API_KEY)
try:
    model = gemini.GenerativeModel('models/gemini-1.5-flash-latest')
    prompt = str(input("digite sua pergunta: "))
    resposta = model.generate_content(
        prompt
        )
    # Imprimir a resposta
    print("\nGemini responde:")
    print(resposta.text)
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    print("Verifique sua chave de API, a quantidade de usos ou a disponibilidade do serviço.")
