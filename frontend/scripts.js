// Adiciona comportamento ao formulário
document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    
    form.addEventListener("submit", async (event) => {
        event.preventDefault(); // Evita o recarregamento da página

        // Coleta os dados do formulário
        const formData = new FormData(form);
        const jsonData = Object.fromEntries(formData.entries());

        // Exibe os dados no console (para depuração)
        console.log("Dados enviados:", jsonData);

        try {
            // Envia os dados para a API FastAPI
            const response = await fetch("http://127.0.0.1:8000/prever", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(jsonData)
            });

            // Processa a resposta da API
            if (response.ok) {
                const result = await response.json();
                alert(`Resultado da previsão: ${JSON.stringify(result)}`);
            } else {
                alert("Erro ao enviar os dados. Verifique o servidor!");
            }
        } catch (error) {
            console.error("Erro ao enviar os dados:", error);
            alert("Erro ao conectar ao servidor. Verifique a conexão!");
        }
    });
});