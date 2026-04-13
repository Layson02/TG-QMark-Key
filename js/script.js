document.getElementById('generateBtn').addEventListener('click', () => {
    const baseKeyInput = document.getElementById('baseKey').value.toUpperCase().trim();
    const resultsDiv = document.getElementById('results');
    
    resultsDiv.innerHTML = '';

    if (!baseKeyInput.includes('?')) {
        alert('Atenção: O código precisa conter o caractere "?" para funcionar.');
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
                row.classList.add('copied-state');
                
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

document.getElementById('advancedBtn').addEventListener('click', async () => {
    const baseKeyInput = document.getElementById('baseKey').value.toUpperCase().trim();
    
    if (!baseKeyInput.includes('?')) {
        alert('Atenção: O código precisa conter o caractere "?" para funcionar.');
        return;
    }

    let keyList = [];
    for (let i = 9; i >= 0; i--) {
        keyList.push(baseKeyInput.replace('?', i));
    }
    
    try {
        await navigator.clipboard.writeText(keyList.join('\n'));
        const btn = document.getElementById('advancedBtn');
        const originalText = btn.textContent;
        btn.textContent = 'Copiado para o Macro!';
        setTimeout(() => {
            btn.textContent = originalText;
        }, 2000);
    } catch (err) {
        alert('Erro ao copiar a lista.');
    }
});

document.querySelectorAll('.popup-link').forEach(link => {
    link.addEventListener('click', e => {
        e.preventDefault();
        window.open(link.href, 'SteamWindow', 'width=1000,height=800,top=100,left=100,menubar=no,toolbar=no,location=no,status=no');
    });
});