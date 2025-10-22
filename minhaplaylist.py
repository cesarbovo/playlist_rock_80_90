import json

# Classe Nó: representa cada música da playlist
class No:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista
        self.anterior = None
        self.proximo = None

# Classe Playlist: gerencia as músicas e a navegação
class Playlist:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.atual = None

    def adicionar_musica(self, titulo, artista):
        novo_no = No(titulo, artista)
        if not self.inicio:
            self.inicio = self.fim = self.atual = novo_no
        else:
            self.fim.proximo = novo_no
            novo_no.anterior = self.fim
            self.fim = novo_no
        print(f"Música adicionada: {titulo} - {artista}")

    def remover_musica(self, titulo):
        no = self.inicio
        while no:
            if no.titulo.lower() == titulo.lower():
                if no.anterior:
                    no.anterior.proximo = no.proximo
                else:
                    self.inicio = no.proximo
                if no.proximo:
                    no.proximo.anterior = no.anterior
                else:
                    self.fim = no.anterior
                print(f"Música removida: {titulo}")
                return
            no = no.proximo
        print(f"Música '{titulo}' não encontrada.")

    def avancar(self):
        if self.atual and self.atual.proximo:
            self.atual = self.atual.proximo
            print(f"Tocando agora: {self.atual.titulo} - {self.atual.artista}")
        else:
            print("Fim da playlist ou nenhuma música disponível.")

    def retroceder(self):
        if self.atual and self.atual.anterior:
            self.atual = self.atual.anterior
            print(f"Tocando agora: {self.atual.titulo} - {self.atual.artista}")
        else:
            print("Início da playlist ou nenhuma música disponível.")

    def exibir_playlist(self):
        print("\n--- Playlist Atual ---")
        no = self.inicio
        pos = 1
        while no:
            atual_str = " <= Tocando agora" if no == self.atual else ""
            print(f"{pos}. {no.titulo} - {no.artista}{atual_str}")
            no = no.proximo
            pos += 1

    def salvar_em_json(self, nome_arquivo="playlist.json"):
        musicas = []
        no = self.inicio
        while no:
            musicas.append({"titulo": no.titulo, "artista": no.artista})
            no = no.proximo
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            json.dump(musicas, f, ensure_ascii=False, indent=4)
        print("Playlist salva em JSON!")

    def carregar_de_json(self, nome_arquivo="playlist.json"):
        try:
            with open(nome_arquivo, "r", encoding="utf-8") as f:
                musicas = json.load(f)
                for m in musicas:
                    self.adicionar_musica(m["titulo"], m["artista"])
            print("Playlist carregada do JSON!")
        except FileNotFoundError:
            print("Arquivo JSON não encontrado.")


# Função principal com menu interativo
def menu():
    playlist = Playlist()

    # Adiciona músicas iniciais de rock nacional anos 80 e 90
    musicas_iniciais = [
        ("Pro Dia Nascer Feliz", "Barão Vermelho"),
        ("Tempo Perdido", "Legião Urbana"),
        ("Primeiros Erros", "Capital Inicial"),
        ("Inútil", "Ultraje a Rigor"),
        ("Envelheço na Cidade", "Ira!"),
        ("Que País É Este", "Legião Urbana"),
        ("O Tempo Não Para", "Cazuza"),
        ("Exagerado", "Cazuza"),
        ("Será", "Legião Urbana"),
        ("Pelados em Santos", "Mamonas Assassinas"),
    ]
    for titulo, artista in musicas_iniciais:
        playlist.adicionar_musica(titulo, artista)

    while True:
        print("""
=== Playlist - Estrutura de Dados ===
1. Adicionar música
2. Remover música
3. Avançar
4. Retroceder
5. Exibir playlist
6. Salvar em JSON
7. Carregar de JSON
8. Sair
""")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título da música: ")
            artista = input("Artista ou banda: ")
            playlist.adicionar_musica(titulo, artista)
        elif opcao == "2":
            titulo = input("Título da música a remover: ")
            playlist.remover_musica(titulo)
        elif opcao == "3":
            playlist.avancar()
        elif opcao == "4":
            playlist.retroceder()
        elif opcao == "5":
            playlist.exibir_playlist()
        elif opcao == "6":
            playlist.salvar_em_json()
        elif opcao == "7":
            playlist.carregar_de_json()
        elif opcao == "8":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Execução do programa
if __name__ == "__main__":
    menu()

