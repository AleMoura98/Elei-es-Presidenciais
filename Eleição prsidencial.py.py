def eleicao_presidencial():
    """
    Simula uma eleição presidencial, contabiliza os votos e exibe os resultados.
    """
    # Dicionário para mapear os códigos dos candidatos aos seus nomes
    candidatos = {
        1: "Alex",
        2: "Gustavo",
        3: "José",
        4: "Soraya"
    }

    # Inicializa os contadores de votos para cada categoria
    votos_candidatos = {1: 0, 2: 0, 3: 0, 4: 0}
    votos_nulos = 0
    votos_em_branco = 0
    total_votos = 0

    print("Bem-vindo à eleição presidencial!")
    print("Por favor, insira os votos conforme os códigos:")
    # Exibe a tabela de códigos e nomes dos candidatos
    for codigo, nome in candidatos.items():
        print(f"{codigo} - {nome}")
    print("5 - Voto Nulo")
    print("6 - Voto em Branco")
    print("0 - Para finalizar a votação")

    # Loop principal para receber os votos
    while True:
        try:
            # Solicita o voto ao usuário
            voto = int(input("Digite seu voto (ou 0 para finalizar): "))

            # Verifica se o usuário deseja finalizar a votação
            if voto == 0:
                print("Votação finalizada. Processando resultados...")
                break
            # Contabiliza votos para os candidatos
            elif voto in candidatos:
                votos_candidatos[voto] += 1
                total_votos += 1
            # Contabiliza votos nulos
            elif voto == 5:
                votos_nulos += 1
                total_votos += 1
            # Contabiliza votos em branco
            elif voto == 6:
                votos_em_branco += 1
                total_votos += 1
            # Lida com códigos de voto inválidos
            else:
                print("Código de voto inválido. Por favor, digite um código válido.")
        except ValueError:
            # Lida com entradas não numéricas
            print("Entrada inválida. Por favor, digite um número inteiro.")

    # --- Exibição dos Resultados ---
    print("\n--- Resultados Finais da Eleição ---")

    # 1. Total de votos para cada candidato
    print("\nTotal de votos por candidato:")
    for codigo, nome in candidatos.items():
        print(f"{nome}: {votos_candidatos[codigo]} votos")

    # 2. Total de votos nulos
    print(f"\nTotal de votos nulos: {votos_nulos} votos")

    # 3. Total de votos em branco
    print(f"Total de votos em branco: {votos_em_branco} votos")

    # Calcula e exibe as percentagens (evita divisão por zero)
    if total_votos > 0:
        # 4. Percentagem de votos nulos sobre o total de votos
        percentagem_nulos = (votos_nulos / total_votos) * 100
        print(f"Percentagem de votos nulos sobre o total: {percentagem_nulos:.2f}%")

        # 5. Percentagem de votos em branco sobre o total de votos
        percentagem_em_branco = (votos_em_branco / total_votos) * 100
        print(f"Percentagem de votos em branco sobre o total: {percentagem_em_branco:.2f}%")

        # 6. Determina o candidato que venceu as eleições
        vencedor = None
        max_votos_candidato = -1

        # Encontra o candidato com o maior número de votos
        for codigo, votos in votos_candidatos.items():
            if votos > max_votos_candidato:
                max_votos_candidato = votos
                vencedor = candidatos[codigo]
            elif votos == max_votos_candidato:
                # Caso haja empate entre dois ou mais candidatos,
                # a lógica a seguir pode ser expandida para tratar melhor.
                # Aqui, simplesmente indicamos que houve um empate.
                if vencedor and vencedor != "Empate": # Verifica se já não foi marcado como empate
                    vencedor = "Empate"
                elif not vencedor: # Primeiro empate encontrado
                    vencedor = "Empate"


        print("\n--- Resultado da Eleição ---")
        if max_votos_candidato == 0 and total_votos > 0:
            # Se não houve votos válidos para nenhum candidato, verifica nulos/brancos
            print("Não houve votos válidos para determinar um vencedor entre os candidatos.")
            if votos_nulos > votos_em_branco:
                print("Os votos nulos foram maioria.")
            elif votos_em_branco > votos_nulos:
                print("Os votos em branco foram maioria.")
            elif votos_nulos > 0: # Nulos e brancos iguais e maiores que zero
                print("Os votos nulos e em branco tiveram a mesma quantidade.")
        elif vencedor == "Empate":
            # Listar todos os candidatos que empataram
            candidatos_empatados = [nome for codigo, nome in candidatos.items() if votos_candidatos[codigo] == max_votos_candidato]
            print(f"Houve um empate entre os candidatos: {', '.join(candidatos_empatados)} com {max_votos_candidato} votos cada.")
        elif vencedor:
            print(f"O candidato vencedor é: {vencedor} com {max_votos_candidato} votos.")
        else:
            print("Não houve votos válidos para determinar um vencedor entre os candidatos.")
    else:
        print("Nenhum voto foi registrado nesta eleição.")

# Chama a função para executar o programa da eleição
eleicao_presidencial()
