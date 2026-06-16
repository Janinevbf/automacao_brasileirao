import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO

def obter_tabela_brasileirao():
    print("🔄 Conectando ao site Chance de Gol e gerando a tabela...")
    
    url = "https://www.chancedegol.com.br/br26.htm"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            response.encoding = 'utf-8' 
            soup = BeautifulSoup(response.text, 'html.parser')
            tabelas = pd.read_html(str(soup))
            
            df_tabela = None
            for t in tabelas:
                if 'Probab. de' in str(t.values) or 'Título' in str(t.values):
                    df_tabela = t
                    break
            
            if df_tabela is not None:
                print("\n🏆 CLASSIFICAÇÃO ATUALIZADA DO BRASILEIRÃO 🏆\n")
                print(df_tabela.to_markdown(index=False))
                print("\n📊 Automação executada com sucesso!")
            else:
                print("\n🏆 CLASSIFICAÇÃO ATUALIZADA DO BRASILEIRÃO 🏆\n")
                print(tabelas[0].to_markdown(index=False))
        else:
            print(f"❌ Não foi possível acessar o site. Status: {response.status_code}")
            
    except Exception as e:
        print(f"💥 Ocorreu um erro ao processar: {e}")

if __name__ == "__main__":
    obter_tabela_brasileirao()