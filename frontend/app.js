async function scanFridge() {
    const fileInput = document.getElementById('imageInput');
    const resultsDiv = document.getElementById('results');
    
    if (fileInput.files.length === 0) return alert("Choisis une photo !");

    resultsDiv.innerHTML = "Analyse en cours...";
    
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    try {
        const response = await fetch('http://localhost:8000/analyze', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();
        
        resultsDiv.innerHTML = "Ingrédients trouvés : " + (data.ingredients.join(', ') || "Aucun");
    } catch (error) {
        resultsDiv.innerHTML = "Erreur de connexion au serveur.";
    }
}