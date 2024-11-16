import csv

def calcular_imc(peso, altura):
    """Calcula o Índice de Massa Corporal (IMC)."""
    return peso / (altura ** 2)

def interpretar_imc(imc, idioma="pt"):
    """Interpreta o IMC com base na classificação da OMS."""
    classificacoes = {
        "pt": [
            ("Magreza grave", "Consulte um médico imediatamente."),
            ("Magreza moderada", "Acompanhamento médico recomendado."),
            ("Magreza leve", "Considere ajustar sua dieta para ganho de peso saudável."),
            ("Peso normal", "Mantenha hábitos saudáveis!"),
            ("Sobrepeso", "Avalie sua dieta e pratique atividades físicas."),
            ("Obesidade grau I", "Considere consultar um profissional de saúde."),
            ("Obesidade grau II", "Intervenção médica é recomendada."),
            ("Obesidade grau III", "Procure ajuda médica com urgência."),
        ],
        "en": [
            ("Severe thinness", "See a doctor immediately."),
            ("Moderate thinness", "Medical monitoring recommended."),
            ("Mild thinness", "Consider adjusting your diet for healthy weight gain."),
            ("Normal weight", "Maintain healthy habits!"),
            ("Overweight", "Evaluate your diet and practice physical activities."),
            ("Obesity grade I", "Consider consulting a health professional."),
            ("Obesity grade II", "Medical intervention recommended."),
            ("Obesity grade III", "Seek urgent medical attention."),
        ],
    }
    
    if imc < 16:
        return classificacoes[idioma][0]
    elif 16 <= imc < 17:
        return classificacoes[idioma][1]
    elif 17 <= imc < 18.5:
        return classificacoes[idioma][2]
    elif 18.5 <= imc < 25:
        return classificacoes[idioma][3]
    elif 25 <= imc < 30:
        return classificacoes[idioma][4]
    elif 30 <= imc < 35:
        return classificacoes[idioma][5]
    elif 35 <= imc < 40:
        return classificacoes[idioma][6]
    else:
        return classificacoes[idioma][7]

def obter_recomendacoes(imc, idade, idioma="pt"):
    """Oferece recomendações personalizadas com base no IMC e idade."""
    if idioma == "pt":
        if imc < 18.5:
            return [
                "Inclua alimentos ricos em calorias e nutrientes na sua dieta, como nozes e abacate.",
                "Pratique exercícios de força para ganhar massa muscular.",
            ]
        elif imc < 25:
            return [
                "Continue mantendo uma dieta equilibrada.",
                "Realize exames regulares para monitorar sua saúde.",
            ]
        elif imc < 30:
            return [
                "Reduza a ingestão de alimentos processados e açúcares.",
                "Incorpore exercícios aeróbicos e de força à sua rotina.",
            ]
        else:
            return [
                "Consulte um nutricionista para criar um plano alimentar personalizado.",
                "Considere atividades de baixo impacto, como caminhada ou natação.",
            ]
    else:
        if imc < 18.5:
            return [
                "Include calorie-dense and nutrient-rich foods in your diet, like nuts and avocado.",
                "Practice strength exercises to gain muscle mass.",
            ]
        elif imc < 25:
            return [
                "Keep maintaining a balanced diet.",
                "Get regular check-ups to monitor your health.",
            ]
        elif imc < 30:
            return [
                "Reduce the intake of processed foods and sugars.",
                "Incorporate aerobic and strength exercises into your routine.",
            ]
        else:
            return [
                "Consult a nutritionist to create a personalized meal plan.",
                "Consider low-impact activities like walking or swimming.",
            ]

def salvar_historico(nome, peso, altura, idade, imc, classificacao, idioma="pt"):
    """Salva os dados em um arquivo CSV."""
    arquivo = "historico_imc.csv"
    cabecalho = ["Nome", "Peso (kg)", "Altura (m)", "Idade", "IMC", "Classificação", "Idioma"]
    dados = [nome, peso, altura, idade, f"{imc:.2f}", classificacao, idioma]

    try:
        with open(arquivo, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            if csvfile.tell() == 0:  # Arquivo vazio? Escreva o cabeçalho
                writer.writerow(cabecalho)
            writer.writerow(dados)
    except Exception as e:
        print(f"Erro ao salvar histórico: {e}")
