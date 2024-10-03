# Heurística Retorno/custo, escolhe sempre o investimento com a melhor relação retorno/custo,
# sem tentar calcular todas as possíveis combinações. 
# Ele faz uma boa escolha local em cada passo e, ao final, 
# espera-se que essa estratégia gere um resultado próximo ao ideal. 
# No entanto, não há garantias de que o resultado seja o melhor possível.

# Definindo os investimentos: (nome, custo, retorno)
investimentos = [
    ("Ações de Empresa X", 30000, 40000),
    ("Ações de Empresa Y", 50000, 60000),
    ("Imóvel Z", 40000, 45000),
    ("Títulos públicos P", 10000, 15000),
    ("Fundo de investimento F", 20000, 25000)
]

# Definindo o orçamento disponível
orcamento = 100000

# Calculando a razão retorno/custo
investimentos_ordenados = sorted(investimentos, key=lambda x: x[2] / x[1], reverse=True)

# Selecionando os investimentos
custo_total = 0
retorno_total = 0
investimentos_selecionados = []

for investimento in investimentos_ordenados:
    nome, custo, retorno = investimento
    # Se ainda houver orçamento, adicionar o investimento
    if custo_total + custo <= orcamento:
        investimentos_selecionados.append(investimento)
        custo_total += custo
        retorno_total += retorno

# Exibindo os resultados
print("Investimentos selecionados:")
for inv in investimentos_selecionados:
    print(f"{inv[0]}: Custo = R${inv[1]:,.2f}, Retorno = R${inv[2]:,.2f}")

print(f"\nCusto total: R${custo_total:,.2f}")
print(f"Retorno total: R${retorno_total:,.2f}")
