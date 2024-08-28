document.getElementById('btn').addEventListener('click', function() {
    // Altera o texto de um parágrafo
    let p = document.createElement('p');
    p.id = 'meuParagrafo';
    p.innerText = 'Texto alterado!';
    document.body.appendChild(p);

    // Muda a cor de fundo de um div
    let div = document.createElement('div');
    div.id = 'meuDiv';
    div.style.width = '200px';
    div.style.height = '100px';
    div.style.backgroundColor = 'lightblue';
    div.innerText = 'Este é o div que mudou de cor.';
    document.body.appendChild(div);

    // Desabilita todos os inputs de texto na página
    document.querySelectorAll('input[type="text"]').forEach(function(input) {
        input.disabled = true;
    });
});
