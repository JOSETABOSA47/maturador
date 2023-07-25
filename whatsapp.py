from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
import random
import time
from selenium.webdriver.common.keys import Keys
from functools import partial
from selenium.webdriver.support.ui import (
    WebDriverWait
)


conversas = [
    "Olá, como vai?",
    "Tudo bem?",
    "Qual é o seu nome?",
    "Qual é a sua idade?",
    "O que você gosta de fazer?",
    "Você tem algum hobby?",
    "Qual é o seu time do coração?",
    "Qual é a sua banda favorita?",
    "Você gosta de filmes de terror?",
    "Qual é o seu filme favorito?",
    "Você tem algum animal de estimação?",
    "Você gosta de viajar?",
    "Qual é o seu lugar favorito?",
    "Você já visitou algum país estrangeiro?",
    "Você sabe cozinhar?",
    "Qual é o seu prato favorito?",
    "Você gosta de jogar videogame?",
    "Qual é o seu jogo favorito?",
    "Você já leu algum livro interessante?",
    "Qual é o seu autor favorito?",
    "Você gosta de esportes?",
    "Qual é o seu esporte favorito?",
    "Você já praticou algum esporte?",
    "Você gosta de academia?",
    "Qual é o seu exercício favorito?",
    "Você tem algum talento?",
    "Qual é o seu sonho?",
    "Você gosta de música?",
    "Qual é o seu estilo musical favorito?",
    "Qual é a sua música favorita?",
    "Você já foi a algum show?",
    "Você gosta de dançar?",
    "Qual é o seu estilo de dança favorito?",
    "Você já fez aulas de dança?",
    "Você gosta de pintura?",
    "Qual é o seu estilo de arte favorito?",
    "Você já visitou algum museu?",
    "Você gosta de ler notícias?",
    "Qual é o seu site de notícias favorito?",
    "Qual é o seu assunto favorito?",
    "Você gosta de tecnologia?",
    "Qual é o seu gadget favorito?",
    "Você já visitou alguma feira de tecnologia?",
    "Você gosta de carros?",
    "Qual é o seu carro favorito?",
    "Você já dirigiu algum carro interessante?",
    "Você gosta de fotografia?",
    "Qual é o seu tema favorito para fotografar?",
    "Você já visitou algum lugar interessante para fotografar?",
    "Eu adoro viajar para lugares diferentes e experimentar novas culturas.",
    "Não consigo decidir entre ir ao cinema ou sair para jantar, o que você prefere?",
    "Eu tenho um cachorro que adora passear no parque, você tem algum animal de estimação?",
    "Ultimamente, tenho gostado de cozinhar pratos diferentes, você tem alguma receita interessante para compartilhar?",
    "Você já visitou algum lugar que sempre sonhou em conhecer?",
    "Eu adoro ler livros de ficção científica, e você, qual é o seu gênero literário favorito?",
    "Eu estou planejando fazer uma viagem para a praia nas próximas férias, você já visitou alguma praia que gostaria de recomendar?",
    "Eu sou fã de esportes, especialmente de futebol, você acompanha algum esporte ou time?",
    "Eu trabalho como engenheiro de software, e você, qual é a sua profissão?",
    "Eu gosto de praticar yoga para relaxar, você já experimentou alguma prática de meditação ou mindfulness?",
    "Eu adoro passar tempo ao ar livre e fazer trilhas na natureza.",
    "Eu realmente gostei do filme que assisti ontem à noite, recomendo que você assista também.",
    "Eu tenho um grupo de amigos muito legal com quem gosto de sair e fazer atividades diferentes.",
    "Eu estou sempre em busca de novos desafios e oportunidades para aprender coisas novas.",
    "Eu sou muito grato pela minha família e amigos, eles são uma grande fonte de apoio e felicidade para mim.",
    "Eu me sinto muito feliz quando estou em contato com a natureza, especialmente na praia ou em um parque.",
    "Eu gosto de experimentar diferentes tipos de comidas e sabores, e adoro cozinhar em casa para minha família e amigos.",
    "Eu acredito que a prática regular de exercícios físicos é essencial para a saúde e o bem-estar.",
    "Eu sempre tento ser positivo e manter uma atitude otimista, mesmo diante de situações desafiadoras.",
    "Eu gosto de viajar e explorar novos lugares, e acho que viajar é uma das melhores maneiras de expandir nossos horizontes e aprender sobre outras culturas.",
    "Não posso ir ao cinema hoje à noite, estou ocupado.",
    "Não gosto muito de comida apimentada.",
    "Não tive um bom dia hoje, estou um pouco estressado.",
    "Não quero falar sobre esse assunto agora, podemos mudar de assunto?",
    "Não acho que eu vá conseguir terminar esse projeto a tempo.",
    "Não me sinto muito confortável em grandes aglomerações de pessoas.",
    "Não sou muito fã de esportes radicais, prefiro atividades mais tranquilas.",
    "Não tive uma boa experiência com esse restaurante da última vez que fui lá.",
    "Não gosto de acordar cedo, sou mais uma pessoa noturna.",
    "Não estou muito animado com essa ideia de viagem, acho que prefiro ficar em casa.",
    "Que belo dia de sol!",
    "Uau, que vista incrível!",
    "Incrível, você conseguiu!",
    "Que festa animada!",
    "Que linda roupa você está usando!",
    "Uau, que performance impressionante!",
    "Parabéns, você arrasou!",
    "Que delícia de comida!",
    "Que surpresa maravilhosa!",
    "Que ideia brilhante!",
    "Uau, que voz poderosa!",
    "Que jogo emocionante!",
    "Que adorável gesto de carinho!",
    "Que talento extraordinário!",
    "Que conquista incrível!",
    "Que alívio, finalmente deu certo!",
    "Uau, que presente surpreendente!",
    "Que emoção, estou sem palavras!",
    "Que dia inesquecível!",
    "Que figura impressionante!",
    "Que piada engraçada, ri muito!",
    "Que obra-prima magnífica!",
    "Uau, que velocidade impressionante!",
    "Que festa divertida, não quero que acabe!",
    "Que atitude corajosa, você é incrível!",
    "Que gesto generoso, você tem um coração de ouro!",
    "Uau, que habilidade incrível!",
    "Que lugar encantador, estou maravilhado!",
    "Que lindo gesto de amor!",
    "Que saudade imensa!",
    "Uau, que vitória espetacular!",
    "Que solução inteligente, parabéns!",
    "Que surpresa agradável, não esperava por isso!",
    "Uau, que voz angelical!",
    "Que momento mágico, vou guardar para sempre!",
    "Estou radiante de felicidade!",
    "Que alegria contagiante!",
    "Estou pulando de alegria!",
    "Que sensação maravilhosa de contentamento!",
    "Estou sorrindo de orelha a orelha!",
    "Alegria pura e genuína!",
    "Meu coração está transbordando de alegria!",
    "Que felicidade imensa, não consigo conter!",
    "Estou nas nuvens de tanta alegria!",
    "A alegria é o combustível da minha alma!",
    "Que momento feliz, quero aproveitar cada segundo!",
    "Estou transbordando de gratidão e alegria!",
    "Que sorriso iluminado pela felicidade!",
    "A alegria é a trilha sonora da minha vida!",
    "Que alegria imensa em meu coração!",
    "Estou exultante de alegria e entusiasmo!",
    "Que felicidade contida em cada célula do meu ser!",
    "Estou vivendo um momento de pura alegria e êxtase!",
    "Que sensação maravilhosa de plenitude e alegria!",
    "Estou dançando de felicidade!",
    "A alegria é como um sol brilhante que ilumina meus dias!",
    "Que felicidade transbordante que me envolve por completo!",
    "Estou flutuando nas asas da alegria!",
    "Que alegria indescritível que aquece minha alma!",
    "A alegria é a música que embala minha existência!",
    "Estou repleto de alegria, não há espaço para tristeza!",
    "Que felicidade contagiosa, quero compartilhar com todos!",
    "Estou no paraíso da felicidade, não poderia estar melhor!",
    "Que alegria genuína e plena que me envolve por completo!",
    "A felicidade é o perfume que exala de mim, onde quer que eu vá!",
    "Que carro esportivo incrível!",
    "Uau, essa moto é uma máquina!",
    "Que barco luxuoso e elegante!",
    "Que avião imponente e poderoso!",
    "Adoro dirigir um carro potente!",
    "Essa moto tem um design incrível!",
    "Adoro navegar em um barco pelo mar!",
    "Viajar de avião é uma experiência única!",
    "Que carro clássico e cheio de estilo!",
    "Essa moto é uma verdadeira obra de arte sobre rodas!",
    "Adoro a sensação de liberdade ao velejar em um barco!",
    "Viajar de avião me faz sentir como se estivesse voando!",
    "Que carro familiar espaçoso e confortável!",
    "Essa moto tem um motor poderoso e impressionante!",
    "Adoro fazer passeios de barco e explorar novos lugares!",
    "Viajar de avião me permite conhecer o mundo de maneira rápida e eficiente!",
    "Que carro conversível, perfeito para curtir o vento no rosto!",
    "Essa moto tem uma aceleração incrível, é pura adrenalina!",
    "Adoro relaxar em um barco, aproveitando a tranquilidade do mar!",
    "Viajar de avião me permite chegar a lugares distantes e explorar culturas diferentes!",
    "Que carro todo-terreno, capaz de enfrentar qualquer desafio!",
    "Essa moto de corrida é simplesmente incrível, uma máquina veloz!",
    "Adoro passear de barco em lagos e rios, apreciando a natureza ao redor!",
    "Viajar de avião é emocionante, especialmente durante decolagens e pousos!",
    "Que carro de luxo, repleto de conforto e tecnologia de ponta!",
    "Essa moto customizada é única, reflete a personalidade do seu dono!",
    "Adoro fazer passeios de barco em ilhas paradisíacas, é como estar em um sonho!",
    "Viajar de avião me proporciona uma perspectiva incrível das paisagens lá embaixo!",
    "Que delícia relaxar em uma rede à sombra das árvores!",
    "Uau, que diversão incrível em um parque de diversões!",
    "Que prazer é desfrutar de um bom livro em uma tarde tranquila!",
    "Incrível, adoro jogar futebol com os amigos no final de semana!",
    "Que maravilha é explorar trilhas ecológicas em contato com a natureza!",
    "Uau, que animação em uma festa com amigos e música animada!",
    "Que alegria é brincar com meus filhos em um parquinho!",
    "Incrível, adoro passar horas pintando e expressando minha criatividade!",
    "Que delícia é se refrescar em uma piscina em um dia quente de verão!",
    "Uau, que emoção é praticar esportes radicais como paraquedismo ou surfe!",
    "Que paz é fazer meditação e encontrar equilíbrio interior!",
    "Incrível, adoro viajar e explorar novos lugares e culturas!",
    "Que maravilha é saborear um jantar delicioso em um restaurante aconchegante!",
    "Uau, que emoção é assistir a um espetáculo teatral ou musical de tirar o fôlego!",
    "Que alegria é passar tempo com a família em um piquenique no parque!",
    "Incrível, adoro tocar um instrumento musical e criar melodias cativantes!",
    "Que delícia é curtir um dia na praia, com sol, mar e areia!",
    "Uau, que animação é participar de um festival de música e dançar até cansar!",
    "Que prazer é jogar videogame e entrar em aventuras virtuais emocionantes!",
    "Incrível, adoro praticar ioga e desfrutar de paz e harmonia interior!",
    "Que maravilha é desfrutar de um bom filme no cinema, com pipoca e refrigerante!",
    "Uau, que diversão é se reunir com amigos para jogar jogos de tabuleiro!",
    "Que alegria é passear em um parque temático e aproveitar os brinquedos radicais!",
    "Incrível, adoro fazer caminhadas e explorar belas paisagens naturais!",
    "Que delícia é cozinhar e experimentar novas receitas na cozinha!",
    "Uau, que animação é participar de uma maratona ou corrida de rua com outros atletas!",
    "Que prazer é fazer sessões de massagem e relaxamento para cuidar do corpo e da mente!",

]


