import json
from conexao import conectar, executar

def carregar_inventario(caminho="inventario.json"):
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    dispositivos = carregar_inventario()
    comandos = ["hostname", "whoami", "uptime -p"]
    
    print("=== INICIANDO COLETA EM LOTE ===\n")
    
    for dev in dispositivos:
        print(f"--- Conectando ao dispositivo: {dev['nome']} ({dev['usuario']}@{dev['host']}) ---")
        try:
            cliente = conectar(dev)
            for cmd in comandos:
                codigo, saida, erro = executar(cliente, cmd)
                if codigo == 0:
                    print(f"  [OK] {cmd} -> {saida}")
                else:
                    print(f"  [ERRO] {cmd} -> {erro}")
            cliente.close()
        except Exception as e:
            print(f"  [FALHA DE CONEXÃO] Não foi possível conectar a {dev['nome']}: {e}")
        print()
        
    print("=== COLETA FINALIZADA ===")

if __name__ == "__main__":
    main()
