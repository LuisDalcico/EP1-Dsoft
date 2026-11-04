from funcoes import define_posicoes
from funcoes import preenche_frota

linha = 2
coluna = 4
orientacao = "vertical"
tamanho = 3

print(define_posicoes(linha, coluna, orientacao, tamanho))

frota = {}
nome_navio = 'navio-tanque'
linha = 6
coluna = 1
orientacao = 'horizontal'
tamanho = 3

resultado = preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
print(resultado)