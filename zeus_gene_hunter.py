 

import urllib.request
import json
import time
from typing import List, Dict

# =====================================================================
# CONFIGURACIÓN DE CRITERIOS DE RECEPTIVIDAD REAL (Filtros v1.5)
# =====================================================================
TARGET_TOPICS = ["foundry", "yul", "account-abstraction", "layer2", "defi-math"]
FORBIDDEN_KEYWORDS = ["meme", "frontend", "interface", "nft-drop", "test-repo"]

class ZeusGeneHunter:
    def __init__(self):
        self.api_url = "https://github.com"
        self.headers = {
            "User-Agent": "Zeus-Gene-Hunter-v1.0",
            "Accept": "application/vnd.github.v3+json"
        }
        self.processed_ids = set()

    def build_query(self) -> str:
        """Construye el vector de búsqueda optimizado para código denso en Base/L2."""
        # Busca repositorios nuevos actualizados recientemente con tópicos de alta ingeniería
        query = "topic:smart-contracts+language:solidity+is:public"
        return f"{self.api_url}{query}&sort=updated&order=desc"

    def scan_network(self) -> List[Dict]:
        """Barre el feed global de GitHub recolectando la materia prima."""
        url = self.build_query()
        req = urllib.request.Request(url, headers=self.headers)
        
        try:
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
                return data.get("items", [])
        except Exception as e:
            print(f"[-] Error de latencia de red en la API de GitHub: {e}")
            return []

    def evaluate_genetic_material(self, repo: Dict) -> bool:
        """Aplica el Filtro Quirúrgico para separar el ruido de la innovación."""
        repo_id = repo.get("id")
        if repo_id in self.processed_ids:
            return False
            
        description = (repo.get("description") or "").lower()
        name = repo.get("name").lower()
        
        # 1. Filtro de exclusión instantáneo de fruta baja/basura
        for word in FORBIDDEN_KEYWORDS:
            if word in description or word in name:
                return False
                
        # 2. Verificación de coincidencia estructural (Banda de Alta Amplitud)
        score = 0
        for topic in TARGET_TOPICS:
            if topic in description or topic in repo.get("topics", []):
                score += 1
                
        self.processed_ids.add(repo_id)
        return score >= 1  # Requiere al menos un nodo matemático verificado

    def execute_cradle(self):
        """Ciclo de reloj continuo del motor de búsqueda."""
        print("[+] Inicializando busqueda de materia prima explotable...")
        print("[+] ZEUS-GENE-HUNTER v1.0 operando en segundo plano en la laptop.\n")
        
        # Simulación de barrido (1 ciclo para control de consola local)
        raw_items = self.scan_network()
        candidates_found = 0
        
        for item in raw_items[:15]:  # Analiza los 15 más frescos del bloque de tiempo
            if self.evaluate_genetic_material(item):
                candidates_found += 1
                print(f"================================================================")
                print(f"💎 MATERIA PRIMA IDENTIFICADA: {item.get('full_name')}")
                print(f"🔗 URL DE EXTRACCIÓN: {item.get('html_url')}/archive/refs/heads/master.zip")
                print(f"📝 DESCRIPCIÓN MACRO: {item.get('description')}")
                print(f"================================================================\n")
                
        if candidates_found == 0:
            print("[•] Ciclo finalizado: No se detectó innovación matemática vacante en este bloque.")

if __name__ == "__main__":
    hunter = ZeusGeneHunter()
    hunter.execute_cradle()
