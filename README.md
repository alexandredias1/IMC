# Calculadora de IMC

Este é um script em Python que utiliza a biblioteca Dear PyGui para criar uma interface gráfica simples que calcula o Índice de Massa Corporal (IMC) com base no peso e altura fornecidos pelo usuário.

## Descrição

O script cria uma interface gráfica onde o usuário pode inserir seu peso e altura. Quando o usuário clica no botão "Calcular IMC", o script calcula o IMC e exibe o resultado na tela. Se os valores inseridos não forem numéricos, uma mensagem de erro será exibida.

## Funcionalidades

- Inserir peso.
- Inserir altura.
- Calcular e exibir o IMC.
- Exibir mensagens de erro para entradas inválidas.

## Como usar

1. Certifique-se de ter o Python instalado em seu sistema.
2. Instale a biblioteca Dear PyGui usando o comando `pip install dearpygui`.
3. Salve o script em um arquivo com a extensão `.py` (por exemplo, `calculadora_imc.py`).
4. Abra um terminal ou prompt de comando.
5. Navegue até o diretório onde o script foi salvo.
6. Execute o script com o comando `python calculadora_imc.py`.
7. Insira seu peso e altura nos campos apropriados e clique em "Calcular IMC" para ver o resultado.

## Exemplo de uso

```python
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
        dpg.set_value("resultado", "Erro: Por favor, insira valores numéricos válidos")

dpg.create_viewport(title='Total IMC', width=700, height=300)

with dpg.window(label="Valor IMC", width=600, height=300):
    dpg.add_input_text(label="Seu peso", tag="peso")
    dpg.add_input_text(label="Sua altura", tag="altura")
    dpg.add_button(label="Calcular IMC", callback=imctotal)
    dpg.add_text("", tag="resultado")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
