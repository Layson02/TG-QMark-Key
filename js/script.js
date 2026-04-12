document.getElementById('generateBtn').addEventListener('click', () => {
    const baseKeyInput = document.getElementById('baseKey').value.toUpperCase().trim();
    const resultsDiv = document.getElementById('results');
    
    resultsDiv.innerHTML = '';

    if (!baseKeyInput.includes('?')) {
        alert('Atenção: A chave precisa conter o caractere "?" para funcionar.');
        return;
    }

    for (let i = 9; i >= 0; i--) {
        const newKey = baseKeyInput.replace('?', i);
        
        const row = document.createElement('div');
        row.className = 'key-row';

        const span = document.createElement('span');
        span.className = 'key-text';
        span.textContent = newKey;

        const copyBtn = document.createElement('button');
        copyBtn.className = 'copy-btn';
        copyBtn.textContent = 'Copiar';
        
        copyBtn.addEventListener('click', async () => {
            try {
                await navigator.clipboard.writeText(newKey);
                copyBtn.textContent = 'Copiado!';
                copyBtn.classList.add('copied');
                
                setTimeout(() => {
                    copyBtn.textContent = 'Copiar';
                    copyBtn.classList.remove('copied');
                }, 1200);
            } catch (err) {
                alert('Erro ao copiar para a área de transferência.');
            }
        });

        row.appendChild(span);
        row.appendChild(copyBtn);
        resultsDiv.appendChild(row);
    }
});