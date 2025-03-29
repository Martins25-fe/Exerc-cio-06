import schedule
import time

def executar_analise():
    print("Executando análise...")
    # Chame aqui a função principal do seu script de análise

# Agendar para rodar todos os dias às 9h
schedule.every().day.at("09:00").do(executar_analise)

while True:
    schedule.run_pending()
    time.sleep(60)  # Aguarda um minuto antes de verificar novamente





