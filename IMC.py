#Calcular o IMC

import dearpygui.dearpygui as dpg

dpg.create_context()

def imctotal():
    peso = dpg.get_value("peso")
    altura = dpg.get_value("altura")

    try:
        peso = float(peso)
        altura = float(altura)
        imc = peso / (altura * altura)

        dpg.set_value("resultado", f"IMC {imc:,.2f}")
    except ValueError:

        dpg.set_value("resultado","Erro: Por favor, insira valores numéricos válidos")

dpg.create_viewport(title='Total IMC', width=700, height=300)

with dpg.window(label="Valor IMC", width=600, height=300):
    # Adiciona um campo de texto para o usuário inserir o preço FIPE
    dpg.add_input_text(label="Seu peso", tag="peso")
    # Adiciona um campo de texto para o usuário inserir a nota de avaliação
    dpg.add_input_text(label="Sua altura", tag="altura")
    # Adiciona um botão que, quando clicado, chama a função 'calcular_preco'
    dpg.add_button(label="Calcular IMC", callback=imctotal)
    # Adiciona um espaço para exibir o resultado ou mensagens de erro
    dpg.add_text("", tag="resultado")

dpg.setup_dearpygui()
dpg.show_viewport()
# Inicia o loop de eventos da interface, onde a aplicação efetivamente roda e espera por interações do usuário
dpg.start_dearpygui()
# Destroi o contexto da aplicação após o fechamento da janela, liberando recursos
dpg.destroy_context()