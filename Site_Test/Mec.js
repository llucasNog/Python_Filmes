function adicionarFilme() {
  
    const nome = document.getElementById("nome").value;
    const ano = document.getElementById("ano").value;
    const genero = document.getElementById("genero").value;
    const descricao = document.getElementById("descricao").value;
    const imagemUrl = document.getElementById("imagemUrl").value;
    const card = document.createElement("div");
    card.classList.add("card");
    const img = document.createElement("img");
    img.src = imagemUrl;
    img.alt = nome;
    card.appendChild(img);


    const info = document.createElement("div");
    info.classList.add("card-info");
    const titulo = document.createElement("h3");
    titulo.textContent = nome;
    info.appendChild(titulo);
    const detalhes = document.createElement("p");
    detalhes.textContent = `${genero} | ${ano}`;
    info.appendChild(detalhes);

    const descricaoTexto = document.createElement("p");
    descricaoTexto.classList.add("descricao");
    descricaoTexto.textContent = descricao;
    info.appendChild(descricaoTexto);
    card.appendChild(info);
    document.getElementById("catalogo").appendChild(card);
    document.getElementById("nome").value = "";
    document.getElementById("ano").value = "";
    document.getElementById("genero").value = "";
    document.getElementById("descricao").value = "";
    document.getElementById("imagemUrl").value = "";
}