def lista_maturacao(telefone_conectado, lista_numeros_maturacao):
    lista_maturacao = []
    lista_maturacao = list(lista_numeros_maturacao)
    for x in lista_maturacao:
        if telefone_conectado[3:] == x:
            lista_maturacao.remove(telefone_conectado)
    return lista_maturacao


def wait_element(by, elemento, webdriver):
    print(f'Tentando encontrar "{elemento}" by {by}')
    if webdriver.find_elements(by, elemento):
        return True
    return False


def browser(session):
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument('lang=pt-br')
    options.add_argument(
        f'--user-data-dir=/utils/sessions/{session}')
    return options


def whatsapp(options, lista_maturacao):

    driver = Chrome(options=options)

    driver.get("https://web.whatsapp.com/")

    wdw = WebDriverWait(driver, 300, poll_frequency=2)

    esperar_carregar_whatsapp = partial(
        wait_element,   By.CSS_SELECTOR, "div[title='Caixa de texto de pesquisa']")

    wdw.until(esperar_carregar_whatsapp, 'Erro ao carregar whatsapp.')

    try:

        while True:

            numero = random.choice(lista_maturacao)
            msg = random.choice(conversas)
            caixa_de_pesquisa = driver.find_element(
                By.CSS_SELECTOR, "div[title='Caixa de texto de pesquisa']")
            caixa_de_pesquisa.send_keys(numero)
            caixa_de_pesquisa.send_keys(Keys.ENTER)
            time.sleep(random.randint(11, 18))
            caixa_de_msg = driver.find_element(
                By.CSS_SELECTOR, "div[title='Mensagem']")
            time.sleep(random.randint(10, 20))
            caixa_de_msg.send_keys(msg)
            time.sleep(random.randint(2, 6))
            caixa_de_msg.send_keys(Keys.ENTER)
            time.sleep(random.randint(9, 13))
            caixa_de_pesquisa.click()
            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            time.sleep(8)

    except:
        print('AGUARDANDO...')
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(5)
