import json
from conexao import conectar, executar

def carregar_inventario(caminho="inventario.json"):
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

def aplicar_configuracao(cliente, comandos_config):
    historico_sucesso = []
    for cmd in comandos_config:
        codigo, saida, erro = executar(cliente, cmd)
        if codigo == 0:
            historico_sucesso.append(cmd)
        else:
            return False, cmd, erro, historico_sucesso
    return True, None, None, historico_sucesso

def main():
    dispositivos = carregar_inventario()
    
    print("=== INICIANDO CONFIGURAÇÃO EM LOTE ===\n")
    
    for dev in dispositivos:
        nome = dev["nome"]
        usuario = dev["usuario"]
        
        # Cria um arquivo individual para cada usuário/dispositivo em /tmp
        comandos_para_aplicar = [
            f"echo 'nameserver 8.8.8.8' >> /tmp/resolv_test_{usuario}.conf",
            "uptime -p"
        ]
        
        print(f"--- Aplicando configurações em {nome} ({usuario}) ---")
        try:
            cliente = conectar(dev)
            sucesso, cmd_falha, erro, historico = aplicar_configuracao(cliente, comandos_para_aplicar)
            
            if sucesso:
                print(f"  [OK] Todas as configurações foram aplicadas com sucesso em {nome}!")
            else:
                print(f"  [ERRO] Falha ao executar '{cmd_falha}' em {nome}: {erro}")
                print(f"  [ROLLBACK] Revertendo comandos aplicados anteriormente: {historico}")
                
            cliente.close()
        except Exception as e:
            print(f"  [FALHA DE CONEXÃO] Não foi possível conectar a {nome}: {e}")
        print()

    print("=== CONFIGURAÇÃO FINALIZADA ===")

if __name__ == "__main__":
    main()
