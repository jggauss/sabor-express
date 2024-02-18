from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praca', 'gourmet')
#restaurante_mexicano = Restaurante('Mexican Food', 'mexicana')
#restaurante_japones = Restaurante('Japa','japonesa')
#restaurante_praca.receber_avaliacao('Gui',1)
#restaurante_praca.receber_avaliacao('Gauss',4)
#restaurante_praca.receber_avaliacao('Luisa',3)

bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho', 2.0,'Melho pão da cidade')
prato_paozinho.aplicar_desconto()
restaurante_praca.adiconar_no_cardapio(bebida_suco)
restaurante_praca.adiconar_no_cardapio(prato_paozinho)

#restaurante_praca.alternar_estado()


def main():
    restaurante_praca.exibir_cardapio
    
    pass

if __name__== '__main__':
    main()