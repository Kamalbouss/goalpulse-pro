let selectedType = 'marketing';

document.querySelectorAll('.type-card').forEach(card => {
    card.addEventListener('click', () => {
        document.querySelectorAll('.type-card').forEach(c => c.style.opacity = '0.6');
        card.style.opacity = '1';
        selectedType = card.dataset.type;
    });
});

document.getElementById('video-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const prompt = document.getElementById('prompt').value;
    const language = document.getElementById('language').value;
    
    try {
        const response = await fetch('/api/generate-video', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                prompt: prompt,
                video_type: selectedType,
                language: language
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            document.getElementById('result').innerHTML = `
                <div class="success">
                    <h3>✅ تم إنشاء الفيديو!</h3>
                    <p><strong>السكريبت:</strong> ${data.script}</p>
                    <p><strong>الفيديو:</strong> ${data.video_url}</p>
                </div>
            `;
        }
    } catch (error) {
        console.error('Error:', error);
    }
});

function scrollToGenerator() {
    document.getElementById('generator').scrollIntoView({ behavior: 'smooth' });
}
