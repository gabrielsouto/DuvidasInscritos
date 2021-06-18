import os

def bytes_to_mb(qntbytes):
    return str(round(qntbytes/1048576, 2)).replace('.', ',')

def bytes_to_gb(qntbytes):
    return str(round(qntbytes/1073741824, 2)).replace('.', ',')

def porcentagem(espaco_usado, total):
    return str(round(espaco_usado*100/total, 2)).replace('.', ',')

if os.path.exists("usuarios.txt"):
    
    with open("usuarios.txt", "r", encoding="utf-8") as usuarios_espacos_txt:
        usuarios_espacos = usuarios_espacos_txt.read().split("\n")
        
        if len(usuarios_espacos) > 0:
            dados_relatorio = {}
            espaco_total_ocupado = 0
            espaco_total = 42949650970
                
            for indice_usuario_espaco in range(len(usuarios_espacos)):
                usuario_espaco = usuarios_espacos[indice_usuario_espaco].split()
                dados_relatorio[usuario_espaco[0]] = int(usuario_espaco[2])
                espaco_total_ocupado += int(usuario_espaco[2])
            
            with open("relatório.txt", "wt", encoding="utf-8") as arquivo_relatorio:
                arquivo_relatorio.write("Uso do espaço em disco pelos usuários\n")
                arquivo_relatorio.write("-" * 62 + "\n")
                
                arquivo_relatorio.write("Nr.".ljust(5))
                arquivo_relatorio.write("Usuário".ljust(15))
                arquivo_relatorio.write("Espaço utilizado".ljust(21))
                arquivo_relatorio.write("% do uso".ljust(9) + "\n\n")
                
                for indice_usuario_espaco, usuario in enumerate(sorted(dados_relatorio, key=dados_relatorio.get, reverse=True)):
                    arquivo_relatorio.write(str(indice_usuario_espaco+1).ljust(5))
                    arquivo_relatorio.write(usuario.ljust(15))
                    arquivo_relatorio.write(bytes_to_mb(int(dados_relatorio[usuario])).rjust(7)+" MB           ")
                    arquivo_relatorio.write(porcentagem(int(dados_relatorio[usuario]), espaco_total).rjust(7)+"%\n")
                    
                arquivo_relatorio.write("\nEspaço total ocupado: " + bytes_to_mb(espaco_total_ocupado) + " MB\n")
                arquivo_relatorio.write("Espaço médio ocupado: " + bytes_to_mb(espaco_total_ocupado/len(usuarios_espacos)) + " MB\n")
                arquivo_relatorio.write("Espaço total livre: " + bytes_to_gb(espaco_total - espaco_total_ocupado) + " GB")
else:
    print("O arquivo usuarios.txt não existe")
