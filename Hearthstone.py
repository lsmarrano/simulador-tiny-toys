import json
import random

# Transformando arquivo .json em um dictionary
jsonfile = open('cards.json', encoding="utf8").read()
cards = json.loads(jsonfile)

# Criando listas para serem usadas mais a frente
images = []
urls = []
name = []

# Simularemos a carta no Modo Padrão, que consiste nesses 6 sets:
standard = ['STORMWIND', 'THE_BARRENS', 'DARKMOON_FAIRE', 'SCHOLOMANCE', 'CORE', 'BLACK_TEMPLE']

# Teremos uma lista 'names' com o nome de todas as cartas possiveis de serem invocadas e uma 'image' com seus
# respectivos IDs, que serão usadas para gerar a imagem da carta
for card in cards:

	# Excluindo cartas sem custo e não colecionaveis
	if 'cost' and 'collectible' in card:

		craftable = (card['collectible'])
		card_set = (card['set'])
		minion = (card['type'])

		# Selecionando apenas as cartas craftaveis
		if craftable is True:

			# Selecionando cartas do Modo Padrão e excluindo feitiços
			if card_set in standard and minion == 'MINION':
				five_cost = card['cost'] == 5
				minion = card['type'] == 'MINION'

				#Dentro do Modo Padrão selecionando todos os minions custo 5 e pegando nome + ID
				if five_cost:

					images.append((card['id']))
					name.append((card['name']))

#Gerando link para visualização da carta
for i in images:

	urllink = "https://art.hearthstonejson.com/v1/render/latest/enUS/512x/" + i +".png"
	urls.append(urllink)

#Função para gerar um minion aleatório
def gerar_minion():
	numero = random.randrange(0, len(images))
	image_minion = images[numero]
	name_minion = name[numero]
	print("https://art.hearthstonejson.com/v1/render/latest/enUS/512x/" + image_minion + ".png")
	print(name_minion)

#Gerando 4 minions aleatórios
gerar_minion()
gerar_minion()
gerar_minion()
gerar_minion()